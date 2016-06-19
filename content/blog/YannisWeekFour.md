Title: LSH Parallelization
Date: 2016-06-19 20:20:20
Tags: gsoc, lsh, multiprobe, openMP, parallel
Author: Yannis Mentekidis

I have done a few things this week on the LSH code, but I want to talk mainly about parallelization of the `LSHSearch` object, a topic which I find very interesting.

First off, a few things to consider:

a) Parallelization should be as transparent as possible. Not everyone is familiar and/or comfortable with parallel frameworks and concepts, and we shouldn't make life hard for future code maintainers/developers.

b) Parallelization, if done the wrong way, can lead to all sorts of pain: very slow code (mainly because of [thread contention](http://stackoverflow.com/questions/1970345/what-is-thread-contention)), deadlocks, correctness errors, to name a few.

c) At the same time, parallelization is very important for a scalable library that deals with large datasets, such as mlpack. If done correctly, it can give an important bump in performance, especially since virtually every machine is multicore now.

So we need to keep (a) and (c) in mind while being careful to not fall in any of the traps mentioned in (b). (a) is easy to do with OpenMP, and we should also try to use only the very basic constructs - parallel for, let's say.

Now let's talk specifically about the LSH code. The main time waster there is  the search we do for each query, after the object has been trained with a reference set.

The way mlpack does this is there is a for loop, inside which, codes are computed for each query, and then other points with the same code are assembled into a candidate set where we then perform naive kNN. There's two possible paths to parallelization here:

1. We can focus on having `LSHSearch::Search` process queries in parallel. This way, whenever this function is called with an array of queries, OpenMP will let us process different queries on different cores.
2. We can instead try to reduce the cost of each individual query, by parallelizing the `ReturnIndicesFromTable` and `BaseCase` functions.

**Option (1)** has several benefits: 

 - When ran with a large query set, the processing cores will be utilized very well - there's plenty of work to go around, so we simply spawn threads and divide work among them.
 - It is trivial to implement and embarrassingly parallel, meaning the more threads we spawn (up to the number of queries) the faster we will be.
 - It should cause an immediate and noticeable bump in performance.

But, this option also has a problem: If the user is running single-query searches, then this will not benefit them at all. That is, we have increased the **number of queries we process per second** but have not decreased the **time required for each query**.

Option 2 serves exactly that purpose: By parallelizing the query processing code itself, each query will complete faster. In use cases where users have a model of LSH already computed, and receive and process queries in real time, this makes much more sense than a parallelization of the query-processing mechanism.

The downside to this is, the part of the process we actually can parallelize is smaller, and isn't embarrassingly parallel. Still, it can benefit quite a lot.

But wait, the upsides and downsides are flipped in these two cases. Couldn't we somehow reap the benefits of both methods?

Yes, we could - by utilizing a hybrid parallelization model. The way to do this is for LSHSearch to keep track of the number of threads it currently uses as well as the maximum number of threads it is allowed to use (by default, equal to the number of machine cores) and then if it realizes that it is not taking advantage of the full machine capabilities, also use the per-query parallelization method.

Fortunately, OpenMP makes life very easy for us, with the `if` clause in its parallelization directive. The `if` clause is evaluated, and threads are spawned only if it evaluates to true. So, we can do something like

```
#pragma omp parallel for \
	if (numThreadsUsed <= maxThreads) \
	num_threads (maxThreads - numThreadsUsed)
	...
```

I have already begun implementing this. I've changed the code in LSHSearch to provide for the thread book-keeping, and have completed the parallel query processing implementation.

Of course, at the same time, we should take care that what we are doing is correct (point c on my list). To do that, I've added yet another unit test to the LSHSearch suite, which performs two searches with the same query set - one that uses only one thread and one that uses the maximum number. These two processes should (and indeed do) return the same thing.
Title: LSH optimizations, modifications, and benchmarking
Date: 2016-06-06 20:20:20
Tags: gsoc, lsh, multiprobe
Author: Yannis Mentekidis

I began this week by debugging my multiprobe implementation which I discussed in my previous post. The algorithm is quite complicated and so I wanted to make sure it runs correctly before moving on to benchmarking and optimization.

Sure enough, I found a lot of minor bugs lying here and there which the tests I had written didn't catch. That worried me, so I decided to write better tests - my idea was to add some simple deterministic test cases.

To do that, I needed to improve access to LSHSearch object's projection tables, which are randomly generated - to have deterministic tests, you need to be able to specify tables instead of allowing the object to generate random ones for you.

In the process of modifying the LSHSearch code to do that, Ryan and I also decided to make a few other modifications, namely

1) Change the data structure that stores the projection tables from an std::vector to an arma::cube. Each slice of the cube is a projection table. This conserves memory and simplifies the code.

2) Change the implementation of the second level hashing. In the current version, an arma::Mat<size_t> table is created where each row corresponds to a hash bucket and stores indices to points hashed to that bucket. This is inefficient, both because the default secondHashSize is pretty large and because the number of points in each bucket might be uneven - so the resulting table is quite sparse. After some demo codes and discussion, we decided on a solution to these two problems.

So, with LSHSearch transparent, more easily testable and more efficient, we are now ready to perform benchmarks of single- and multiprobe LSH, see what we can optimize in the multiprobe code, and then move on to parallelization. All this will start today, so stay tuned :D
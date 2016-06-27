Title: LSH Parallelization
Date: 2016-06-27 20:20:20
Tags: gsoc, lsh, multiprobe, openMP, parallel
Author: Yannis Mentekidis

This week I focused on implementing the parallelization changes I discussed in my previous blog post. I also spent some time on bug fixes and style changes of Multiprobe LSH, but I will not bore you with that.

# Processing Queries in Parallel

First, I parallelized the query processing code. This was pretty straightforward since OpenMP lets us define private and shared variables and takes care of memory access by itself. 

Here's a nice example of *why* memory access becomes a concern when dealing with parallel code.

Let's say you're on vacation in a nice Greek beach, and you run out of money. You call your mom to deposit some on your bank account but she doesn't answer, so you leave a message and then call your dad. Your dad answers and runs out to send you money through the ATM. While he's out, your mom listens to the message and goes online to also send you money... 

So, your dad at the ATM and your mom through e-banking both perform these actions:

```
// balance = how much money you have. In the beginning this is 0.
balance = read_account_balance(); 
balance += 100; // the new deposit 
write_account_balance(balance); // update balance
```

But, because the bank you use doesn't employ great programmers, so they didn't care about memory access by multithreaded applications. So these commands are executed like this:

```
balance_mom = read_account_balance(); // mom knows you have 0
balance_mom += 100;
balance_dad = read_account_balance(); // dad knows you have 0
write_account_balance_mom(balance_mom); // mom just set your balance to 100
balance_dad += 200; // dad is more generous
write_account_balance_dad(balance_dad); // dad just set your balance to 200
```

Well, that's a problem - both mom and dad gave you money, but you only received 200 out of the 300 total. The reason is that the code is what is called a "critical segment" - a dangerous point where no two threads are safe to operate at the same time.

Does this mean we don't get to use parallelism in fear of ruining our results? Of course not! We just need to verify that what we are doing is correct - essentially forbidding parallel execution of the (usually very small) parts of the code that are critical segments.

OpenMP can force single-core execution of parts of the code with `#pragma omp atomic` (for one critical expression) or `#pragma omp critical` (for longer pieces of code).


# Thread book-keeping

Once I was done with that and had it tested, I started implementing code to keep track of how many threads we use. That code started becoming very complicated, so I considered implementing a thread-control class and managing threads through it, but that has the potential of complicating the code too much. Many of the parts we're intervening with already have an increased level of code complexity (long functions with a lot of branching) and so adding more complexity might make the next person to look at the code want to learn where I leave and come murder me - something I would very much like to avoid.

So, I ended up going with a simpler solution. OpenMP by default does not allow for nested parallelism - that is, it doesn't allow a spawned thread to spawn threads of its own. This is very good: it's easy to accidentally get yourself in recursive situations where spawning more threads that spawn more threads (and so on) leads to either the program to crash or it being very slow.

Since the code I want to parallelize further is nested inside parallel regions, it will, by default, be executed by only one thread. If, however, a user wants to enable that parallelism as well (for example in the live-query processing scheme I described in the previous post), then they can enable OpenMP's nested parallelism by setting the environment variable `OMP_NESTED` to `TRUE`.

# Further parallelism

For now, I have only parallelized the for loops inside `ReturnIndicesFromTables()`, but they are not the bottleneck - `find()` and `unique()` are. So this week I plan to implement parallel versions of these functions and add tests for the second level of parallelism. Once that is done, the chapter of LSH parallelization will be over :)
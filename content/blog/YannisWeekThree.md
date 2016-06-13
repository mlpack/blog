Title: LSH Utility Features, Multiprobe LSH Benchmarking
Date: 2016-06-13 20:20:20
Tags: gsoc, lsh, multiprobe, optimization
Author: Yannis Mentekidis

This is week 3 of GSoC and, according to plan, I am still working on multiprobe LSH. I thought this would have progressed faster - since a first working version of the algorithm was actually completed by the end of Week 1, but I learned that debugging and testing machine learning algorithms is actually harder than I expected :)

I started week 3 by implementing a function in LSHSearch that computes recall given a reference set of neighbors and the neighbors found by LSH. This functionality is now available through the mlpack_lsh binary using the -t switch and specifying a true neighbor indices file. Computing recall is a very useful step in LSH parameter tuning, so I thought it would be nice to provide this simple computation.

I also implemented a few deterministic tests for LSH. Now we can be relatively sure that what we do doesn't break the algorithm but only improves it. The deterministic tests essentially use given projection tables, so that disjoint clusters of points merge or don't merge controllably.

Finally I started running tests on single- and multiprobe LSH. I've found that different datasets behave differently here, some benefiting from multiprobe while some being better off without it. Profiling with gprof showed that the computation of additional probing bin codes doesn't affect performance significantly (usually accounts for 2-4% of total time), so now I'm trying to understand what the bottleneck is, precisely.

The two ideas I have regarding this is that either the resulting candidate set is very large in some cases, and so the resulting final linear search is what affects performance, or that the process of exploring so many additional bins is what causes these unpleasant results. In any case, I will investigate more.

By this week's end, I will hopefully be finished with all optimizations that occur from profiling and tests of multiprobe LSH, and will have started parallelization with OpenMP.
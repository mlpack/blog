@brief Profiling for parallelization and parallel stochastic optimization methods - Summary
@author Shikhar Bhardwaj
@page profiling-for-parallelization-and-parallel-stochastic-optimization-methods-summary Profiling for parallelization and parallel stochastic optimization methods - Summary
@date 2017-08-23 22:05:00

@section profiling-for-parallelization-and-parallel-stochastic-optimization-methods-summary Profiling for parallelization and parallel stochastic optimization methods - Summary

As we are fast approaching the final date ending final evaluation period for GSoC for this year, I think now is the right time to make a cumulative account of all the work done over the past 12 weeks during this project.

Initially, the accepted proposal was about the implementation of stochastic optimization methods, but after an agreement, we decided to include some aspects of the "Profiling for parallelisation" proposal as part of this project.

The primary goal of the "Profiling for parallelisation" project was to find parts of the library which could benefit from a parallel implementation and modify them to take advantage of multiple cores using OpenMP. On the other hand, "Parallel stochastic optimization methods" was concerned with the implementation of parallel approaches to optimization algorithms.

## Executive summary
Here is the list of Pull Requests with work related to this project. These PRs have all the code that was intended to be committed to the library :

- [#1015:Add tests to the CTest framework](https://github.com/mlpack/mlpack/pull/1015)
- [#1024:Parallel implementation of NaiveKMeans](https://github.com/mlpack/mlpack/pull/1024)
- [#1037:Implementation of parallel SGD](https://github.com/mlpack/mlpack/pull/1037)
- [#1075:Implementation of Stochastic Coordinate Descent](https://github.com/mlpack/mlpack/pull/1075)

The list of commits merged into the codebase is [here](https://github.com/mlpack/mlpack/commits?author=shikharbhardwaj). [Here](https://github.com/mlpack/mlpack/graphs/contributors?from=2017-05-31&type=c) is a better visualisation of the contributions made during GSoC.

In addition to the above library code, I wrote a number of benchmarks and examples to try out different ideas and gather more information about the performance of existing implementations in and outside of `mlpack`. Some important ones are listed [here](https://gist.github.com/shikharbhardwaj/a8fcb0eb6233459842cf91d4f88bb19e).

A weekly update of the progress on the project was posted as blog posts on this blog, which can be cumulatively found [here](http://www.mlpack.org/gsocblog/ShikharBhardwajPage.html).

  - Parallel testing framework: This part of the project involved adding the tests under the Boost unit testing framework to the CTest test runner included with CMake, which would allow for spawning of multiple jobs and make testing faster. For automating this process, a CMake script for parsing the required test suite names was written. Overall, there is about 2x reduction in testing times with four jobs.

  - Profiling for parallelisation: I wrote benchmarks for finding computational bottlenecks in `mlpack` code. KMeans was found to be easily parallelizable with `OpenMP`, giving around 3.5x speedup with the parallel implementation. Ideas for profiling and parallelisation were drawn from [this paper](https://papers.nips.cc/paper/3150-map-reduce-for-machine-learning-on-multicore).

  - Implementation of parallel `SGD`: I worked on the implementation of a parallel variant of Stochastic Gradient descent, based on the "HOGWILD!" scheme of unsynchronised updates between various threads, described by [this paper](https://arxiv.org/abs/1106.5730). The algorithm has been implemented with OpenMP, which was able to generate the right primitives for a lock-free approach, as required by the paper. Convergence is much faster due to the computation of sparse gradients, and the gradient updates take much less time as compared to other optimizers.

  - Implementation of parallel `SCD`: This involved implementation of another optimizer which worked with partial gradients of the loss functions to update disjoint parts of the decision variable, being trivially parallelizable. The PR for the sequential optimizer is in the final phase for the merge. The changes involved for parallelization should be trivial, as most of the required work has been done in the sequential version. As more changes needed to be added to the `FunctionType` policy in `mlpack`, some documentation highlighting the various types of FunctionType requirements was also added as a part of the work on this optimizer.

## Highlights
Working on this project made me appreciate the kind of power a robust API like OpenMP brings. With minimal changes to existing code, fast, cross-platform multi core implementations could be written which scale nearly linearly with the number of threads. Particularly, the implementation of `HOGWILD!` was much less complex with OpenMP involved to take over the work-sharing and synchronisation, while providing equivalent (or better) performance than a hand-rolled implementation of a thread pool and memory barriers.

## Future work
Some ideas which would build upon work done during this project over the summer :

- More algorithms in `mlpack` need to be profiled for potential parallelization. One particularly interesting and major change would be with the introduction of parallel tree traversers (although the impact of such an implementation needs to be analyzed if it will be worth the time and effort for parallelization).
- The implementation of `SCD` needs some trivial changes to work on multiple cores.
- `SCD` could also use a line search algorithm instead of gradients to optimize the function under consideration, possibly leading to a much faster optimizer.
- An in-depth empirical analysis of the implemented parallel optimizers, with different problems and datasets.

## Conclusion
This summer has been a great learning experience for me, from not only the work done during my project but also seeing the constant flow of interesting work from the projects from other students.
I would like to thank Yannis, Ryan and Marcus for their valuable time and guidance over the course of the entire summer to make this project an fundamental part of my experience as a developer.
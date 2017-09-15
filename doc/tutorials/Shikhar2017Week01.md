@brief Profiling for parallelization and parallel stochastic optimization methods - Week 1
@author Shikhar Bhardwaj
@page Shikhar2017WeekOne Profiling for parallelization and parallel stochastic optimization methods - Week 1
@date 2017-06-05 17:14:00

@section Shikhar2017WeekOne Profiling for parallelization and parallel stochastic optimization methods - Week 1

This summer, I'll be working on the parallel implementations of
the sequential algorithms already implemented in mlpack to improve their
performance on multicore systems.

I began week 1 by starting with the integration of CTest in the mlpack testing
interface. It makes testing faster by making multiple jobs run in parallel,
making use of the available extra threads, reducing  development time. The
intial results look quite promising, with around 2x reduction in [test
times](https://gist.github.com/shikharbhardwaj/12445adf0d952f59be7f1ef4a5fcb872#file-ctest-times)
while running 4 jobs in parallel. The PR opened for introducing this feature in
the mlpack build system is [here.](https://github.com/mlpack/mlpack/pull/1015)
Currently, I am working on automating the process of adding tests to CTest by
getting the test suite names and procedurally adding them to the list of tests.

In the meantime, I have been writing benchmarks and profiling the algorithms
which are to be implemented in parallel to find the existing bottlenecks and the
expected performance improvements from the parallel implementations.

In the coming weeks, my work will mainly be focussed on implemeneting the
algorithms with significant scope for improvement of performance in their
parallel versions and finding out more ways of improving and scaling mlpack's
performance on multicore systems.
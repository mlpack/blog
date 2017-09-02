@brief Profiling for parallelization and parallel stochastic optimization methods - Week 5
@author Shikhar Bhardwaj
@page Shikhar2017WeekFive Profiling for parallelization and parallel stochastic optimization methods - Week 5
@date 2017-07-04 17:26:00

@section Shikhar2017WeekFive Profiling for parallelization and parallel stochastic optimization methods - Week 5

As mentioned in the earlier blog post, this week was primarily focussed on adding more
tests for the implementation of Parallel SGD, along with progress on the matrix completion
example from the paper. I have made some improvements to the code based on initial reviews,
while adding new parts.

Both the implemented examples from the paper can be added as separate methods to mlpack. Once
enough tests are added, I'll run the methods on the datasets from the paper. While waiting for
an in depth review on the PR, I'll work on adding more tests for SparseSVM and SparseMC.
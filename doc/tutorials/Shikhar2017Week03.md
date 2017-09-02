@brief Profiling for parallelization and parallel stochastic optimization methods - Week 3
@author Shikhar Bhardwaj
@page Shikhar2017WeekThree Profiling for parallelization and parallel stochastic optimization methods - Week 3
@date 2017-06-21 15:14:00

@section Shikhar2017WeekThree Profiling for parallelization and parallel stochastic optimization methods - Week 3

During week 3, I finished up work on the parallel implementation of KMeans, making the mlpack
implementation nearly 4x faster with 4 threads available. The next algorithms for profiling would
be GMMs and dual tree traversers. For now, I have started to focus on the other aspect of my 
project, the implementation of parallel stochastic optimization methods.

I have discussed about the implementation of parallel SGD with the HOGWILD! scheme of update with
Yannis and the changes to the DecomposableFunctionType interface to carry the necessary details
for the HOGWILD! update on separate processors. Some of these details are problem specific and 
the primary challenge in designing the interface is to preserve genericity in the Optimizer
to allow users to write their own loss functions with minimal effort.

Next, I'll open up a PR with the initial implementation of this interface for further discussion
and testing.
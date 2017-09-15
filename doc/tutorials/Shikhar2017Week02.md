@brief Profiling for parallelization and parallel stochastic optimization methods - Week 2
@author Shikhar Bhardwaj
@page Shikhar2017WeekTwo Profiling for parallelization and parallel stochastic optimization methods - Week 2
@date 2017-06-13 18:14:00

@section Shikhar2017WeekTwo Profiling for parallelization and parallel stochastic optimization methods - Week 2

Week 2 continued with finishing up work on the CTest PR and profiling algorithms in 
mlpack for parallelization. The first algorithm under testing was the Gaussian Naive Bayes 
Classifier. The algorithm is simple enough to understand. For training, it takes a single 
pass through the data, calculating the mean and variance of each label for each feature, 
assuming that the feature values are sampled from a Gaussian PDF.

Since the algorithm is linear in the size of the dataset, any time spent in IO easily 
overshadows any time spent in computing the mean and variance of the data(which is very
small to begin with). Also, the original form of NBC (in a multi label setting) is not 
trivially parallelizable with OpenMP. A change in the algorithm was required, which would
increase the time complexity, while giving trivial gains from parallelization. Coupled with 
the fact that NBC cannot model complex datasets, we decided it was probably not worth the added
complexity to the codebase to add a parallel implementation of this algorithm. A few measurements
of the proposed implementation exist in this [gist](https://gist.github.com/shikharbhardwaj/238e0b152d7a575c9d2f6494208d87b1).

The next algorithm to be measured was KMeans. The implementation of NaiveKMeans was trivially 
parallelizable and profiling showed that most of the time was spent in computing the Metric(which is good).
The mlpack KMeans class uses NaiveKMeans as a subroutine and the parallel implementation can
be switched for the sequential one because of the same interface. The speedup in the initial
implementation is quite noticiable. [Here are the measurements](https://gist.github.com/shikharbhardwaj/89bf1f1e58b3730b4bfc00bb6373e222). I have opened up [#1024](https://github.com/mlpack/mlpack/pull/1024) with this implementation for 
discussion and further refinement.

Next, I will be going ahead with the implementation of HOGWILD! and possibly parallel dual-tree
traversal algorithms.
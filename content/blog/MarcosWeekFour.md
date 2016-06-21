Title: Approximate Nearest Neighbor Search - Week 4
Date: 2016-06-20 21:00:00
Tags: gsoc, knn, kfn
Author: Marcos Pividori

Last week, I completed the improvement of existing code for NSModel
[[1]](http://github.com/mlpack/mlpack/issues/674), using boost variant to manage
different options for tree types.

The general functionalities were implemented through visitor classes, taking
advantage of template specialization to differentiate those tree types that
accept leafSize as a parameter, where we need a slightly different procedure.

AppVeyor has shown some problems with the MSVC compiler, in the resolution of
template parameters of alias templates, similar to an old issue:
[[2]](https://github.com/mlpack/mlpack/issues/476)
We finally managed to fix this including some extra definitions.

All this work was merged in the PR:
[[3]](https://github.com/mlpack/mlpack/pull/693).

Also, I have been updating the benchmarking system to include an epsilon
parameter for neighbor search, not only with mlpack, but also with other
libraries like [ANN](https://www.cs.umd.edu/~mount/ANN/) and
[FLANN](http://www.cs.ubc.ca/research/flann/).

Now, I am working in adding a new view to the benchmarking system, to plot the
progress of a specific metric for different values of a method parameter. In
particular, we are interesting in analyzing the number of base cases and runtime
for different values of approximation error (epsilon). A trade-off between doing
neighbor search accurately and doing it quickly.

Next week, I plan to finish this comparison and start working in the
implementation of some alternative approaches like Spill Trees
[[4]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf).


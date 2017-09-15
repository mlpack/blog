@brief Approximate Nearest Neighbor Search - Week 3
@author Marcos Pividori
@page Marcos2016WeekThree Approximate Nearest Neighbor Search - Week 3
@date 2016-06-13 21:00:00

@section Marcos2016WeekThree Approximate Nearest Neighbor Search - Week 3

Last week, I finished the extension for approximate neighbor search
[[1]](http://github.com/mlpack/mlpack/pull/684).

Mainly, I modified the code to include an epsilon value, which represents the
accepted relative error. It is considered by the prune rules when deciding if
a given node combination should be analyzed.

When doing dual tree search, the best between the modified $B_1$ bound (with
epsilon) and the original $B_2$ bound is chosen. As was discussed in
[[2]](https://github.com/mlpack/mlpack/pull/684#discussion_r66614123),
with actual implementation, $B_2$ can not be relaxed to include the epsilon
value.

Then, I added many test cases with different values of epsilon and different
kind of trees (KDTree/BallTree/CoverTree), checking the relative error between
the approximated results and the true best candidates.

The command line tools: mlpack_knn and mlpack_kfn, were updated to include an
extra option "-e", to specify the relative error (default value: 0).
We have been discussing about which approximation parameters use for KFN in
[[3]](http://github.com/mlpack/mlpack/pull/684/files/07879a2cc79b35b10d7fae687d6e27ad90a9f2d7#r66611928).


Also, I have been working improving existing code for NSModel, as was suggested
by Sumedh in [[4]](http://github.com/mlpack/mlpack/issues/674). After
considering many options, boost variant seems to be the most appropiate.

Next week, I plan to continue working improving existing code and checking some
details. Also, I will do some comparisons in performance of exact vs approximate
neighbor search.
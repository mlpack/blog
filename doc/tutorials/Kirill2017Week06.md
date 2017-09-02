@brief Cross-Validation and Hyper-Parameter Tuning - Week 6
@author Kirill Mishchenko
@page Kirill2017WeekSix Cross-Validation and Hyper-Parameter Tuning - Week 6
@date 2017-07-10 12:45:00

@section Kirill2017WeekSix Cross-Validation and Hyper-Parameter Tuning - Week 6

During the sixth week I implemented k-fold cross-validation. I haven't sent it
for review yet since the previous PR
([#1044](https://github.com/mlpack/mlpack/pull/1044)) is still under
consideration, and the new code depends on this PR.

On the sixth week I also started to work on the hyper-parameter tuning module by
implementing a wrapper for cross-validation strategies. This wrapper serves for
adapting the interface of the cross-validation classes to the one that can be
utilized by the mlpack optimizers. It also makes it possible to bind some
arguments (hyper-parameters) to some specific values.

On the next week I plan to finish my work on the cross-validation wrapper and to
start implementing the grid-search optimizer (iterating through points on a
multidimensional grid).
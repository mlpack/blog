@brief Cross-Validation and Hyper-Parameter Tuning - Week 7
@author Kirill Mishchenko
@page Kirill2017WeekSeven Cross-Validation and Hyper-Parameter Tuning - Week 7
@date 2017-07-17 12:00:00

@section Kirill2017WeekSeven Cross-Validation and Hyper-Parameter Tuning - Week 7

During the seventh week I have been primarily working on implementation of
different parts of the hyper-parameter tuning module. I have implemented the
cross-validation wrapper that I mentioned previously, as well as grid-search
based optimization. The grid-search optimizer follows the same interface as
other mlpack optimizers, so it is possible to use it in other mlpack methods
too.

Now I'm working on a hyper-parameter tuner itself. It should be able to accept
different types of information for hyper-parameters - e.g. that some
hyper-parameters should be bound to particular values, while others be chosen
from sets of values.

I haven't sent any of the implemented parts for review yet since [my latest
PR](https://github.com/mlpack/mlpack/pull/1044)
is still under review (and the new code depends on this one). Once my latest PR
is merged and the hyper-parameter tuner is ready, I will send the whole
hyper-parameter tuning module as a PR.
@brief Implementing Essential Deep Learning Modules - Week 8
@author Shikhar Jaiswal
@page Shikhar2018Week08 Implementing Essential Deep Learning Modules - Week 8
@date 2018-07-08 11:12:00

@section Shikhar2018Week08 Implementing Essential Deep Learning Modules - Week 8

This week, we benchmarked the performance of our `GAN` module against `Tensorflow`'s runtimes, and worked out on optimizing the routines even further. Then, we went forward with implementing `EvaluateWithGradient()` function for all the variants, which gave us a straight performance improvement of `13%` over the previous update routine, cutting almost `45` minutes of training time.

Currently, `Tensorflow` has a training time of `4.5` hours (multi-threaded) and about `11` hours (single core aggregate), whereas `mlpack` has a runtime of `6.25` hours (single-threaded). We (Marcus, Ryan and Sumedh) have been discussing on parallelizing the `FFN` class in order to benchmark in a multi-threaded environment as well. However, we decided to go forward with implementing as many modules as we currently can, and later optimizing them as we go on benchmarking.

The `RBM` PR currrently passes tests for the stochastic input, and would have to be optimized for mini-batches, which would be done in Phase III. Phase II ends here, and I'm really glad that we were able to complete our planned goals so soon!

`Totsiens`

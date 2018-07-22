@brief Implementing Essential Deep Learning Modules - Week 10
@author Shikhar Jaiswal
@page Shikhar2018Week10 Implementing Essential Deep Learning Modules - Week 10
@date 2018-07-21 23:25:00

@section Shikhar2018Week10 Implementing Essential Deep Learning Modules - Week 10

We covered a lot of traction with the `RBM` pull request this week.

The original design of the `RBM` class, being based around individual templatised policies, was a little inefficient for trying different variations of the code, and passing simple parameters. Hence, the entire codebase was refactored to a `SFINAE` + `enable_if<>` paradigm, enabling us to just implement specific functions for the two policies: `BinaryRBM` and `SpikeSlabRBM`. This also led to substantial code-deduplication, and the outdated comments were also handled.

Moreover, we corrected our implementations of the tests for the two variants on the `Digits` dataset. A little bit of hyperparameter-tuning, and we were good to go on the tests as well. Currently, both the variants perform better than standard softmax regressors, having an accuracy north of `80%` currently. Though we could achieve even greater scores with more tuning, I think we atleast have been able to prove the effectveness of our implementations, and that should be the priority here. The PR is now complete and should be merged shortly.

More tests and optimizations to this code would follow next week.

`पुनर्दर्शनाय`

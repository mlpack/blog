@brief LMNN (via LRSDP) & BoostMetric Implementation - Week 5
@author Manish Kumar
@page Manish2018Week05 LMNN (via LRSDP) & BoostMetric Implementation - Week 5
@date 2018-06-18 16:30:00

@section Manish2018Week05 LMNN (via LRSDP) & BoostMetric Implementation - Week 5

Continuing the practice from previous weeks, last week too the main focus was on optimization. As a result, AMSGrad and BigBatchSGD came into the picture, performing even better than SGD on LMNN in combined terms of speed and final objective.

The optimizers traits w.r.t performance on LMNN also lead to the inclusion of a new term `passes`, The number of full passes on the dataset. Hence instead of `max_iterations`, the `passes` decide the number of `max_iterations` that AMSGrad, BigBatchSGD and SGD can take. 

Again as a part of optimization, a parameter `range` was included, which decides the interval after which impostors need to be re-calculated. It proved out to be a great milestone in the journey of LMNN optimization :) The basis for `range` is that the impostors don't show much change from an iteration to other successive iterations.

Apart from this setting up benchmarking system for LMNN was also in the spotlight. Though, debugging it took more time than expected. But, Now we have it ready. Benchmarking scripts for both the Mlpack's and Shogun's implementation are prepared and are in the process of being executed.

Hoping by this week we can conclude LMNN :)
@brief LMNN (via LRSDP) & BoostMetric Implementation - Week 7 & 8
@author Manish Kumar
@page Manish2018Week08 LMNN (via LRSDP) & BoostMetric Implementation - Week 7 & 8
@date 2018-07-09 05:00:00

@section Manish2018Week08 LMNN (via LRSDP) & BoostMetric Implementation - Week 7 & 8

We started the week by taking the well-known policy of divide and conquer into account in order to safely handle massive optimization tasks. That being so Ryan opened several issues dealing with each individual task. 

The optimization tasks mainly cover imposing bounds over the data points wherever possible, caching & adapting (in the newly transformed space) the reference & query trees to avoid re-construction of trees on every call to `Impostors()` and verifying the correctness of low-rank optimization. As of now, most of the bounds are derived (Thanks to Ryan!) and tested successfully. Apparently, results depend on the dataset considerably. Low-rank optimization also seems to work pretty decently. Hopefully, we will see some more decrement in runtime during the upcoming week.

And the best part is, we finally have LMNN merged. Thanks to Ryan and Marcus, the code and documentation were thoroughly fine-tuned before the merge. Probably, shortly we will start with Boostmetric implementation as well.

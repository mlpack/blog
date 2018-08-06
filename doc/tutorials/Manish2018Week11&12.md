@brief LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 11 & 12
@author Manish Kumar
@page Manish2018Week12 LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 11 & 12
@date 2018-08-06 11:00:00

@section Manish2018Week12 LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 11 & 12

Past two weeks we were working on finishing things up related to LMNN optimizations. We got some of the optimizations, mostly related to bounds, completely validated (in terms of correctness & speedups) and merged. Though work related to tree-based optimizations is still in progress. Hopefully, we will be able to successfully complete it shortly. Additionally, Ryan has been working over the LMNN target neighbors and impostors rules in order to avoid multiple passes of KNN during there computation. He has already witnessed significant speedups in this regard. 

Unfortunately, we are still seeing some bugs in the LMNN code related to BigBatchSGD optimizer, leading to build timeouts or more specifically execution is getting stuck at some point. Most likely the problem is related to shuffling of data points leading to changes in objective function. Rest assured, we are determined to solve this at the earliest.

Meanwhile, a PR related to BoostMetric has been opened. And perhaps it will be in its final stages very soon. Possibly some results validation and some amount of code optimization, wherever applicable will need to be taken care of.

Hopefully, we will be able to achieve all our goals we aimed for.
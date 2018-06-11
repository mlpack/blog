@brief LMNN (via LRSDP) & BoostMetric Implementation - Week 4
@author Manish Kumar
@page Manish2018Week04 LMNN (via LRSDP) & BoostMetric Implementation - Week 4
@date 2018-06-11 08:30:00

@section Manish2018Week04 LMNN (via LRSDP) & BoostMetric Implementation - Week 4

Last week a fair amount of debugging and optimization was performed. In regard to optimization, some of the repetitive calculation was avoided by caching the results in accordance with the decomposable function policy both in LMNN function and Constraints class.  We also performed quite a number of benchmarking tests on the full covertype dataset, which gave us some reasonable results, though running time was not good enough, it was clear that it can be improved a lot.

Apart from optimization, we faced an unacceptable objective divergence issue while using SGD optimizer which was causing some serious issues in other parts of code. For avoiding this we tried adding a penalty parameter to the objective but it didn't prove out to be a success. We also tried normalizing the objective matrix, though it worked but the overall optimization time was increased. Hence, we decided to check out other optimizers which support adaptive learning rate. Here, BigBatchSGD proves out to be the best choice. Some minor issues are needed to be taken care of before completely switching to BigBatchSGD.

Additionally, Low-rank distance learning support was added. It also gave considerable results. Some more optimizations ideas (like avoiding impostors calculation as much as possible) are in progress. Hopefully major things w.r.t LMNN will be concluded by the end of this  week.
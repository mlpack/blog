@brief Alternatives to Neighborhood-Based CF - Week 4
@author Wenhao Huang
@page Wenhao2018Week04 Alternatives to Neighborhood-Based CF - Week 4
@date 2018-06-11 23:00:00

@section Wenhao2018Week04 Alternatives to Neighborhood-Based CF - Week 4

This week I finished the remaining work (mostly of which are testing and debugging work) for data normalization after the PR of refactoring CF class was merged. There are a few improvements pointed out by review comments to do, and I am excited that it is close to be merged. (Many thanks to Marcus and Mikhail for reviewing the PR!). Based on my testing I found that it might be better if `RegSVD` or `BatchSVD` is used as default matrix factorizer, but I will open another PR dedicated to this issue later.

As for weights interpolation, all classes for neighbor search (`LMetricSearch<TPower>`, `CosineSearch`, `PearsonSearch`) and interpolation methods (`AverageInterpolation`, `RegressionInterpolation`, `SimilarityInterpolation`) are added. There is another interpolation method which is an improvement of `RegressionInterpolation` and it is also worth implementing. But to keep up with schedule I plan to implement this interpolation method after I finish my scheduled tasks in the following few weeks. The remaining work for the PR of weights interpolation is to templatize the current methods to use `NeighborSearchPolicy` and `InterpolationPolicy`, and to add tests for all neighbor search classes and interpolation classes.

According to my schedule, I need to test the added funtionalities, i.e. data normalization and weights interpolation, on a public dataset. The are some work left to do for weights interpolation so I am a bit behind schedule, but I will try to catch up. In the next week I will complete the remaining work for weights interpolation once the PR of data normalization is merged, and work on testing these methods on a public dataset.

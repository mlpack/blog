@brief Alternatives to Neighborhood-Based CF - Week 3
@author Wenhao Huang
@page Wenhao2018Week03 Alternatives to Neighborhood-Based CF - Week 3
@date 2018-06-04 20:00:00

@section Wenhao2018Week03 Alternatives to Neighborhood-Based CF - Week 3

During the third week, I first added two more classes for neighbor search: `CosineSearch` and `PearsonSearch`, which search for neighbors based on cosine similarity and pearson correlation. Instead of using neighborSearch directly with cosine/pearson distance, reference and query set are first normalized, so that we can use neighbor::KNN (i.e. neighborSearch with Euclidean distance and KDTree). Resulting neighbor similarities are used to calculate interpolation weights. Besides, I was working on the implmentation of `RegressionInterpolation` from [this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.443.300&rep=rep1&type=pdf) but it is not complete yet. The paper discusses `RegressionInterpolation` with sparse rating matrix. But as the current CF algorithm can generate a dense rating matrix, the exact implmentation of `RegressionInterpolation` might be different from that in the paper.

As for CF data normalization, when I was adding accuracy tests for data normalization, I noticed that the bound for prediction accuracy in testing is too large. However, when I set the bound to a reasonably smaller value, some tests would fail. I will spend some time in solving this issue next week.

For the fourth week, I plan to complete `RegressionInterpolation`, tests for data normalization, and keep working on templatizing some CF methods to take `NeighborSearchPolicy` and `InterpolationPolicy` as template parameters.

@brief Alternatives to Neighborhood-Based CF - Week 1
@author Wenhao Huang
@page Wenhao2018Week01 Alternatives to Neighborhood-Based CF - Week 1
@date 2018-05-20 22:40:00

@section Wenhao2018Week01 Alternatives to Neighborhood-Based CF - Week 1

The goal of my summer project is to improve the CF framework from different aspects, including rating normalization (aka. global effects removal), interpolation of neighborhood weights. I will also work on implmenting more expressive CF models like BiasSVD and SVD++.

For the first week, I have implmented all common-used data normalization methods: `OverallMeanNormalization`, `UserMeanNormalization`, `ItemMeanNormalization`, `ZScoreNormalization`, and `CombinedNormalization<>` which can apply several normalization methods in a sequential manner. Explanation on rating normalization and global effects removal can be found in [this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.443.300&rep=rep1&type=pdf). Data normalization in CF complies with policy-based design, so a user can easily write a customized data normalization class. Normalization class needs to implement `Normalize()` and `Denormalize()` methods which are used to process ratings in CF. I have run an experiment with these normalization methods and found that, with normalization added, the performance of CF with the default factorizer can be significantly improved.

For the next week, I plan to add tests for the normalization classes to ensure they produce reasonable prediction accuracy. I will also start to investigate and implment different weight interpolation poclies for aggregation of neighborhood ratings.

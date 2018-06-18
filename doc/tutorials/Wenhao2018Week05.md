@brief Alternatives to Neighborhood-Based CF - Week 5
@author Wenhao Huang
@page Wenhao2018Week05 Alternatives to Neighborhood-Based CF - Week 5
@date 2018-06-18 21:00:00

@section Wenhao2018Week05 Alternatives to Neighborhood-Based CF - Week 5

The first evaluation has passed and I am delighted to receive positive feedbacks. In week 5, firstly the PR for data normalization in CF was merged. Then I continued to work on neighbor search policies and interpolation policies. I templatized `Predict()` and `GetRecommendations()` so that the function templates can use different kinds of `NeighborSearchPolicies` and `InterpolationPolicies`. Tests have been added for the those classes. The PR for neighbor search and calculation of interpolation weights is ready to be reviewed and should be close to merge.

Following the plan, I also tested the performance of the current CF module with rencently added normalization methods, neighbor search policies and interpolation policies. MovieLens-100k dataset is used as benchmark dataset. The performance (represented by RMSE(root mean square error)) can be viewed [here](https://gist.github.com/Wenhao-H/8470c63f5063e18057af42e05c4549e0).

As for the following week, I will start working on implmentation of `BiasSVD` and `SVD++`, which are two models different from the current matrix-decomposition-based CF model in mlpack.

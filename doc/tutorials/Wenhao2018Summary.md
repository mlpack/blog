@brief Alternatives to Neighborhood-Based CF - Summary
@author Wenhao Huang
@page alternatives-to-neighborhood-based-cf Alternatives to Neighborhood-Based CF - Summary
@date 2018-08-12 7:00:00

@section alternatives-to-neighborhood-based-cf Alternatives to Neighborhood-Based CF - Summary

# Brief Summary

This blog summarizes the work I have done for my GSoC-2018 project [Alternatives to Neighborhood-Based CF][project]. The goal of my project is to add alternative algorithms to the Collaborative Filtering module in mlpack. The algorithms I have completed include different rating normalization methods, negihbor search methods, weight interpolation methods, and `BiasSVD`, `SVD++` models.

# Completed Algorithms

## Data Normalization

With data normalization in CF, raw ratings are normalized before performing matrix decomposition. When predicting missing rating, data is 'denormalized' to original scale. As this [benchmarking][benchmark] result shows, data normalization is important for improving the performance. The followings are brief explanations of different data normalization methods that have been implemented.

1. **NoNormalization** : Default normalization class. It doesn't perform any data normalization.
2. **OverallMeanNormalization** : Normalize ratings by substrating mean rating.
3. **UserMeanNormalization** : Normalize ratings by substracting the corresponding user's mean rating.
4. **ItemMeanNormalization** : Normalize ratings by substracting the corresponding item's mean rating.
5. **ZScoreNormalization** : Perform z-score normalization on ratings.
6. **CombinedNormalization** : Perform a sequence of normalization methods on ratings. For example, `CombinedNormalization<OverallMeanNormalization, UserMeanNormalization, ItemMeanNormalization>` performs `OverallMeanNormalization`, `UserMeanNormalization`, `ItemMeanNormalization` in sequence.

The code for data normalization can be found in folder `mlpack/src/mlpack/methods/cf/normalization`, or in PR [#1397][1397].

For more information on rating normalization, refer to [this paper][Koren2007].

## Neighbor Search

Only neighbor search of Euclidean distance was implemented before the start of this project. I refactored the code and added neighbor search methods of cosine distance and pearson correlation. The followings are brief explanations of different neighbor search methods that have been implemented.

1. **LMetricSearch** : Searching with l_p distatnce is the general case of searching with Euclidean distance. `EuclideanSearch` is the alias of `LMetricSearch<2>`.
2. **CosineSearch** : Search neighbors and return similarities using cosine distance. 
3. **PearsonSearch** : Search neighbors and return similarities using pearson correlation.

All simlarities returned by the methods above are restricted to be in the range [0, 1].

With normalized vectors, neighbor search of cosine/pearson distance is equivalent to neighbor search of Euclidean distance. Therefore, instead of performing neighbor search directly with cosine/pearson distance, vectors in reference/query set are normalized and then neighbor search of Euclidean distance is used.

The code for neighbor search policies can be found in folder `mlpack/src/mlpack/methods/cf/neighbor_search_policies`, or in PR [#1410][1410].

## Weight Interpolation

Before the start of this project, predicted rating is calculated as the average of neighbor's ratings. I refactored the code and added two more weight interpolation algorithms: `SimilarityInterpolation` where weights are based on neighbor similarities, and `RegressionInterpolation` where weights are calculated by solving a regression problem. The followings are brief explanations.

1. **AverageInterpolation** : Interpolation weights are identical and sum up to one.
2. **SimilarityInterpolation** : Interpolation weights are calculated as normalized similarities and sum up to one.
3. **RegressionInterpolation** : Interpolation weights are calculated by solving a regression problem.

With interpolation weights, the CF algorithm multiplies each neighbor's rating with it's weight and sums them to predict rating.

The code for weight interpolation policies can be found in folder `mlpack/src/mlpack/methods/cf/interpolation_policies`, or in PR [#1410][1410].

For more information on `RegressionInterpolation`, refer to [this paper][Koren2007].

## Bias SVD

BiasSVD is similar to regularizedSVD. The difference is that BiasSVD also models user/item bias. In BiasSVD, rating is predicted as 

$ r_{iu} = \mu + b_i + b_u + p_i * q_u $,

where $\mu$ is mean rating, $b_i$ is item bias, $b_u$ is user bias, $p_i$ item latent vector, $q_u$ is user latent vector.

Same as `RegularizedSVD`, `BiasSVD` is opmitzed using Stochastic Gradient Descent (SGD).

The code for BiasSVD can be found in folder `mlpack/src/mlpack/methods/bias_svd/`, or in PR [#1458][1458].

## SVD++

SVD++ is a more expressive model. Besides explicit ratings, SVD++ also takes implicit feedback as input and learns latent vectors to model implicit feedback. For each item, a latent vector is used to model the relationship between the item and a user in terms of implicit feedback.

In SVD++, rating is predicted as

$ r_{iu} = \mu + b_i + b_u + p_i * (q_u + \sum_{t \in I(u)}{y_t}) $,

where $I(u)$ is the set of items which user $u$ has interacted with, and $y_t$ is the latent vector to model the implicit feedback.

Same as `RegularizedSVD` and `BiasSVD`, `SVDPlusPlus` is optimized using Stochastic Gradient Descent (SGD).

The code for BiasSVD can be found in folder `mlpack/src/mlpack/methods/svdplusplus/`, or in PR [#1458][1458].

Please read [this paper][svdpp] for more explanation on SVD++.

## Other modifications/refactoring

1. To make addition of new cf models (e.g. BiasSVD, SVD++) easier, I refactored decomposition policies. The mofications are: 1) all model parameters are moved from `class CFType<>` to `class DecompositionPolicy`. 2) `DecompositionPolicy` has to implement method `GetRating()` to compute rating for given user and item. 3) `DecompositionPolicy` has to implement method `GetNeighborhood` to compute neighborhoods for given users. (This modification is in PR [#1458][1458]).
2. `class CFModel` is implemented to be used for cf main program. When `mlpack_cf` is executed from command line, `CFModel` is serialized instead of `class CFType<>`. `class CFModel` is needed for the main program because CFType is a class template. (This modification is in PR [#1397][1397]).

So far the PRs ([#1397][1397], [#1410][1410]) for data normalization, neighbor search, and weight interpolation have been merged. The PR ([#1458][1458]) for BiasSVD and SVD++ is pretty long and is still under reviewing and debugging, but it will also be merged soon.

# To Do

1. Add supports for alternative normalization methods, neighbor search methods and weight interpolation methods in cf main program. Currently the cf main program only supports `NoNormalization`, `EudlideanSearch` and `AverageInterpolation`.
2. Write automatic benchmarking scripts to compare the CF module in mlpack with other recommender system libraries.


# Acknowledgements
Working on my GSoC project this summer has been really amazing and rewarding. This is the first time I contirbute to an open-source library and I've found the fun in it. I want to thank Mikhail especially for reviewing my codes and giving useful suggestion on specific implementation of algorithms. I also want to thank Marcus, Ryan, and all community members who have been super helpful in answering my questions. Although GSoC is about to come to the end, I will still make contributions to mlpack library and work on improving the cf module and implementing other algorithms.

[project]: https://summerofcode.withgoogle.com/projects/#5422247402012672
[benchmark]: https://gist.github.com/Wenhao-H/8470c63f5063e18057af42e05c4549e0
[1397]: https://github.com/mlpack/mlpack/pull/1397
[1410]: https://github.com/mlpack/mlpack/pull/1410
[1458]: https://github.com/mlpack/mlpack/pull/1458
[Koren2007]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.129.4662&rep=rep1&type=pdf
[svdpp]: http://www.cs.rochester.edu/twiki/pub/Main/HarpSeminar/Factorization_Meets_the_Neighborhood-_a_Multifaceted_Collaborative_Filtering_Model.pdf

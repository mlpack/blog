@brief Alternatives to Neighborhood-Based CF - Week 2
@author Wenhao Huang
@page Wenhao2018Week02 Alternatives to Neighborhood-Based CF - Week 2
@date 2018-05-28 23:00:00

@section Wenhao2018Week02 Alternatives to Neighborhood-Based CF - Week 2

For the second week, I first read some materials on computing interpolation weights for neighborhood-based collaborative filtering. There are three methods I planned to implment: average interpolation, similarity-based interpolation, and regression-based interpolation. So far I have implmented `AverageInterpolation` and `SimilarityInterpolation`, and I am currently working on `RegressionInterpolation`. As for rating normalization, I merged codes of refactored CF class (thanks to Haritha for the refactoring work), and I am working to solve some issues that occur after the merge.

For the third week, I am going to modify methods in CF to use policy-design for weights interpolation and neighbor search, add `RegressionInterpolation`. After that I will do the remaining work of rating normalization.

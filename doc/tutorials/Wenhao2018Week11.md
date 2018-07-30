@brief Alternatives to Neighborhood-Based CF - Week 10 & 11
@author Wenhao Huang
@page Wenhao2018Week11 Alternatives to Neighborhood-Based CF - Week 10 & 11
@date 2018-07-31 00:20:00

@section Wenhao2018Week11 Alternatives to Neighborhood-Based CF - Week 10 & 11

The work to implement `BiasSVD` and `SVD++` is more than I have expected, and this task takes more time than scheduled. For the past two weeks, I first debug the errors in `BiasSVD` (thanks to Mikhail's careful review), and then finished the implementation of `SVDPlusPlus` class. After making sure that `SVDPlusPlus` is working reasonably, I implemented wrapper classes of `BiasSVD` and `SVDPlusPlus` which are used by `CFType<>` as decompostion policy. Then, I refactored `CFModel` so that the pointer to the actual model class is saved as `boost::variant<...>`. `BiasSVD` and `SVD++` are not supported in cf executable yet. I will implement the supports after this PR is merged (so that we are sure `BiasSVD` and `SVD++` are working properly). I also spent quite some time in debugging the Travis Test failure with regard to armadillo.

For the next week, I will carry on implementing test cases and complementing code comments. I will also start to work on CF benchmarking if time permits.

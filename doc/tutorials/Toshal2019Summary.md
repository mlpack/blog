@brief Implementing Essential Deep Learning Modules - Summary
@author Toshal Agrawal
@page Toshal2019Summary Implementing Essential Deep Learning Modules - Summary
@date 2019-08-26 03:43:00

@section Toshal2019Summary Implementing Essential Deep Learning Modules - Summary

# Overview

This summer I got an opportunity to work with `mlpack` organisation. My proposal for `Implementing Essential Deep Learning Modules` got selected, and under the mentorship of `Shikhar Jaiswal` and `Marcus Edel` I was working on it for the last three months.

The main aim of my project was to enhance the existing `Generative Adversarial Network (GANS)` framework present in `mlpack`. The target was to add some more `functionality` in `GANs` and to implement some new algorithms to `mlpack` such that performance of `GANs` is improved. The project also focussed on adding some new algorithms so that testing of `GANs` becomes feasible.

# Implementation

#### Improving Serialization of GANs

The first challenge in the existing `GAN` framework was to enable loading and saving the `GAN` model correctly. In `mlpack` the loading and saving of models was done with the help of `Boost Serialization`. The most important responsibility was to have complete consistency so that all the functionalities of the model are working perfectly fine after saving and loading the model. The Pull Request [#1770][1770] focussed on this and it will get merged soon.

#### Providing Option to Calculate Exact Objective

In order to make [Dual Optimizer](#dual-optimizer-for-gans) functionality efficient it was required to remove the overhead of calculating the objective over the entire data after optimization. In order to do so I opened [#109][109] in mlpack's `ensmallen` repository. It is merged and now ensmallen's `Decomposable` Optimizer's provide an option to user that weather he wish to calculate exact objective after optimization or not.

#### Dual Optimizer for GANs

Various research papers published related to `GANs` used two seperate Optimizer's in their experiments. However mlpack `GAN` framework had only one optimizer. Due to this testing of `GAN` was quite tedious. So the main aim of the [#1888][1888] Pull Request was to add `Dual Optimizer` functonality in GANs. The implementation of `Dual Optimizer` is quite complete and currently it's testing is going on.

#### Label Smoothing in GANs

One sided label smoothing mentioned in the [Improved GAN paper][improved-gan] was seen to give better result while training `GAN` model. Also in order to add [LSGAN](#lsgan) in mlpack label smoothing was required. It's implementation and testing is quite complete in [#1915][1915], however to make label smoothing work perfectly some commits from [serialization][1770] PR were required. So, it will get merged once [#1770][1770] gets merged.

#### Bias Visitor

In order to prevent normalizing the `Bias` parameter in [Weight Norm Layer](#weight-normalization-layer) a bias visitor was required to set the `bias parameters` of a layer. The first step was to add getter method `Bias()` in some layers. Afterwards these getter methods were used to set the weights. The visitor is merged with the help of [#1956][1956] PR.

#### Work Around to add more layers

The `Boost::variant` method is able to handle only 50 types. So inorder to add more layers to mlpack's ANN module a work around was required. After digging somewhat about the error online I found a work around. The `Boost::variant` method provides an implicit conversion which enables adding as many layers as we can with the help of tree like structure. The [#1978][1978] PR was one of the fastest to get merged. I just completed it in two days such that the Weight Norm layer gets merged.


#### Weight Normalization Layer

Weight Normalization is a technique similar to `Batch Normalization` which normalize the `weights` of a layer rather than the activation. In this layer only `Non-bias` weights are normalized. Due to normalization the gradients are projected away from the weight vector, thus testing the `gradients` got tedious. The layer is implemented as a wrapper around another layer in [#1920][1920].

#### Inception Layer

In order to complete my [Frechet Inception Distance](#frechet-inception-distance) PR GoogleNet was required. In order to do that `Inception Layer` is required. There are various versions of the `Inception Layer`. The first version of the layer is quite complete. However [#1950][1950] will be merged after implementing it's all three versions. The `Inception Layer` is basically just a `wrapper` around a `Concat` Layer.

#### Frechet Inception Distance

`Frechet Inception Distance` is used for testing the performance of the `GAN` model. It uses the concept of `Frechet Distance` which compares two `Gaussian` Distribution as well as the parameters of the `Inception` model. In order to get the parameters of Inception model [#1950][1950] will be required to merge first. The `Frechet Distance` is currently implemented in [#1939][1939] and it will be integrated with `Inception Model` once it is merged.


#### Fix failing radical test

While working on this PR I learned how important and tough testing is. The `RadicalMainTest` was failing about 20 times in 100000 iterations. After quite a lot of digging it was found that the reason was that random values were being used for testing. With this PR I learned about `Eigen Vectors`, `Whitening` of a matrix and many other important concepts. The [#1924][1924] PR provided a fix matrix for the test.


#### Serialization of glimpse, meanPooling and maxPooling layers

While working on [Gan Serialization](#improving-serialization-of-gans), I found that the `glimpse`, `meanPooling` and `maxPooling` are not serialized properly. I fixed the serialization in [#1905][1905] PR. Finding the error was one of the patience testing job but it felt quite satisfied after fixing it.

#### Generator Update of GANS.

While testing `GANs` I found one error in the update mechanism of it's `Generator`. The issue is being discussed with the mentors, however the error seems ambiguous. Hence, [#1933][1933] will get merged after arriving at the conclusion on the issue.

#### LSGAN

`Least Squares GAN` uses `Least Squares` error along with `smoothed labels` for training. It's implementation is quite complete and [#1972][1972] will get merged once LSGANs testing will get completed.  

# Pull Request Summary

#### Merged Pull Requests

* [Pull Request ensmallen/#109][109] - Providing option to calculate exact objective  
* [Pull Request #1905][1905] - Serialization of glimpse, meanPooling and maxPooling layer
* [Pull Request #1920][1920] - Weight Normalization Layer
* [Pull Request #1924][1924] - Fix failing radical test
* [Pull Request #1956][1956] - Bias Visitor
* [Pull Request #1978][1978] - Work Around to add more layers


#### Open Pull Requests

* [Pull Request #1770][1770] - Improving Serialization of GANs
* [Pull Request #1888][1888] - Dual Optimizer for GANs
* [Pull Request #1915][1915] - Label Smoothing in GANs
* [Pull Request #1933][1933] - Error in Generator Update of GANs
* [Pull Request #1939][1939] - Frechet Inception Distance
* [Pull Request #1950][1950] - Inception Layer
* [Pull Request #1972][1972] - LSGAN

# Future Work

* Completion of Open Pull Requests.
* Addition of Stacked-GAN in `mlpack`.
* Command Line Interface for training `GAN` models.
* Command Line Interface for testing `GAN` models.

# Conclusion

I learned quite a lot while working with mlpack till now. When I joined mlpack I was quite a beginner in `Machine Learning` and in the past months I have learned quite a lot. I also learned quite a lot how `Object Oriented Programming` helps in `Developing a big project`. Also my patience got tested while `debugging` the code I have written. Overall it was quite good learning and fun.

I will keep contributing and will ensure that all of my Open PR's get merged.

I would also like to thank my mentors `ShikharJ`, `zoq` and `rcurtin` for their constant support and guidance throughout the summer. I learned quite a lot of things from them. I would also like to thank Google to give me an opportunity to work with such highly experienced people.

[1770]: https://github.com/mlpack/mlpack/pull/1770
[109]: https://github.com/mlpack/ensmallen/pull/109
[1888]: https://github.com/mlpack/mlpack/pull/1888
[improved-gan]: https://arxiv.org/abs/1606.03498
[1915]: https://github.com/mlpack/mlpack/pull/1915
[1956]: https://github.com/mlpack/mlpack/pull/1956
[1978]: https://github.com/mlpack/mlpack/pull/1978
[1920]: https://github.com/mlpack/mlpack/pull/1920
[1905]: https://github.com/mlpack/mlpack/pull/1905
[1924]: https://github.com/mlpack/mlpack/pull/1924
[1950]: https://github.com/mlpack/mlpack/pull/1950
[1939]: https://github.com/mlpack/mlpack/pull/1939
[1972]: https://github.com/mlpack/mlpack/pull/1972
[1933]: https://github.com/mlpack/mlpack/pull/1933

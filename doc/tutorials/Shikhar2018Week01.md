@brief Implementing Essential Deep Learning Modules - Week 1
@author Shikhar Jaiswal
@page Shikhar2018Week01 Implementing Essential Deep Learning Modules - Week 1
@date 2018-05-20 13:15:00

@section Shikhar2018Week01 Implementing Essential Deep Learning Modules - Week 1

It has been a productive first week with `Mlpack`, on my project `Implementing Essential Deep Learning Modules`. The objective of the project is to implement the core infrastructure and API of some of the essential deep learning modules, primarily `Generative Adversarial Networks (GANs)` and `Restricted Boltzmann Machines (RBMs)`, over the summers and maybe beyond!

For the upcoming Phase I evaluations, I'd be working almost exclusively on `GAN`s, which are one of the most reverred ideas in the field of Deep Learning today.

This week, and during the Community Bonding period, I worked on introducing the support for `Transposed Convolution` and `Atrous Convolution` layers, effectively completing the convolutional toolbox of `Mlpack`, and the support for `Layer Normalization`. I also discovered a couple of bugs in the existing code-base for `Batch Normalization` and the `Naive Convolution` rule, both of which have now been fixed. The pull requests are now merged and we are ready to begin on more implementation-heavy tasks such as the `GAN` and `DCGAN` API.

I also opened an issue for the implementation of `.shed_rows()` and `.shed_cols()` routines for `arma::Cube`, which would help us in optimizing the calculation of gradients for `Atrous Convolutions`. This is not a priority task for now and hence, would be taken up later.

For the coming week, I'll be spending most of my time away debugging the errors in Kris' `GAN` implementation and hopefully, get it merged within the week itself.

Till Next Time Then!

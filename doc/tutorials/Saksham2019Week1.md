@brief Implementing Improved Training Techniques for GANs - Week 1
@author Saksham Bansal
@page Saksham2019Week1 Implementing Improved Training Techniques for GANs - Week 1
@date 2019-06-02 22:05:00

@section Saksham2019Week1 Implementing Improved Training Techniques for GANs - Week 1

The aim of my summer project with mlpack is to add new features and training techniques to the GAN framework so, that it is ready for release. More specificially, I will be working on adding improved training techniques for GANs such as `MinibatchDiscrimination` and `VirtualbatchNormalization`. I will also be implementing Conditional GANs and other regularization methods if time remains.

This week I was able to have my pending PRs for GANs merged. I started working on `MinibatchDiscrimination` which we have decided to implement as a layer in the mlpack API. The major difficulty in implementing a layer is always in deriving the gradient and implementing it successfully however after some debugging I was able to have the numerical graident test to pass. I believe the major coding part of the layer is complete and more tests and optimizations should follow in the next week.

I also worked on `Inception Score` function that we require to test the performance of the layer. Hopefully testing in the coming week won't be too troublesome and we would be able to merge both.

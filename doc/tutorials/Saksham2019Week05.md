@brief Implementing Improved Training Techniques for GANs - Week 5
@author Saksham Bansal
@page Saksham2019Week5 Implementing Improved Training Techniques for GANs - Week 5
@date 2019-07-08 03:05:00

@section Saksham2019Week5 Implementing Improved Training Techniques for GANs - Week 5

This blog post has been slightly delayed since the first evaluations were over. I am happy that I passed and I'll be continuing my work. Anyways I am back to work and since then completed the implementation of orthogonal regularization. I have also been making the changes to other open PRs namely `MinibatchDiscrimination` and `VirtualBatchNormalization`. I have started working on another technique for GANs called spectral normalization which has shown to provide superior results to simple weight normalization. However, to implement it successfully we require a `visitor` that can return the dimensions of the weights of a layer and also the bias term is not normalized. So, after that visitor is merged I will continue with the implementation of the layer.

In the meantime, I will be working on adding a `Padding` layer to `mlpack/ann` modules. Basically, the code that is used for padding is same in all the convolutional layers and so, it is best to abstract that inside a general `Padding` layer and reduce redundancy from the convolutional layers. Also, this would give me an opportunity to investigate the cause of failure for the gradient test of `AtrousConvolution` layer.

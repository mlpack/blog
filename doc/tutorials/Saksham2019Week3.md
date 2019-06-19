@brief Implementing Improved Training Techniques for GANs - Week 3
@author Saksham Bansal
@page Saksham2019Week3 Implementing Improved Training Techniques for GANs - Week 3
@date 2019-06-18 03:05:00

@section Saksham2019Week3 Implementing Improved Training Techniques for GANs - Week 3

This week I worked on finishing my implementation of `VirtualBatchNormalization`. The main difficulty was in writing the implementation of the `Backward` method. I was able to consult the implemnentation of the `BatchNorm` layer as a reference. I also looked at the implementations of the `VirtualBatchNormalization` layer in Tensorflow and Pytorch. The implementation of my `Gradient` method is correct as I verified through the numerical gradient test however the `Backward` method is still not working correctly. I hope to resolve this issue in the coming week. In the meantime I was able to find a bug in the implementation of the `BatchNorm` layer and fix it.

I also started working on regularizers and opened a PR. I have added support for L1 and L2 regularizers and hope to add support for orthogonal regularization in the coming week which should not take much time once the design is finalized.

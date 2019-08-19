@brief Implementing Improved Training Techniques for GANs - Week 11
@author Saksham Bansal
@page Saksham2019Week11 Implementing Improved Training Techniques for GANs - Week 11
@date 2019-08-19 03:05:00

@section Saksham2019Week11 Implementing Improved Training Techniques for GANs - Week 11

This week after Toshal’s PR on support for more than 50 layers was merged a lot of my work was ready to be merged. Specifically, the padding layer has now been completed and merged. Also the mini batch discrimination layer is complete and the build is finally passing so, we should be able to merge that soon as well!

Other than that I have continued my work with spectral norm layer. One difficultly with the implementation is that the the layer uses a power iteration method during the forward pass for computing the spectral norm of the weight matrix. I am not completely sure how we would compute the gradient for this approximation. I have been try to do the manual derivation for this but it is very tedious and I have not been successful with it so far. Hopefully, in the coming week I can get it to work. Otherwise I hope to continue the work post-GSoC.

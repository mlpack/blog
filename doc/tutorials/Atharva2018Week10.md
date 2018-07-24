@brief Variational Autoencoders - Week 10
@author Atharva Khandait
@page Atharva2018Week10 Variational Autoencoders - Week 10
@date 2018-07-24 19:00:00

@section Atharva2018Week10 Variational Autoencoders - Week 10

I implemented another definition of the `Forward()` function in the FFN class along with a test. This now makes it very easy to forward pass just through the encoder or the decoder of a saved model.

The convolutional model was not working with the `Sequential` object because in its `Forward()` function, `reset` was being hard set to `true`. Hence, it was setting the `inputWidth` and `inputHeight` of the `TransposedConvolutional` layer both to 0. I trained that convolutional model and observed the total loss go much below what it went with a dense layered model, as expected. Although, the KL divergence was heigher than dense layered model and as a result sampling from the prior didn't generate **defined** results.

To put this on the **models** repository, I had to work with some **CMake**. It was to learn some basics of **CMake** for this task.

I added `BernoulliDistribution` to ann dists. It will be needed for generating **binary** MNIST. I tried training a model and it did seem to work. I also added support for **beta** VAEs which was a very simple task.


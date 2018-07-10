@brief Variational Autoencoders - Week 8
@author Atharva Khandait
@page Atharva2018Week08 Variational Autoencoders - Week 8
@date 2018-07-10 09:00:00

@section Atharva2018Week08 Variational Autoencoders - Week 8

When using the `Sequential` object for the encoder and the decoder, it kept erroring out. I corrected the `Gradient` function of that object. Also, the encoder wasn't participating in the backward pass at all. It was because the `Backward()` helper function of FFN class does not go over the first layer of the network as it's not needed in most cases. So, Marcus suggested we use an `IdentityLayer` before the encoder. Another mistake which went unnoticed earlier was that in the `Loss()` function of the `Reparametrization` layer, the KL loss was being always added to the total loss, even when includeKl was false. I corrected that. To make keeping track of training progress easier, I overloaded the `Evaluate()` function of the FFN class. The new definiton takes input(`predictors`) and target(`responses`) and returns the loss with the current parameters. I think it would have taken a longer to debug this whithout Sumedh's help.

I trained a VAE model with fully connected layers on 90% of MNIST for about 5 hours. I expected it to at least generate some blurry but distinguishable digits. Sadly, on seeing the results, the images seemed to just have random noise. I am currently trying to figure out what's going wrong. Also, I am seeing some weird trends with the total loss while training.
@brief Variational Autoencoders - Week 7
@author Atharva Khandait
@page Atharva2018Week07 Variational Autoencoders - Week 7
@date 2018-07-02 20:00:00

@section Atharva2018Week07 Variational Autoencoders - Week 7

The jacobian test for the `NormalDistribution` class passes now. The problem was when we applied softplus, the approximate jacobian was still being calculated with respect to the standard deviation. Whereas, the `LogProbBackward()` was calculating it with respect to the pre standard deviation. I had to add some functions to be able to modify `preStdDev` from outside the class. It took a while to figure this out.

I created a VAE model in my local copy of the **models** repository. As discussed with Sumedh, I used `Sequential` layers for the encoder and the decoder. I tried training it on MNIST. But, the reconstruction loss isn't decreasing at all over iterations. I will discuss this with Sumedh tonight and try to figure out what's going wrong. For generation, I am currently writing functions in a different file which will sample from the distribution output by the decoder. Also, I was wondering if using log probability as the reconstruction loss is correct or should we use negative log probability.

I think we should be able to see some nice results in this week using fully connected layers first. After that is done, I will see what needs to be done to get the `Reparametrization` layer and the `ReconstructionLoss` to work with convolutional layers. As I have tried to make everything generic till now, I don't think that should be too much work.
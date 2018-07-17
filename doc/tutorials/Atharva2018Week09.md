@brief Variational Autoencoders - Week 9
@author Atharva Khandait
@page Atharva2018Week09 Variational Autoencoders - Week 9
@date 2018-07-10 09:00:00

@section Atharva2018Week09 Variational Autoencoders - Week 9

I was finally able to get some good results with the network. I used the `MeanSquaredError` for these results. Training with `ReconstructionLoss` generates barely recognizable digits. Sumedh and I were thinking that this might be due to some fundamental faults in the way we are modelling the distribution for the output.

I realized that I was using `ReLU` activation after the decoder and normalizing the data to (-1, 1). This was the reason that the reconstruction loss wasn't decreasing. After removing the activation, it trained well and here are some results.

Passing a random gaussian sample to the decoder:
<p>
<img src = "images/vae_random.jpg" width = "640" height = "35" hspace = "10"/>
</p>

Varying a latent variable of a gaussian sample continuosly:
<p>
<img src = "images/vae_latent_varying.jpg" width = "640" height = "35" hspace = "10"/>
</p>

To work with the decoder seperately from the network, I first thought about serializing `parameters` in the `Sequential` layer but later realized that it only acts as a container and the `parameters` member is empty. After discussing it with Marcus, I have decided to solve this by overloading the `Forward()` function of the FFN class. This new definition will take additional arguments, the starting and ending index of the layers to forward pass through.

I am currently debugging a VAE model using convolutional layers. Once done, I think it will give better results.
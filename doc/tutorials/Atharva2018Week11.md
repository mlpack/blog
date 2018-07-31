@brief Variational Autoencoders - Week 11
@author Atharva Khandait
@page Atharva2018Week11 Variational Autoencoders - Week 11
@date 2018-08-1 00:20:00

@section Atharva2018Week11 Variational Autoencoders - Week 11

I did some refactoring of the code in the PR for the **models** repository. I modified the generation scripts and played around with the learned distribution.

The following samples are the result of modifying each latent variable independently out of the 10.
<p>
<img src = "images/allLatent.jpg" width = "600" height = "335" hspace = "10"/>
</p>
As we can see, only the 3rd, 4th and 9th latent variable affect the generated data.

So, I took two of them, 3rd and 4th, and changed them in two dimensions. Here is how it looks.
<p>
<img src = "images/2dLatent.jpg" width = "600" height = "600" hspace = "10"/>
</p>
The digits which can't be seen here are the ones that are dependent on the 9th latent variable. I tried it. Collectively, these three latent variables can generate all of MNIST.

I also did some cherry-picking and split the huge ReconstructionLoss PR. The NormalDistribution PR will be kept open until we can prove that it works. The BernoulliDistribution PR has been reviewed and needs to be merged for all the PRs.

For CVAEs(Conditional Variational Autoencoders), we will need to use `Forward()`, `Backward()` and `Update()` instead of `Train()` function as we need to append the labels to the output of the `Reparametrization` layer midway during the forward pass.

I am now putting a convolutional VAE model to train on the CelebA dataset, I think it's on this dataset that experiments with beta-VAEs and CVAEs can be really interesting.

I had trained a model on binary MNIST as well, here are the results.
Sampling from the prior:
<p>
<img src = "images/priorBinary.jpg" width = "640" height = "35" hspace = "10"/>
</p>
Sampling from the posterior:
<p>
<img src = "images/posteriorBinary.jpg" width = "640" height = "35" hspace = "10"/>
</p>
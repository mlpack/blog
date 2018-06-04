@brief Variational Autoencoders - Week 2 + 3
@author Atharva Khandait
@page Atharva2018Week03 Variational Autoencoders - Week 2 + 3
@date 2018-06-04 18:00:00

@section Atharva2018Week03 Variational Autoencoders - Week 2 + 3

Having started coding a little later than planned, I have almost caught up with the planned timeline.

Implementation of the Sampling layer has been completed, modifications were made in the Softplus activation function to expand it's support to matrices and cubes. KL Divergence has been implemented inside the Sampling class. Sumedh and I thought about using the GaussianDistribution object for the above tasks but we need support for univariate gaussian distributions, so that has been kept on hold and everything has been implemented in the Sampling layer. We plan to talk to Ryan about implementing another normal distribution class for our purpose. I am currently testing the Sampling layer and plan to include the tests for KL Divergence along with it. I think I will need Sumedh's suggestions about how to test the Sampling layer well.

The next task for this week will be to start the implementation of the VAE class. I am quite excited about it.

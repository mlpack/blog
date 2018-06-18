@brief Variational Autoencoders - Week 5
@author Atharva Khandait
@page Atharva2018Week04 Variational Autoencoders - Week 5
@date 2018-06-18 23:00:00

@section Atharva2018Week04 Variational Autoencoders - Week 5

We have decided against implementing a VAE class. Instead we will try to extend the functionality of the current ANN and DIST architecture to make it more generic.

This week, I implemented a NormalDistribution class, different from the existing GaussianDistribution class. This one is for multiple univariate distributions as opposed to a single multivariate distribution of the older class. The reconstruction loss was implemented, which takes a dist object using templates, default being the NormalDistribution class.

I am debugging the gradient check of this loss function. I will update the tasks for this week tomorrow once I discuss it with Sumedh.
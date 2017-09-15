@brief Deep Learning Module in mlpack - Week 1
@author Krishnakant Singh
@page Kris2017WeekOne Deep Learning Module in mlpack - Week 1
@date 2014-06-07 12:20:00

@section Kris2017WeekOne Deep Learning Module in mlpack - Week 1

### Goal
This summer I will be working on implementing Deep
Learning Modules such as RBM, ssRBM and GAN's to
the mlpack library.

### Week1
This week I discussed at length the merits and de-merits of my proposed solution to vanilla/plain **RBM** architecture. In the proposed solution for the Gibbs sampling function. I had proposed a generic Gibbs sampler but I found the hard way that implementing such a generic Gibbs sampler(user defined probability functions with a variable number of parameter, any number of variables, arbitrary functions for calculating the parameters of the distributions) would not be worth time. Interestingly I did not find such a Gibbs sampler even with [STAN](https://github.com/stan-dev/stan) a very popular probabilistic programming framework in cpp.

**Mikhail** and I discussed several solutions that could be possible.
But we finally decided upon a layered architecture solution for RBM. This was majorly motivated with idea of code re-usability and the resulting modularity in the architecture eg for a vanilla RBM implementation would look like
Visible Layer <---> Linear Layer <---> Sigmoid Layer <---> Hidden Layer
The double arrows indicate bidirectional flow at every alternating epoch.

I have implemented a rough sketch of the solution
* [Rbm](https://gist.github.com/kris-singh/a5de37f17d68c9d11fbdb05bcb57dafc) partially(only training algorithm [cd-k]) is missing.
* We also created layers for the visible and hidden units for the RBM they have been implemented here [Layers](https://gist.github.com/kris-singh/8e65d23d91a2583679461c0c725f8df0). They would be very helpful when we begin the ssRBM as we would have to change the visible layer only(with other modification to RBM file of course)

I would also like to share with you some of approaches we tried for [generic](https://gist.github.com/kris-singh/20a234c5560b505e0e5b89904dd8a3d1) [gibbs](https://gist.github.com/kris-singh/935d5d46b78935cfafb81133c68acee6) [sampler](https://gist.github.com/kris-singh/cdd952a793b7b7dc932ddac83c579761) but the efforts went in vain. Most of the implementation of RBM's in [python](https://github.com/blaswan/rbm-mnist/blob/master/code/rbm.py) also do not use generic Gibbs sampler.
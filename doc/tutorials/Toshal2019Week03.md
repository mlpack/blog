@brief Implementing Essential Deep Learning Modules - Week 3
@author Toshal Agrawal
@page Toshal2019Week03 Implementing Essential Deep Learning Modules - Week 3
@date 2019-06-18 00:30:00

@section Toshal2019Week03 Implementing Essential Deep Learning Modules - Week 3

This week was quite productive from my previous week. I have completed the implemenation of `Weight Norm Layer` in this week. It was my first layer. I got quite familiar with the layer API. Also as weight norm will have a layer inside I was required to ensure that the proper calls to the wrapped layer are also made.

The main challenge during it's correct implemenation was in it's `gradient testing`. I was required to provide an `offset` to check the gradients,because the weights of the wrapped layer are intialized with respect to the `vector and scalar parameter` of the weight norm layer. Finding the need to do this was quite somewhat challenging as it got somewhat difficult to find the error. Also while testing it I also found lot of small syntactic mistakes in my implemenation.

I also worked on fixing the radical test. I wrote a small bash script for reproducing the error. While working on it, I also got to know what `Singular Value Decomposition` and `Whitening` is. `ICA` and `PCA` are quite interesting topics.

In the upcoming week I am going to implement `Frechet Inception Distance` for measuring the performance of GANs. It would be quite interesting thing to work on as it may involve working on Inception Model.

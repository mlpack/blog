@brief Deep Learning Module in mlpack - Week 11 + 12
@author Kris Singh
@page Kris2017WeekElevenTwelve Deep Learning Module in mlpack - Week 11 + 12
@date 2017-08-21 23:00:00

@section Kris2017WeekElevenTwelve Deep Learning Module in mlpack - Week 11 + 12

This week was mostly spent in writing test for the GAN PR and Fixing changes in the GAN PR.
We wanted to implement the [Orilley](https://www.oreilly.com/learning/generative-adversarial-networks-for-beginners) example. I faced a lot of problems implementing this example as valid convolution padding used in
the example leads to creation of very weird padding size which didn't make sense at the time. For taking care
of that problem I had to implement the resize layer which basically is a interpolation layer using bilinear
interpolation for scaling or de-scaling and image.

This week we also refactored the code using Lozhnikov's idea. Basically we want the predictors matrix to remain constant for the both the generator and discriminator network.

I also tried to get the 1d gaussian test and digits dataset to work this week. The parameter tuning for the digits is dataset pretty hard and we end up generating random noise most of time. We also added support for convents with gan's this week.
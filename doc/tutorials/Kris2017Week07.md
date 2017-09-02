@brief Deep Learning Module in mlpack - Week 7
@author Kris Singh
@page Kris2017WeekSeven Deep Learning Module in mlpack - Week 7
@date 2017-07-24 13:00:00

@section Kris2017WeekSeven Deep Learning Module in mlpack - Week 7

## Week Seven

This week i mostly tried completing ssRBM and GAN PR's.
Majority of the time was spend in making both the codes
work on the test dataset. We finally managed to do so.
With ssRBM Pr we were running into the errors of memory 
mangament due to me allocating around ~30gb of memory 
for the parameters. Since i was declaring all the parameters to 
be of full matricies. But i managed to reduce this to just vectors.
The problem left withh ssRBM still is the training part we 
getting a accuracy of around 12% for the mnist data set that we used
in the binary rbm. We are working on fixing the test.

This week i also managed to finish the GAN implmenetation the code
on work on the test data but is givin near random images even for 
say 1000 iterations of alternating sgd(with the discriminator being
trained for 3000(3 * 1000) iterations) and generator being trained 
for 1000 iterations(the generator and discriminator being used here
are just simple ffn). The GAN PR also requires review for me to fully
undertand where i am gouing wrong. I want to thank Konstantin here 
also since i was using the CrossEntropy Code that he wrote for the
GAN's. I am also not sure how to test GAN. Write now i am just trying
to see if it can generate real quality images.

Next Week:
I would mostly be working on fixing both the GAN' and ssRBM test.
Also i would write serialisation for GAN's next week. I hoping 
within 10 days both PR's would be mergable.
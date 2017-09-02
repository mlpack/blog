@brief We need to go deeper, Googlenet - Week 9
@author Nilay Jain
@page Nilay2016WeekNine We need to go deeper, Googlenet - Week 9
@date 2016-07-26 18:00:00

@section Nilay2016WeekNine We need to go deeper, Googlenet - Week 9

I started this week by first testing the inception layer. While writing tests I was not getting the expected outputs, so I checked the codes of ConvLayer and Pooling Layer which are called in the Inception Layer. I then corrected the code in pooling layer so that we can pool with stride correctly now. I added this feature last week only but was still not getting correct results, so I corrected the logic and tested it, and it works now. We have merged this feature.

Then I corrected small bugs in the logic of ConvLayer. The forward pass and the backward pass logic have been corrected now and give expected results, we still need to check the Gradient() function, which is my immediate task to resolve. I have written tests for the forward and backward passes of the ConvLayer and checked that they work with padding, and that they give the desired output using standard kernels.

I also wrote code for the ConcatLayer. I have completed the Forward and Backward function and checked them with tests to see that they work. This layer will give us the functionality to concatenate the outputs of two or more layers and then distribute the errors among the constituent layers for the backward pass. The Gradient() function still needs to be written, and I need to discuss what happens when we combine two or more base Layers in our ConcatLayer. Also I first need to write the test for Gradient() function of the ConvLayer then I can complete the Gradient tests for both the Inception Layer and the Concat Layer.

I think we made good progress this week, and the trivial implementation of the Inception Layer we have developed can be automated to subnet_layer. Along with this, I will discuss what other tasks need to be completed this week with my mentors and will update you about them in the next blog post. Stay tuned!
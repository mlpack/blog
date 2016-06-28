Title: We need to go deeper, Googlenet : Week-5 Highlights
Date: 2016-06-28 15:00:00
Tags: gsoc, edge_boxes, CNN, googlenet, deep learning
Author: Nilay Jain

I started this week by discussing "Going Deeper with Convolutions " paper with my mentor, to get an idea how to implement the inception layer. I also clarified some of the concepts regarding backprop, convolutions, and standard regularization techniques like dropout which are used in deep networks. I read the network in network paper to get an idea about 1 x 1 convolutions which was introduced here, and how smaller neural nets are used to build larger networks.

Then I fixed minor issues pointed out in the PR for feature extraction code in edge_boxes method. I tested the timings for performing convolution using armadillo submatrices, and using loops and pointers by invoking NaiveConvolution class. Armadillo submatrices gives a faster method but I think this might not work when we have to convolve with stride. If we can figure out how we can work that, performance may improve for the Convolution method. Then I improved the gradient function by calculating edges by applying convolution using sobel filter.

Then I looked at the ann implementation of mlpack. I looked at the convolution and pooling layers that will be used in implementing the inception layer, and had to read things for some of the functions implemented in these classes. It took me a bit of time to get accustomed to the style in which the ann method is implemented because of lot of templatization in code. I guess I still have many things to learn.  I also glanced at some other implementations of googlenet in other libraries without understanding many details of course, but getting a rough idea.

I have started the implementation of the inception layer and plan to finish it in the next days. After examining the convolution_network_test, it looks very easy to stack layers for the inception layer in a similar fashion. For improving discretize function we will use the fast PCA method which uses randomized SVD as suggested and explained by my mentor. Further, interface for googlenet will be discussed once inception layer is complete.

Title: We need to go deeper, Googlenet : Week-8 Highlights
Date: 2016-07-19 17:00:00
Tags: gsoc, CNN, googlenet, deep learning
Author: Nilay Jain

This week I finished the implementation of the Inception Layer and the test for it. The version we have finished right now is very simple and will serve as a guiding example to make subnet_layer which could take any collection of layers as input and allow the user to duplicate it over the network. I also started with the implementation of the concat_layer which will concatenate the output of one or more layers for the forward pass, and distribute error among the layers, for the backward pass. This coming week our plan is to merge the code for inception layer and complete the concat_layer and it's test.
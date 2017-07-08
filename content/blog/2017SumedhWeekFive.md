Title: Neural Turing Machines : Week 5
Date: 2017-06-06 14:00:00
Tags: gsoc
Author: Sumedh Ghaisas

No major contribution from me in this as I was mostly sick due to bad weather.
Fixed couple of bugs in GRU PR and wrote forward and gradients tests for it.
I am lacking benhind on NTM implementation which is the major part of my project
so I will be working on that before I complete the tests for Batch Normalization.
This will allow me to complete NTM on time and I can use the time while running
experiments on NTM to actually complete batch normalization. Cause running exeriments
on NTM is going to be a lengthy process. I have couple of weeks dedicated to that.

NTM will be implemented as a part of RNN framework. Extra layer of memory unit will
be added which will deal with memory operations. I am comcentrating on implementing
memory unit for now. I am almost done except for the part of implementing circular convolution.
I am not able to decide between implementations there. Hopefully I will figure that out soon.

**Title: Deep Learning Module in MLpack(Week 5)**
**Date: 2017-07-07 13:00:00**
Tags: neural networks, restricted Boltzmann machines
Author: Kris Singh

### Week Five
This week was primarily focused on reading and understanding the ssRBM paper. I also opened a new PR for ssRBM that basically implements the spike slab layer.
Our approach for implementation of ssRBM is that it will be a policy class of the RBM class. This would mean that we would have
very less code duplication and things we would actually need to implement for the ssRBM would be Gradients, Reset and the FreeEnergy function. I have already implemented these the only part remaining is refactoring of the RBM class.

The plan for the next week is basically to complete the ssRBM implementation and hopefully test the ssRBM implementation for classification on the mnist/cifar dataset. I don't exactly know how would we add these to the repo as cifar dataset is huge.


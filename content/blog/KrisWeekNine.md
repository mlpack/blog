Title: Deep Learning Module in MLpack(Week 9)
Date: 2017-08-3
Author: Kris Singh

### Week Nine
Most of the week was spent in just fixing both the ssRBM and GAN PR.
As the present situation stands ssRBM is achieving accuracy of 76% on the mnist dataset and around 79% on cifar10 dataset(500 images).I also made changes to the ssRBM PR so that now the input and output are now templated accepting any rather than just arma::mat. These accuracies are pretty good for cifar10 dataset but if still have to check for the whole dataset(10k) where the accuracy is ~68%
</br>

With the GAN PR I have modified the training algorithm now such that it only requires the use of only one Optimizer.optimize function call.
Right now i am stuck with the GAN PR as after the training the outputs are essentially random and I was not able to find any mistakes with the training procedure. Also, there is no easy way to test GAN so i am confused as for how to test the implementation out other than just visualizing the outputs.

### Next Week
The goal for the next week is to hopefully add some meaningful results from GAN PR. Also, I have started reading the stacked GAN paper it seems a bit of stretch if we would be able to implement it.
I am hoping if GAN PR is complete by next week I can move on to stacked GAN.

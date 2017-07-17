Title: Deep Learning Module in MLPack(Week 6)
Date: 2017-16-07 13:00:00
Tags: neural network, restricted Boltzmann machines, GAN
Author: Kris Singh

### Week Six
This week the majority of time went in refactoring of the code of existing RBM and writing code for ssRBM. I have succesfully been able to refactor the code and make all the test's pass for Binary RBM(serialisation test and classification test). The code for ssRBM is also now complete. I primarily aim to test the ssRBM implementation this week though i am not sure about how what test. Basically the classification test given in the ssRBM paper requires that we
use the Cifar-10 dataset which is around 178Mb so i think that test is not good to commit but can be tested. Mikhail gave a idea to test the existing classification test with Mnist. Though i don't have any idea which values to start with. 

This week I also implemented the GAN. Though there are some issues that we have to work with. Testing GAN would be easy if we don't run into any issues with training of GAN's which is a known issue.

This week I planning to get the test for ssRBM right and opening a PR for GAN.
P.S: Sorry for the Late blog post

@brief Implementing Essential Deep Learning Modules - Week 4
@author Shikhar Jaiswal
@page Shikhar2018Week04 Implementing Essential Deep Learning Modules - Week 4
@date 2018-06-11 11:09:00

@section Shikhar2018Week04 Implementing Essential Deep Learning Modules - Week 4

We have finally wrapped up with Phase I and along with it, a number of key goals.

The `GAN` code is finally merged, and the `DCGAN` code has been debugged for the `MNIST` dataset. Now the only thing remaining to be done is to debug the test for the `CelebA` dataset, and the PR can be merged thereafter. Also, then we can upload the code to the models repository, though for now all the code is hosted within mlpack itself, as this is a secondary goal.

This week we got some promising results with the `GAN` code on the 10,000 image subset and the full 70,000 image set of `MNIST` for you to feast your eyes on:

`10,000 Images`
<p>
<img src = "images/mnist_gan_10_epoch.png" width = "600" height = "600" hspace = "10"/>
</p>

`70,000 Images`
<p>
<img src = "images/mnist_gan_full_dataset.png" width = "600" height = "600" hspace = "10"/>
</p>

For the next week, we will be focussing on implementing the support for batch sizes and optimizer separation for `GANs`.

`Vale!`

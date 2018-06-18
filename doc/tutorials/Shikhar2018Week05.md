@brief Implementing Essential Deep Learning Modules - Week 5
@author Shikhar Jaiswal
@page Shikhar2018Week05 Implementing Essential Deep Learning Modules - Week 5
@date 2018-06-18 02:27:00

@section Shikhar2018Week05 Implementing Essential Deep Learning Modules - Week 5

Phase I evaluations came in and I'm glad that Marcus is happy with what we have been able to achieve.

The `DCGAN` code is now completely functional, and has been debugged for the `CelebA` dataset as well. However, I have been unable to prepare the dataset for `CelebA` in our preferable format, because it is memory intensive, and always crashes my system.

This week we got some promising results with the `DCGAN` code as well on the 10,000 image subset and the full 70,000 image set of `MNIST`:

`10,000 Images`
<p>
<img src = "images/mnist_dcgan_20_epoch.png" width = "640" height = "480" hspace = "10"/>
</p>

`70,000 Images`
<p>
<img src = "images/mnist_dcgan_full_dataset.png" width = "640" height = "480" hspace = "10"/>
</p>

After discussing with Marcus, we decided to merge the `DCGAN` code in its present state, which would be done shortly. Also, this week I implemented the support for mini-batches in the convolutional layers, and the `GAN` implementation. The PR is also completely debugged and ready to get merged. I really couldn't thank Marcus enough for his instant reviews and debugging help.

The only thing remaining to be done now for optimization of our code is the implementation of the `GANOptimizer` class, which would allow us to separate our optimizers for the `generator` and the `discriminator`. Also, this week, I'll start working on the `Wasserstein GAN` implementation. We are right on track to wrap up all of the planned work for the summer by the end of Phase II, after which, I can take up the work pertaining to the additional goals planned.

`Adéu!`

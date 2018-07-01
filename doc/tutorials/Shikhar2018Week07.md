@brief Implementing Essential Deep Learning Modules - Week 7
@author Shikhar Jaiswal
@page Shikhar2018Week07 Implementing Essential Deep Learning Modules - Week 7
@date 2018-07-02 00:09:00

@section Shikhar2018Week07 Implementing Essential Deep Learning Modules - Week 7

We have formally entered a streak of productive weeks! The `WGAN` PR is now complete and under review, and should be ready to merge anytime next week. We have totally refactored the `GAN` module according to `SFINAE` + `enable_if<>` paradigm, allowing us to choose the variant of `GAN` at compile time.

With the above changes, we have further reduced the training time to under ~7 hours with all the variants! We tested our implementations, again on the full `70,000` image `MNIST` dataset, and obtained the following results:

`Standard GAN`
<p>
<img src = "images/output_gan.png" width = "640" height = "480" hspace = "10"/>
</p>

`DCGAN`
<p>
<img src = "images/output_dcgan.png" width = "640" height = "480" hspace = "10"/>
</p>

`WGAN`
<p>
<img src = "images/output_wgan.png" width = "640" height = "480" hspace = "10"/>
</p>

`WGAN-GP`
<p>
<img src = "images/output_wgangp.png" width = "640" height = "480" hspace = "10"/>
</p>

We're still planning out the optimal startegy for implementing `DualOptimizer` class. Thankfully, Marcus has offered his help (as always) regarding the same. We have also planned to complete the `RBM` and `Spike and Slab RBM` work left over from Kris' `GSoC` last year. We have been very fortunate to cover a lot up until now, and probably we can cover a lot more this month as well.

`Pozdrav`

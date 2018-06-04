@brief Implementing Essential Deep Learning Modules - Week 3
@author Shikhar Jaiswal
@page Shikhar2018Week03 Implementing Essential Deep Learning Modules - Week 3
@date 2018-06-04 12:09:00

@section Shikhar2018Week03 Implementing Essential Deep Learning Modules - Week 3

We're into the final week of Phase I and, thanks to Marcus' suggestions and reviews, right on track! A number of key decisions were taken up by us this week.

The `GAN` code is finally ready to get merged, and the `DCGAN` code has been pushed, which should be ready to get merged by the end of this week. As discussed with Marcus, the `DCGAN` code uses the same class as the standard `GAN`, which allows us the freedom to just implement the test cases, as the required layers are already available in `mlpack`.

This week we got some good results with the `GAN` code on a 500-image subset of `MNIST` dataset, and I'm currently in process of running the code on the full 70,000-image `MNIST` dataset, which would be posted in the PR itself. Also, we decided to not run the test on `Travis`, and instead, push the code to the `mlpack/models` repository, whch would be done soon.

Also, we decided to try out optimizer separation and implementing batch support for the `GAN` implementation after Phase I, which would allow us flexibility to compare and contrast our single optimizer output as well, and provide full user flexibility to try out different variants of the `GAN` infrastructure.

That's all for now! See you next week!

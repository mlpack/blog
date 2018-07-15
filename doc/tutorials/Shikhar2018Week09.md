@brief Implementing Essential Deep Learning Modules - Week 9
@author Shikhar Jaiswal
@page Shikhar2018Week09 Implementing Essential Deep Learning Modules - Week 9
@date 2018-07-15 16:40:00

@section Shikhar2018Week09 Implementing Essential Deep Learning Modules - Week 9

Building up on our work from the last week on optimizing our `ANN` framework, we went forward with implementing `EvaluateWithGradient()` function for the `FFN` and `RNN` classes as well.

Though we had done the same with the aim of reducing code duplication in mind initially, we realized that with the above function implemented, we were able to obtain atleast a `30%` speedup in the case of simple `FFN` networks!

For the case of `RNN` class, the speedup was slightly lower at `22%` ~ `25%`, primarily because of the heavier gradient computation routines being used. Nevertheless, we also applied the above function inside our `GAN::EvaluateWithGradient()` function, so a certain amount of speedup is expected there as well!

I also received my Phase II evaluations this week, and I'm glad that Marcus is satisfied with the effort that we have put in. I will continue to build up on my work on `RBM`s and hopefully, we can merge them as well before this month ends.

`Mirupafshim`

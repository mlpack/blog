@brief Implementing Essential Deep Learning Modules - Week 7
@author Toshal Agrawal
@page Toshal2019Week07 Implementing Essential Deep Learning Modules - Week 7
@date 2019-07-16 12:35:00

@section Toshal2019Week07 Implementing Essential Deep Learning Modules - Week 7

In this week I have completed implementing `Inception Layer(v1)`. I am thinking to add version wise implementation. Also I am somewhat confused about the auxillary classifier in the implementation. But I will look for it's implementation somewhere else soon.

The failing radical test issue is also fixed. It took quite a lot of patience while finding out the error. The error which came out over there was just because of floating point exception. The reason for memory error is still quite unknown.

I also kept track of the test I am running on my `Dual Optimizer`. It's taking quite a lot of time. Hopefully it finishes soon.

I have also started working on implementing `visitor` which will return the weight of the non-bias term. It may get somewhat complicated. But yes it's on it's way. The challenge over here is for the layers which have `Model()` parameters. I may need to `add a getter` for getting non-bias weights. I am quite unsure about it, so I think I will need to discuss it soon.

In this week I am thinking to completely implement my `Inception Layer` PR and the `visitor's`.

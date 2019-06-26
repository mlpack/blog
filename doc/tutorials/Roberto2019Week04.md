@brief Implementing probabilistic KDE error bounds - Week 4
@author Roberto Hueso
@page roberto-2019-week-04 Implementing probabilistic KDE error bounds - Week 4
@date 2019-06-25 18:00:00

@section roberto-2019-week-04 Implementing probabilistic KDE error bounds - Week 4

This week probabilistic KDE API has been integrated into the existing codebase
and many unit tests have been implemented. All tests seem to indicate that this
implementation is working well. After a review by Ryan, there are a few things
to improve a bit but for the most part it should be ready.

Another possibility for further improvement is to reclaim unused error tolerance
as explained in [this paper](https://arxiv.org/pdf/1206.6857.pdf). I am working
on this for this week as well.

It was interesting to learn some tips on how to test pieces of code that depend
on random parameters.

![Random number XKCD](https://imgs.xkcd.com/comics/random_number.png)

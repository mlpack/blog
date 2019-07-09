@brief Implementing probabilistic KDE error bounds - Week 5
@author Roberto Hueso
@page roberto-2019-week-05 Implementing probabilistic KDE error bounds - Week 5
@date 2019-07-03 18:00:00

@section roberto-2019-week-05 Implementing probabilistic KDE error bounds - Week 5

This week has been mostly about reclaiming not used probability. Probability reclaim
has been implemented for both single and dual trees.

The idea is this: Whenever a KDE's ruleset evaluates kernel on two different points
by any means that are not Monte Carlo estimation, there's some amount of probability
that it's not being used. If we could use that amount of probability for making future
Monte Carlo estimation less strict, then the original total amount of probability
would still be the same and a higher amount of point's KDE can be estimated by using
Monte Carlo, which reduces computation time.

Results might depend very much on the selected parameters but, for all tests I did,
I got an increase on the amount of points estimated by Monte Carlo.

All code needs to be reviewed but in the meantime I'll be working on subspace trees.

![Don't throw away stuff XKCD](https://imgs.xkcd.com/comics/still_in_use.png )

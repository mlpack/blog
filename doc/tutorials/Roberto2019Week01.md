@brief Implementing probabilistic KDE error bounds - Week 1
@author Roberto Hueso
@page roberto-2019-week-01 Implementing probabilistic KDE error bounds - Week 1
@date 2019-06-03 18:00:00

@section roberto-2019-week-01 Implementing probabilistic KDE error bounds - Week 1

### Current state of KDE in mlpack

The current [KDE](https://en.wikipedia.org/wiki/Kernel_density_estimation)
codebase takes advantage of one property: Many kernel functions decrease their
value the further away two points are.
If it's affodable to have an approximation, then it's possible to avoid many
calculations by relaxing the problem (i.e. setting an absolute or relative
error bound).

### Let's relax even more

It's summertime so let's take those error bounds on vacation so they can relax :)

By setting a probabilistic relative error bound, researchers in
[this paper](http://papers.nips.cc/paper/3539-fast-high-dimensional-kernel-summations-using-the-monte-carlo-multipole-method.pdf)
made the error bound more flexible (e.g. the KDE, with a 95% probability,
will differ as much as 5% from the real value).

During the week I have been working on implementing this into the existing mlpack
codebase. So far, the implementation for single trees is almost ready, but I haven't
been able to figure out some issues yet. At the moment approximations get really
close to the real value, but still not close enough.

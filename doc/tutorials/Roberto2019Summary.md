@brief Advanced Kernel Density Estimation Improvements - Summary
@author Roberto Hueso
@page Roberto2019Summary Advanced Kernel Density Estimation Improvements - Summary
@date 2019-08-26 06:00:00

@section Roberto2019Summary Advanced Kernel Density Estimation Improvements - Summary

# Abstract

`Kernel Density Estimation` (KDE) is a, widely used, non-parametric technique to estimate a probability density function. `mlpack` already had an implementation of this technique and the goal of this project is to improve the existing codebase, making it faster and more flexible.

These improvements include:

* Improvements to the `KDE` space-partitioning trees algorithm.
* Cases in which data dimensionality is high and distance computations are expensive.

# Implementation

We can summarize the work in 3 PRs:

### Implement probabilistic KDE error bounds

[Pull request #1934][1934].

Up to this moment, it was possible to set an exact amount of absolute/relative error tolerance for each query point in the `KDE` module. The algorithm would then try to accelerate as much as possible the computations making use of the error tolerance and space-partitioning trees.

Sometimes an exact error tolerance is not needed and it would mean a lot for flexibility to be able to select a `fuzzy` error tolerance. The idea here is to select an amount of error tolerance that would have a certain probability of being accomplished (e.g. with a 95% probability, each query point will differ as much as 5% from the exact real value). This idea comes from [this paper][dongryeol].

This is accomplished by probabilistically pruning tree branches. This probability is handled in a smart way so that when an exact prune is made or some points are exhaustively evaluated, the amount of probability that was not used is not lost, but rather reclaimed and used in later stages of the algorithm.

Other improvements and fixes were made in this PR:

* Statistics building order was fixed for cover and rectangular trees.
* Scoring function evaluation was fixed for octrees and binary trees.
* Simplification of metrics code.
* Assignment operator was added for some trees ([issue #1957][1957]).

### Subspace tree

[Pull request #1962][1962].

The dominant cost in `KDE` is metrics evaluation (i.e. distance between two points) and usually not all of these dimensions are very relevant. The idea here is to use `Principal component analysis` (PCA), as a dimensionality reduction technique, to take points to a lower dimensional subspace where distance computations are computationally cheaper (this is done in [this paper][dongryeol]). At the same time the idea is to preserve the error tolerance, so that it is easy to know the amount of maximum error each estimation will have.

This is done by calculating a `PCA` base for each leaf-node and then [merging those bases][merge] as we climb to higher nodes.

This PR is still a **work in progress**.

### Reclaim unused KDE error tolerance

[Pull request #1984][1984].

[This paper][reclaim] mentions the idea of reclaiming not used error tolerance when doing exact pruning. The idea is that, when a set of points are exhaustively evaluated, the error of these computations is zero, so there is an amount of error tolerance for pruning that has not been used and it could be used in later stages of the algorithm. This provides the algorithm with the capability of adjusting as much as possible to the error tolerance and pruning more nodes.

Thanks to `Ryan`'s derivations, we also realized that the bounds of the previous algorithm were quite loose, so a lot of error tolerance was being wasted. This has been reimplemented and will probably represent a huge source of speedup.

# Future work

There are some ideas that we did not have time to finish but are quite interesting:

* Finish subspace tree PR.
* In the proposal there was the idea of implementing [ASKIT][ASKIT] and this is really interesting for me.

# Conclusion

This has been an awesome summer. I had the opportunity to contribute to a meaningful project and will continue to do so in the future, since there are many ideas that came while I was working on this or did not have time to finish. It has been a very enriching experience for me, I learned lot, it was a ton of fun and, definitely, debugging skills got sharpened.

I would like to thank the whole mlpack community as well as Google for this opportunity. A special mention has to be made for my mentor `rcurtin`, without his help when I was stuck and his new ideas I would not have enjoyed this as much, so thank you.

For people reading this and thinking about applying for GSoC in the future: Apply now, it will be fun and you will learn a lot from highly skilled people.

[1934]: https://github.com/mlpack/mlpack/pull/1934
[1962]: https://github.com/mlpack/mlpack/pull/1962
[1984]: https://github.com/mlpack/mlpack/pull/1984
[dongryeol]: http://papers.nips.cc/paper/3539-fast-high-dimensional-kernel-summations-using-the-monte-carlo-multipole-method.pdf
[merge]: https://www.researchgate.net/publication/3193153_Merging_and_splitting_eigenspace_models
[reclaim]: https://arxiv.org/abs/1206.6857
[1957]: https://github.com/mlpack/mlpack/issues/1957
[ASKIT]: https://arxiv.org/abs/1410.0260

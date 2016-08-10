Title: Approximate Nearest Neighbor Search - Week 11
Date: 2016-08-10 09:00:00
Tags: gsoc, knn, spill-tree
Author: Marcos Pividori

Last week, I have implemented generalized Spill Trees, to consider general splitting hyperplanes, not necessarily axis-orthogonal.

I added a new template parameter for Spill Trees: `HyperplaneType`, and I implemented two candidate classes: `AxisOrthogonalHyperplane` and `Hyperplane`.

(+) `AxisOrthogonalHyperplane`: consider an axis-parallel projection vector. So, we can project any vector in O(1) time, considering the appropiate dimension.

(+) `Hyperplane` consider a general projection vector. So we can project any vector in O(d) time, through a dot product.

Inside Spill Tree, I consider `BallBound` for non-axis-orthogonal hyperplanes, and `HrectBound` for axis-orthogonal hyperplanes.

Considering this abstraction, I managed to significantly simplify the Split methods: `MeanSplit` and `MidpointSplit`. Now, they share most of the code.

By default, `SpillSearch` considers `AxisOrthogonalHyperplanes` because they seem to be faster in many cases, but this is not always true. We have to benchmark both methods and see which is faster and which is more accurate, I mean, which has the best relation between running time and relative approximation error.

All of this changes were included in the pull request: [[1]](https://github.com/mlpack/mlpack/pull/747).

I plan to work next days in these topics:

+) Add many test cases for all the code developed: `SpillTree` class, `SpillSearch` class, `Hyperplane` class, etc.

+) AppVeyor has shown some problems with the MSVC compiler, in the resolution of template parameters of alias templates, similar to an old issue: [2]. I have to fix it, probably including some extra definitions.

+) Check details in the Spill Tree's implementation.

Follow the progress in: [[2]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).

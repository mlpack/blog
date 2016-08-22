Title: Implementation of tree types : Summary
Date: 2016-08-23 02:00:00
Tags: gsoc, space trees
Author: Mikhail Lozhnikov

In this blog post I'll try to describe consisely the work that I have done for the mlpack project this summer.

### Summary

Here's a list of my Pull Requests. All these PRs are merged except [Pull Request 746] [746] (Universal B tree implementation, the code is under review now. The tree works correctly, maybe it requires a number of small fixes, I believe the PR will be merged soon).

 * Hilbert R tree: [664] [664]
 * R+ and R++ trees implementation: [699] [699]
 * Vantage point tree: [708] [708]
 * Removed RectangleTree::Points(): [709] [709]
 * Hilbert R tree fixes: [710] [710]
 * RectangleTree::NumDescendants() optimization and some RectangleTree fixes: [711] [711]
 * Replaced SortStruct by std::pair: [721] [721]
 * Fixed a segfault in RPlusTreeSplit. Fixed traits for the R+/R++ tree: [724] [724]
 * Random projection trees: [726] [726]
 * Fixed an error in MidpointSplit that may lead to a segfault: [741] [741]
 * Universal B tree implementation: [746] [746]
 * Vantage point tree and HRectBound improvements: [760] [760]
 * Fixed copy constructor of RectangleTree and added move constructor: [767] [767]

### Hilbert R tree

I began my work with the Hilbert R tree. The tree is implemented according to the [Hilbert R-tree: An Improved R-tree Using Fractals] [hilbert-r-tree-paper] paper on the basis of the `RectangleTree` class.

The Hilbert R tree differs from original Guttman's R trees by the split and the insertion methods. All points are being inserted into the Hilbert R tree according to their position on the Hilbert curve (the Hilbert value).

The Hilbert curve is a variant of space-filling Peano curves. The algorithm that translates a point to the Hilbert value is based on the following paper [Programming the Hilbert curve] [hilbert-curve-paper]. The paper sugests an algorithm that allows to calculate the Hilbert value by means of bit operations whereas previous attempts construct the curve using recursion. The method is implemented in `DiscreteHilbertValue` class. I tried a different approach that compares the Hilbert order of two points by means of recursion but the algorithm was much slower than the method suggested in the paper.

The changes are contained in [Pull Request #664] [664] and [Pull Request #710] [710].

### R+/R++ tree

I continued my project with the R+ tree which is based on the paper [The R+-tree: A dynamic index for multi-dimensional objects] [r-plus-tree-paper]. The main advantage of the tree is the property that children do not overlap each other.

When I had implemented the tree I found an error in the insertion algorithm. The paper does not discuss the method in detail. It is not difficult to think out a case when we can not insert a point and preserve the property of non-overlapping children. Another problem is that the tree does not guarantee that the number of child nodes after the split algorithm is less than the maximum allowed number. The issues appear to be well known problems. I looked through a series of articles and came across the paper [R++ tree: an efficient spatial access method for highly redundant point data] [r-plus-plus-tree-paper] that describes a variant of the R+ tree tat takes into account the maximum bounding rectangle and avoids the issues. So, I added a workaround that solves the R+ tree problems by increasing the maximum size of the node and I implemented the R++ tree.

The implementation of the R+ tree and the R++ tree can be found in [Pull Request 699] [699] and [Pull Request 724] [724].

### Vantage point tree

The vantage point tree is implemented on the basis of the paper [Data Structures and Algorithms for Nearest Neighbor Search in General Metric Spaces] [vp-tree-paper]. The implementation appears to be much slower than the implementation of the k-d tree. The main disadvantage is that the bound of a node is too complex and attempts to calculate the distance between a point and a vp-tree node precisely require a lot of computations. The first version of the vantage point tree contains a point in each intermediate node. Then Ryan suggested to move vantage points to separate nodes in order to simplify tree traversal rules. Then I tried to implement a variant of the vantage point tree that contains points only in leaf nodes. That variant appears to be faster then the previous variants.

Moreover, I tried a number of different bounds. Right now, the tree uses the bound which consists of two non-concentric balls, the outer ball is the minimum bounding ball and the inner one is centered at the vantage point.

The changes can be found in [Pull Request 708] [708] and [Pull Request 760] [760]. Moreover, I implemented a variant of the vantage point tree that uses the hollow-rect bound which consists of the minimum bounding rectangle and a number of rectangular hollows. I didn't issue a PR since the implementation is slower than the implementation of the vantage point tree (I pushed the code [here] [hrect-vp-tree]).

### Random projection tree

The implementation of random projection trees are based on the paper [Random projection trees and low dimensional manifolds] [random-projection-tree-paper].

I implemented two versions of the split method: the mean split and the max split. Both methods are described in the paper. Unfortunately, the tree performs much slower than the k-d tree since the bound of the random projection tree is a polytope. There are a number of methods that calculates the distance between a point and a polytope but they are based on the gradient descent method and require a lot of computations.

The tree is implemented on the basis of the `BinarySpaceTree` class. The changes can be found in [Pull Request 726] [726].

### Universal B tree

I think the universal B tree is the most complicated algorithm that I have implemented this summer. The implementation is based on the paper [The Universal B-Tree for Multidimensional indexing: General Concepts] [ub-tree-paper].

The universal B tree is a variant of the B tree. Like the Hilbert R tree, the UB tree maps multidimensional space to a linear ordered space. All points are being inserted into the tree according to that ordering. Notably, this mapping preserves the multidimensional clustering.

The bound of the UB tree is a stairway-shaped figure in multidimensional space. Thus, the bound consists of a number of non-overlapping hyper-rectangles. Of course, the tree allows to use non-overlapping bounds but that leads to a huge number of computations.

The changes can be found in [Pull Request 746] [746]. The PR is not merged yet, but I believe it will be merged soon.

### Other changes

I made a number of changes that are not connected directly with my project, I'll briefly describe them here. I've removed extensions of the TreeType API in the `RectangleTree` class. The changes can be found in [Pull Request 709] [709]. [Pull Request 711] [711] contains optimizations that allow to find descendant points by a logarithmic time. [Pull Request 721] [721] solves [Issue 712] [712]. [Pull Request 741] [741] solves a problem which has appeared after refactoring. And [Pull Request 767] [767] adds the copy-constructor and the move constructor to the `RectangleTree` class.

### TODOs

Right now, some tree types like the vantage point tree and random projection trees use looser-bounds. That leads to a huge number of base cases in dual-tree algorithms. I think these bounds may be even more optimized but I don't know how.

Another problem is concerned with [Rank-Approximate Nearest Neighbor Search] [rann-paper]. The algorithm often fails with some tree types (e.g. the Hilbert R tree). It is an interesting problem to understand why that happens.

### Acknowledgement

That was an amazing summer, thanks to the mlpack team and especially to Ryan Curtin who looked through the code and has suggested a lot of advices on the optimization of the algorithms and to Marcos Pividori who has proposed a series of ideas on the optimization of the `RectangleTree` class (such as [Pull Request 711] [711] and [Pull Request 767] [767]).

[664]: https://github.com/mlpack/mlpack/pull/664
[699]: https://github.com/mlpack/mlpack/pull/699
[708]: https://github.com/mlpack/mlpack/pull/708
[709]: https://github.com/mlpack/mlpack/pull/709
[710]: https://github.com/mlpack/mlpack/pull/710
[711]: https://github.com/mlpack/mlpack/pull/711
[721]: https://github.com/mlpack/mlpack/pull/721
[724]: https://github.com/mlpack/mlpack/pull/724
[726]: https://github.com/mlpack/mlpack/pull/726
[741]: https://github.com/mlpack/mlpack/pull/741
[746]: https://github.com/mlpack/mlpack/pull/746
[760]: https://github.com/mlpack/mlpack/pull/760
[767]: https://github.com/mlpack/mlpack/pull/767
[712]: https://github.com/mlpack/mlpack/issues/712
[hrect-vp-tree]: https://github.com/lozhnikov/mlpack/tree/hollowhrectbound
[hilbert-r-tree-paper]: http://www.cs.uml.edu/~cchen/580-S06/reading/KF94.pdf
[hilbert-curve-paper]: http://scitation.aip.org/content/aip/proceeding/aipcp/10.1063/1.1751381
[r-plus-tree-paper]: http://www.vldb.org/conf/1987/P507.PDF
[r-plus-plus-tree-paper]: http://ics.upjs.sk/~sumak/files/2013_ADBIS_RPP-tree_full.pdf
[vp-tree-paper]: http://web.cs.iastate.edu/~honavar/nndatastructures.pdf
[random-projection-tree-paper]: http://cseweb.ucsd.edu/~dasgupta/papers/rptree-stoc.pdf
[ub-tree-paper]: http://link.springer.com/chapter/10.1007/3-540-63343-X_48
[rann-paper]: http://www.mlpack.org/papers/rann.pdf

Title: Approximate Nearest Neighbor Search - Week 10
Date: 2016-08-03 09:00:00
Tags: gsoc, knn, spill-tree
Author: Marcos Pividori

Last week, I have implemented Spill trees with axis-orthogonal splitting hyperplanes [[1]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).

I created a new class `SpillSearch` that provides an interface similar to `NeighborSearch` but with an extension to properly set the tau parameter. It encapsulates an instance of `NeighborSearch`.

Also, I have implemented a new version of `NeighborSearchRules` specialized for Spill Trees, because I needed to modify the methods:
 + `Score()` to consider splitting hyperplanes when calculating the score for overlapping nodes.
 + `CalculateBounds()` to ignore $B_2$ bound (we can not use $B_2$ bound for Spill Trees).

## Single Tree Search:

The `SingleTreeTraverser` is similar to the implementation for `BinarySpaceTree`.
The difference is in the implementation of `NeighborSearchRules` for SpillTrees.
When calculating the score of a query point and a reference node I consider 2 cases:
  + If the reference node is non-overlapping, I calculate the score the same than before.
  + If the reference node is overlapping, I analyze the reference node's half space. If it contains the given query point, I return 0 (best score). Else, I return DBL_MAX (prune). As we consider axis-orthogonal splitting hyperplanes, we can decide which child node to traverse in O(1), analising the appropiate dimension.

## Dual Tree Search:

The Query tree is built without overlapping.

When calculating the score of a query node and a reference node, I consider 2 cases:
  + If the reference node is a non-overlapping node, I calculate the score the same as before.
  + If the reference node is a overlapping node, I analyze query node's bounding box. If it intersects the reference node's half space, I return 0 (best score). Else, I return DBL_MAX (prune). As the reference spill tree is built with axis-orthogonal hyperplanes and the query tree considers hrect bounds, we can make this decision in O(1) time.

The `DualTreeTraverser` is slightly different to the implementation for `BinarySpaceTree`. When referenceNode is a overlapping node and we can't decide which child node to traverse, this means that queryNode is at both sides of the splitting hyperplane, we analyse the queryNode:
 + If queryNode is a non-leaf node, I recurse down the query node.
 + If queryNode is a leaf node, I do single tree search for each point in the query node.

The `DualTreeTraverser` is faster than the `SingleTreeTraverser`, specially when the value of tau increases.

The extension was incorporated to existing *mlpack_knn*. With actual implementation, we can use *"-t spill"* to consider spill trees and *"--tau 0.1"* to set different values for the overlapping size (default value is tau=0).

I have made a pull request with this implementation in: [[2]](https://github.com/mlpack/mlpack/pull/747).

I plan to work next days in these topics:
 + Implement another version of SpillTrees to consider general hyperplanes (not necessarily axis-orthogonal), using `BallBound` instead of `HrectBound`, and holding a projection vector in each node.
 + Add a command line flag *"--get_real_error"* to compare the approximate neighbor search against the naive method and print the real relative error, so we can test with differents values of tau and see the difference.

Follow the progress in: [[1]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).

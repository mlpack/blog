Title: Approximate Nearest Neighbor Search - Week 9
Date: 2016-07-27 01:00:00
Tags: gsoc, knn, kfn, spill-tree
Author: Marcos Pividori

Last week, I have been improving NeighborSearchRules and considering differents approaches for the implementation of Hybrid Spill Trees [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf).

# Spill Trees's decision boundary:

The initial implementation of Spill Trees, was based on BinarySpaceTrees's code [[2]](http://github.com/mlpack/mlpack/tree/master/src/mlpack/core/tree/binary_space_tree).
In mlpack, KDTrees are built using the midpoint split but, when calculating the score and deciding how to traverse the tree, instead of the distance to the hyperplane determined by the midpoint split, the distance to the hrect bound is considered because it provides a tighter bound.
So, I decided to take the same approach for spill trees: build the tree splitting the points with a midpoint split, and consider the bounds when calculating the score and traversing the tree.
But this implementation is different to the approach mentioned in Ting Liu’s paper [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf), where it is supposed that you consider the same hyperplane when splitting the list of points and when deciding which node to visit in a dfs search.
So, the difference is that, we consider a midpoint split hyperplane when building the tree, but we consider a different decision boundary when traversing the tree (the decision boundary is defined by the set of points with the same distance to the left child’s bound and the right child’s bound).
After analysing this difference, I realized that it could make a difference in the overlapping of nodes.
We have been discussing about the advantages and disadvantages of these approaches in [[issues/728]](http://github.com/mlpack/mlpack/issues/728) and
[[spilltrees.pdf]](http://github.com/mlpack/mlpack/files/372825/spilltrees.pdf).
Finally, we decided to implement a similar approach to the one mentioned in Ting Liu's paper, considering midpoint cutting hyperplanes when calculating the score, the same hyperplanes that are considered when building the tree.

# Heaps for the list of candidates:

I realized in many parts of the code, we keep track of the best k candidates visited. In this situation, it is not necessary to keep a sorted list of the k elements. We only need to know the value of the worst candidate, so we can compare it with new elements and know if we must insert them to this list.
So, instead of maintaining a sorted list, a better approach is to use a priority queue.
I have been working on this improvement in: [[pull/732]](http://github.com/mlpack/mlpack/pull/732)

Next week, I will work in the implementation of Dual Tree Search for Spill Trees. Follow the progress in: [[3]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).

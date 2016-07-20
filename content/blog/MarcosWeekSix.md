Title: Approximate Nearest Neighbor Search - Week 6
Date: 2016-07-04 21:00:00
Tags: gsoc, knn, kfn, spill-tree
Author: Marcos Pividori

Last week, I have been working on the implementation of Spill Trees, as defined in: "An Investigation of Practial Approximate Nearest Neighbor Algorithms" [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf).

Spill tree is a variant of binary space trees in which the children of a node can "spill over" each other, and contain shared datapoints.

Two new separating planes LP and RP are defined, both of which are parallel to the original decision boundary, at a distance $\tau$ from it.
The region between LP and RP is called "overlapping buffer", and determines the points that are shared by the children nodes.

One problem with Spill Trees is that their depth varies considerably depending on the overlapping size $\tau$. For that reason, we are implementing Hybrid Spill Trees [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf), which provide better guarantees.

For each node, we first split the points considering the overlapping buffer.
If either of its children contains more than $\rho$ fraction of the total points we undo the overlapping splitting. Instead a conventional partition is used.
In this way, we can ensure that each split reduces the number of points of a node by at least a constant factor, resulting in logarithmic depth of the tree.

The implementation of spill trees is similar to the implementation of Binary Space Trees. However, we need to manage the list of points differently. We are going to have overlapping nodes, so we can not use range of indexes of the main dataset's matrix as we do with binary trees.
Therefore, actual implementation includes a general dataset instance (as we do with binary trees), and leaf nodes hold a vector of indexes pointing to columns of that matrix. Follow the progress in: [[2]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).

Next week, I will continue working in the implementation of Spill Trees and the Defeatist Seach for approximate neighbor search.

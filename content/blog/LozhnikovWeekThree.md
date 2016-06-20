Title: Implementation of tree types : Week 3
Date: 2016-06-13 10:30:00
Tags: gsoc, space trees, dual-tree algorithms, single-tree algorithms
Author: Mikhail Lozhnikov

As I had planned in the previous post I modified base cases and pruning rules for the neighbor search method, the range search algorithm and the k rank-approximate-nearest-neighbors search method.

In order to do that I had to modify the RectangleTree traversal algorithms. Since the methods described above represent results as a vector of the indices of points in the dataset I had to implement an approach for calculating the index for any particular point in the tree.

Also I started working on the implementation of the R+ tree.

P.S. Unfortunately, we decided that these modifications make base cases and pruning rules too complicated. So, these changes have to be removed. But as for me it was interesting to explore this as a possibility.

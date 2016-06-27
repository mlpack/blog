Title: Implementation of tree types : Week 5
Date: 2016-06-27 18:30:00
Tags: gsoc, space trees, R+ tree, R++ tree, Vantage point tree
Author: Mikhail Lozhnikov

As I had planned in the previous post I did the refactoring of the R+/R++ tree. I added a template parameter SweepType to the RPlusTreeSplit class and implemented a sweep method that tries to partition an intermediate node with the minimum number of splits. All sweep techniques are designed in  tree-independent manner. In order to do that I introduced a template parameter SplitPolicy. This parameter helps to determine the subtree in which we should insert any particular child of an intermediate node that is being split. Also I fixed some errors.

Moreover, I began the vantage point tree implementation. Right now the split method (VantagePointSplit class) is implemented. I have to implement a piecewise ball boundary type since the BallBound is not suitable for the vantage point tree. Also I did not think about vantage point tree-specific tests.

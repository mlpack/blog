Title: Implementation of tree types : Week 7
Date: 2016-07-12 12:00:00
Tags: gsoc, space trees, Vantage point tree
Author: Mikhail Lozhnikov

Last week, I have been working on the implementation of `HollowBallBound`. This class represents the area included between two concentric ball bounds. The radius of the inner ball may be equal to 0.

The `HollowBallBound` class is intended to replace the original piece-wise ball bound of the vantage point tree. This bound allows to calculate the minimum distance to a point much faster than the original bound. One of the disadvantages is the loss the crucial property of the binary space tree: the use of `HollowBallBound` may lead to overlapping children.

Since the vantage point tree is slightly different from the binary space tree, namely each intermediate node contains a point, I had to move the vantage point tree to a separate class. Unfortunately, that led to the duplication of the code.

Moreover, I added some tests for the vantage point tree.

@brief Implementation of tree types - Week 8
@author Mikhail Lozhnikov
@page Lozhnikov2016WeekEight Implementation of tree types - Week 8
@date 2016-07-18 23:00:00

@section Lozhnikov2016WeekEight Implementation of tree types - Week 8

Last week I continued working on the vantage point tree. Since the first point of each left subtree of the vantage point tree is the centroid of its bound and the right subtree does not contain the centroid at all, I added a new method (`IsFirstPointCentroid()`) to the TreeType API. This check should allow dual and single tree algorithms to use some optimizations.

Moreover, I implemented two types of the random projection tree: `RPTreeMax` and `RPTreeMean` (these tree types are based on `BinarySpaceTree`). Right now, these tree types use `HRectBound`, I implemented only the split algorithm.

The `RPTreeMax` split divides a node by a random hyperplane. The position of the hyperplane may differ from the median by a random deviation. The `RPTreeMean` split divides a node by a random hyperplane if the diameter is less or equal to the average distance between points multiplied by a constant.

My implementation is sligthly different from the original algorithms. I use a fixed number of random dataset points in order to calculate the median and the average distance between points. And since the algorithm that the paper introduces in order to find the deviation from the median is weird (one of two resulting nodes may be empty), I shrank the bounds of this deviation.
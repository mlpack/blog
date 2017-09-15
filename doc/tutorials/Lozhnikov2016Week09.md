@brief Implementation of tree types - Week 9
@author Mikhail Lozhnikov
@page Lozhnikov2016WeekNine Implementation of tree types - Week 9
@date 2016-07-27 00:30:00

@section Lozhnikov2016WeekNine Implementation of tree types - Week 9

Last week I have been working on the vantage point tree and the universal B-tree.

### Vantage point tree
I tried various fixes of the vantage point tree. Namely, I moved vantage points to separate nodes. That should considerably simplify pruning rules (we needn't implement the score algorithm for a query node and a reference point). Thus, each intermediate node of the vantage point tree contains three children. The first child contains only the vantage point. In such a way, the first point of the first sibling of a node is the centroid of the node.

This property allows to use some optimizations in dual-tree algorithms and I added this check to `NeighborSearchRules` and `RangeSearchRules`. There are still some errors, some base cases are duplicated.

### Universal B-tree
The UB-tree is a variant of the B-tree. It introduces an ordering in multidimensional space i.e. the space is mapped to a linear ordered space. Notably, this mapping preserves the multidimensional clustering. Thus, all points are inserted into the UB-tree according to this ordering. I implemented the split algorithm. Right now, I am working on the implementation of the UB-tree bound. This bound is slightly more complicated than `HRectBound` since it consists of a number of hyperrectangles. In contrast to `VantagaPointTree`, this bound preserves a crutial property of `BinarySpaceTree`. Namely, UB-tree's children do not overlap each other.
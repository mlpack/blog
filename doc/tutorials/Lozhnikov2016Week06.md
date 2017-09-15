@brief Implementation of tree types - Week 6
@author Mikhail Lozhnikov
@page Lozhnikov2016WeekSix Implementation of tree types - Week 6
@date 2016-07-04 22:00:00

@section Lozhnikov2016WeekSix Implementation of tree types - Week 6

Last week I had been working on some fixes of the `RectangleTree` class, including the removal of `RectangleTree::Points()`, the removal of `RectangleTree::Children()` and the optimization of `RectangleTree::NumDescendants()`.

The removal of the `Children()` method requires to make `SplitType`, `AuxiliaryInformationType` and `DescentType` friends of the `RectangleTree` class. The optimization of `NumDescendants()` method allows `Descendant()` to take $O(\log N)$ operations instead of $O(N)$.

Moreover, I finished the R+/R++ tree implementation. Namely, I replaced `SortStruct` by `std::pair` in `MinimalCoverageSweep` and `MinimalSplitsNumberSweep`, I simplified the code of `MinimalCoverageSweep` and I fixed the error with addition of a huge amount of equal points.

Unfortunately, I failed in the implementation of the `PiecewiseBallBund` class since I am not able to think out any cost-efficient method of finding the distance between a point and a piece-wise ball bound. The problem is not easy even in 2 dimensions.
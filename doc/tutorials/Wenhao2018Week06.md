@brief Alternatives to Neighborhood-Based CF - Week 6
@author Wenhao Huang
@page Wenhao2018Week06 Alternatives to Neighborhood-Based CF - Week 6
@date 2018-06-24 21:00:00

@section Wenhao2018Week06 Alternatives to Neighborhood-Based CF - Week 6

This week's work can be dividied into two parts. First, for weights interpolation, I finished some loose ends of that PR and made the improvements as pointed out by Mikhail's review comments. Also, as suggested by Ryan, I am also working on templatizing `NeighborSearchPolicy` so that a user can choose `kNN` or `LSH` (and maybe other methods as well) as the neighbor search algorithm. The second part is about implementing `BiasSVD` and `SVD++`. One issue is that the current CF framework cannot be used directly to implement the new models. After discussing with Mikhail, we have decided to refactor `DecompisitionPolicy` classes. The refactoring work includes adding a new function in `DecompositionPolicy` like `GetRating(user, item, ...)` to compute rating using the algorithm of that decomposition policy, moving model parameters (`W`, `H`, ...) to `DecompositionPolicy` class, etc. In this way, we only need to add two new decompisition policies for `BiasSVD` and `SVD++`. It also facilitates future work if new models are to be added. Refactoring the `DecompositionPolicy`, adding policies for `BiasSVD` and `SVD++` will be my focus for the next two weeks.

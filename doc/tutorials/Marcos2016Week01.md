@brief Approximate Nearest Neighbor Search - Week 1
@author Marcos Pividori
@page Marcos2016WeekOne Approximate Nearest Neighbor Search - Week 1
@date 2016-05-29 21:00:00

@section Marcos2016WeekOne Approximate Nearest Neighbor Search - Week 1

I am working this summer on the implementation of approximate nearest neighbor search.

First, we want to update the existing dual tree algorithm to do approximate nearest neighbor search, modifying the prune rule to include an epsilon, as mentioned at the end of the paper [[1]](http://www.ratml.org/pub/pdf/2015faster.pdf).

After reading the paper: "Tree-Independent Dual-Tree Algorithms" [[2]](http://www.ratml.org/pub/pdf/2013tree.pdf) in detail, I found some issues in the definition of the B2 bound. We were discussing about it in [[3]](http://github.com/mlpack/mlpack/issues/642) and, after thinking about the different special cases, we found some examples where actual definition could fail. We seem to have a solution. New week, I will work in updating existing code to fix this and compare the performance after this modification.

When reviewing the implementation of tree types, I found a subtle mistake! Ball trees were using hyper rectangle bounds instead of ball bounds! [[4]](http://github.com/mlpack/mlpack/pull/646) It was fixed and is waiting to be merged.

Next week, I plan to continue improving the neighbor search code, to fix the issue related to the bounds. Once this is working properly, I could add the modification to do approximate search and do some tests.
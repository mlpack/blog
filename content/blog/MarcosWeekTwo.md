Title: Approximate Nearest Neighbor Search - Week 2
Date: 2016-05-05 21:00:00
Tags: gsoc, knn, kfn
Author: Marcos Pividori

Last week we finished the discussion about neighbor search's bounds [1](http://github.com/mlpack/mlpack/issues/642).  I updated existing code to consider slighty different bounds. Then, I compared the performance, using the benchmarking system with a modification to measure the number of base cases for ALLKNN/ALLKFN. Results shown exactly the same num of base cases for many datasets, so we decided to go ahead and merge it.

Then, I continued working in existing neighbor search code, updating the dual tree algorithm to do approximate nearest neighbor search. I modified the prune rule to include a relative error, as mentioned at the end of the paper [2](http://www.ratml.org/pub/pdf/2015faster.pdf), with a general implementation that works for both kfn and knn [3](http://github.com/MarcosPividori/mlpack/tree/approx-knn).

As we are doing approximate search, we can prune more than when an exact solution is required. For example, for knn, we consider the prune rule:

```latex
prune if $d_min(N_q, N_r) > ( 1 / (1 + \epsilon ) ) * B_1(N_q)$.
```

Next week, I plan to continue working in the implementation of aprox knn, adding many test cases. Once everything is ready, I will merge it into the main repository.

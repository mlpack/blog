@brief Approximate Nearest Neighbor Search - Week 7
@author Marcos Pividori
@page Marcos2016WeekSeven Approximate Nearest Neighbor Search - Week 7
@date 2016-07-13 21:00:00

@section Marcos2016WeekSeven Approximate Nearest Neighbor Search - Week 7

Last week, I have completed the implementation of Hybrid Spill Trees [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf).

It is possible to configure both parameters: the overlapping size ($\tau$) and the balance threshold ($\rho$), as I mentioned in last blog post.

Also, I have included a Single Tree Traverser to perform Hybrid SP-Tree Search [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf).

Generally, neighbor search algorithms spend a large fraction of time backtracking to prove a candidate point is the true nearest neighbor.
A different approach is to descend the metric tree without backtracking, and then output the point in the first leaf node visited as the nearest neighbor  of the query point. This is called "defeatist seach" on a metric-tree.
The problem with this approach is very low accuracy, specially when the query point is close to the decision boundary.
However, Spill trees are especially appropriate for defeatist search. By including a overlapping buffer, we can increase the accuracy.

As mentioned in last blog post, Hybrid Spill trees have both overlapping and non-overlapping nodes. If we combine defeatist search with the previous approach, we have a Hybrid SP-Tree Search: "we only do defeatist search on overlapping nodes, for non-overlapping nodes, we still do backtracking using Neighbor Search Rules to decide when pruning".

We can control the hybrid by varying $\tau$. If $\tau$ is zero, we have a pure spill tree with defeatist search, very efficient but not accurate enough. If $\tau$ is a very large number, then every node is a non-overlapping node and we get back to the traditional metric tree, with prunning rules, perfectly accurate but not very efficient. By setting different values for $\tau$, we have a trade-off between efficiency and accuracy.

Next week, I will continue improving the implementation of Spill Trees and the Defeatist Seach and write some tests. Also, I have to continue thinking about possible alternatives to implement Hybrid SP-Tree Search as a dual tree algorithm. Follow the progress in: [[2]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).
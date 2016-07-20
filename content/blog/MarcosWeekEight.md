Title: Approximate Nearest Neighbor Search - Week 8
Date: 2016-07-19 21:00:00
Tags: gsoc, knn, kfn, spill-tree
Author: Marcos Pividori

Last week, I have considered different modifications to the implementation of Hybrid Spill Trees [[1]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf).

I have summarized what I have implemented in a pdf file: [[spilltrees.pdf]](https://github.com/mlpack/mlpack/files/372825/spilltrees.pdf)

## Tau parameter:

I was wondering why don't consider a percentage instead of a fixed value for tau. I mean, considering a percentage of the range of values in the dimension considered, so the overlapping buffer could change according to the width of the range of values in each split.

I looked for other implementations of spill trees and I found that both approaches are considered.

So, I decided to read more documentation on spill trees. I have read Ting Liu's thesis [[2]](http://www.cs.cmu.edu/~tingliu/thesis/tingliu_thesis.pdf). She doesn't provide a strong justification but, when analysing the appropiate value for tau parameter, it is mentioned:

*"Eq. (5.9) also implies that tau only depends on R_s and d, so it should be a fixed value for a given data set, the idea of changing tau for each partition does not work very well for this reason."*

So, according to what was proposed there, I decided to continue considering a fixed value for tau.

## Knn search:

As we don't know how many nodes will be pruned by the defeatist search, we can not be sure that we will have considered at least k points after traversing the tree. Maybe, we have visited less than k points by the end of the search, so we don't have enough points. This happens because with defeatist search we don't do backtracking. We can be sure we will visit at least 1 point, because all leaves contain at least one point.

So, I decided to modify actual implementation to guarantee that we always return k neighbors, no matter which tau parameter is used. This is achieved by doing backtracking, even on overlapping nodes, until we have k candidates.
Because we do backtracking in some overlapping nodes, I had to modify the implementation to avoid repeated candidates when analysing the same point twice.

However, we have not decided yet if we will include this modification.


Also, I added many test cases for the structure of spill trees and knn search with them.

Next week, I will continue considering different options to improve the implementation of Spill Trees. Follow the progress in: [[2]](https://github.com/MarcosPividori/mlpack/tree/spill-trees/src/mlpack/core/tree/spill_tree).

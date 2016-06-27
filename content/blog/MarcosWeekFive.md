Title: Approximate Nearest Neighbor Search - Week 5
Date: 2016-06-27 21:00:00
Tags: gsoc, knn, kfn
Author: Marcos Pividori

Last week, I have been working on the benchmarking system [[1]](https://github.com/zoq/benchmarks/pull/17).
After considering different options, I created a new view to plot the progress of a specific metric for different values of a method parameter. For example, for knn, it is possible to analyze the number of base cases and runtime for different values of approximation error (epsilon), with different libraries/configurations.

I executed some tests for: mlpack_knn with cover trees and kdtrees, and other libraries like [ANN](https://www.cs.umd.edu/~mount/ANN/) and
[FLANN](http://www.cs.ubc.ca/research/flann/). Results are available on: [[2]](http://marcospividori.github.io/mlpack-app/) ("Metric analysis with multiple parameters for an algorithm/dataset combination.")

We plan to benchmark approximate neighbor search with bigger datasets, using Jenkins's servers.

Next week, I will continue working in the implementation of Spill Trees [[3]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf). I will consider different approaches to include this extension and analyse the possibility of implementing Hybrid SP-Tree Search as a dual tree algorithm.

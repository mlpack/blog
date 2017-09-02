Title: Cross-Validation and Hyper-Parameter Tuning: Week 5
Date: 2017-07-03 14:45:00
Tags: gsoc
Author: Kirill Mishchenko

During the fifth week I was primarily working on a cross-validation
infrastructure and the simple cross-validation strategy. The main part of the
work has been done, and now it is in the review stage
([#1044](https://github.com/mlpack/mlpack/pull/1044)).

The next task is to implement k-fold cross-validation strategy. Luckily, almost
all secondary stuff is implemented, and coding can be focused on the strategy
itself. The main challenge here is to avoid creating multiple copies of data
while preparing different subsets.

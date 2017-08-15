Title: Cross-Validation and Hyper-Parameter Tuning: Week 11
Date: 2017-08-15 09:00:00
Tags: gsoc
Author: Kirill Mishchenko

Last week I was primarilly finishing working on k-fold cross-validation and the
main part of the hyper-parameter tuning module. Sending a PR for k-fold
cross-validation to the main repository was delayed since there was [a
bug](https://github.com/mlpack/mlpack/issues/1086) in the linear regression copy
constructor which caused failing for one of k-fold cross-validation tests. Now
it is [fixed](https://github.com/mlpack/mlpack/pull/1089), and a PR for k-fold
cross-validation is [sent](https://github.com/mlpack/mlpack/pull/1095).

As I have already mentioned, I was also finishing working on the main part of
[the hyper-parameter tuning module](https://github.com/micyril/mlpack/pull/2).
Mainly it concerns using a new interface for mlpack optimizers that is about
accepting a DatasetMapper parameter describing data type and possible values (if
it is of categorical type) for each dimension (that corresponds to a
hyper-parameter in the case of hyper-parameter optimization).

The remaining time of GSoC I'm going to work on supporting gradient decent for
hyper-parameter tuning, as well as to write a final report.

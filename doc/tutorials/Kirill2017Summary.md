@brief Cross-Validation and Hyper-Parameter Tuning - Summary
@author Kirill Mishchenko
@page cross-validation-and-hyper-parameter-tuning-summary Cross-Validation and Hyper-Parameter Tuning - Summary
@date 2017-08-20 10:00:00

@section cross-validation-and-hyper-parameter-tuning-summary Cross-Validation and Hyper-Parameter Tuning - Summary

My GSoC project can be summarized in the following PRs.

* [#1016 Add accuracy and mean squared error](https://github.com/mlpack/mlpack/pull/1016)

* [#1020 Add a method form detection tool](https://github.com/mlpack/mlpack/pull/1020)

* [#1031 Add a meta information extractor](https://github.com/mlpack/mlpack/pull/1031)

* [#1044 Add simple cross-validation](https://github.com/mlpack/mlpack/pull/1044)

* [#1074 Add precision, recall and F1](https://github.com/mlpack/mlpack/pull/1074)

* [#1095 Add k-fold cross-validation](https://github.com/mlpack/mlpack/pull/1095)

* [#1101 Add a hyper-parameter tuning module](https://github.com/mlpack/mlpack/pull/1101)

# Cross-validation module

During the summer I have implemented two `cross-validation strategies`. The first
one is simple: it splits data into two sets - training and validation sets -
and then runs training on the training set and evaluates performance on the
validation set. The second cross-validation strategy is `k-fold cross-validation`.

The cross-validation module has the following features.

1. Data preparation happens only once when a cross-validation object is
constructed.

2. In many cases you don't need to be explicit about data of what types you
are going to pass: the developed meta-programming tools are used to deduce
types for storing data. It also allows you to pass objects that can be
converted to the target types (e.g. objects of types that used by
[armadillo](http://arma.sourceforge.net/) to store intermediate results).

3. The interface is designed in the way that you first pass common (among
machine learning algorithms implemented in `mlpack`) constructor parameters
including data, number of classes, and information about dimensions
(datasetInfo). During this step your compiler will check whether the specified
machine learning algorithm accepts these parameters. If some check fails, a
human-readable message will be printed.

# Hyper-parameter tuning module

Another part of my GSoC project is a `hyper-parameter tuning module`. It lets
you optimize hyper-parameters using one of the cross-validation strategies in
couple with one of the metrics as objective.

The implemented module has the following features.

1. It has the same interface for constructors as in the cross-validation
module, and all features mentioned for the `cross-validation module` about
construction are applied here too.

2. What strategy to use during optimization is specified by a user. By now
support for two strategies has been implemented. With the first strategy,
`GridSearch`, users specify a set of values for each hyper-parameter they want
to optimize. The second strategy, `GradientDescent`, uses numerically
calculated gradients of functions based on cross-validation to optimize
real-valued hyper-parameters.

3. If some hyper-parameter should not be optimized, it can be marked with the
Fixed function.

# Metrics

I have implemented different metrics that can be used for cross-validation and
hyper-parameter tuning. These include accuracy, mean squared error, precision,
recall, and F1.

# Acknowledgment

I thank Ryan Curtin for his mentorship during the summer and for his passion to
provide deep and thoughtful responses to my works. I also want to thank Marcus
Edel for his reviews and for being responsive to my general questions about
`mlpack`.
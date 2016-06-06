Title: Dataset and Experimentation Tools : Week-2 Highlights
Date: 2016-06-05 21:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

Here are some things I've done in week 2.

* fixed [default output problem](https://github.com/mlpack/mlpack/issues/667) with [this pull request](https://github.com/mlpack/mlpack/pull/680).
Previously when output parameters are not specified the user, the program saved the results in a file with arbitrary name. This might delete user's data without warning.
I changed the default outputs to required parameters.
In some cases where output is not necessary, the program now gives warning to the user that it is not going to save the result if it is not specified, not save or overwrite existing data with default name.

* implemented [binarize](https://github.com/mlpack/mlpack/pull/666) functions, which transforms matrix values to 0 and 1 according to a given threshold.
This can provide a easy-to-use implementation for pre-processing dataset. Previously the user had to learn how to work with armadillo matrix.
Plus, it provides an overload which can apply binarize to selected dimensions.

* I experimented with the proof-of-concept I've done last week.
I thought of a way to change missing variables to NaNs while mapping the categorical (including missingi) data
and apply various imputation strategies by reverse-mapping the values,
but after a few discussion, it seems that implementing this while loading seems to be a better idea since it can allow users to specify which values are invalid or missing.

* Wrote a [How to install mlpack on Windows 10 Tutorial](http://keon.io/mlpack-on-windows.html)

* I discussed and implemented basic one-hot-encoding and min-max-scale functions.
These preprocessing features can be used in other methods or projects.

Next week, I am going to (really) finalize missing variables and imputation features, one-hot-encoding, and min-max-scale.
Along the way, I also hope to solve [this issue](https://github.com/mlpack/mlpack/issues/671), which I got unsuccessful this week because of segmentation faults errors.

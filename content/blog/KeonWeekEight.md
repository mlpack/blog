Title: Dataset and Experimentation Tools : Week-8 Highlights
Date: 2016-07-20 16:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

This week, I:

DatasetMapper & Imputer

1) Optimized Imputer a little bit. The details are discussed in the pull request [#694](https://github.com/mlpack/mlpack/pull/694).

2) Debugged and polished some comments.

Descriptive Statistics

1) Made statistics.hpp and statistics_impl.hpp, which is basically a more convinient version of armadillo statistics functions.
It also has more features like calculating skewness and kurtosis.
They are made to provide convinience, so the computational efficiency is little hurt.
I made the results to sync with the results given by the excel.
The commits I've done are in [describe branch](https://github.com/keonkim/mlpack/commits/describe)

2) The first version of the statistics class calculated every statistics at its constructor.
The benchmark scores are recorded [here](https://github.com/keonkim/mlpack/commit/2a89412fe6375178f2657bc48c3d698430419da0#commitcomment-18315506).

3) Changed iomanip to boost::format for formatting the output.

I've been studying little more about how ANN and RNNs are implemented in mlpack (just personal interest).
Deep learning is more fun than I thought, hopefully I can contribute to neural net parts of the mlpack in the future. 

Later, I will work a little more on statistics module, mainly to optimize a little more and polish the comments and outputs.

And, I will work on mlpack_preprocess_verify executable, which is just a small extension of Imputer module.
In this program, it does not change or replace any values, but only detects the invalid values.

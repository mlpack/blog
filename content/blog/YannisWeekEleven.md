Title: Modeling LSH - Implementation Week 3
Date: 2016-08-09 20:20:20
Tags: gsoc, lsh, modeling
Author: Yannis Mentekidis

The past week, I continued the implementation of the LSH model, the skeleton of which I outlined in my previous blog post.

The `LSHModel::Train()` method, that uses the dataset to learn some useful parameters is complete, so the `LSHModel::Predict()` remains for the proposed algorithm to be complete.

While implementing `LSHModel::Predict()`, I realized some of the GammaDistribution class features which I mentioned are [missing](https://github.com/mlpack/mlpack/issues/733) will actually be needed by the LSHModel. As a result of this realization, I went back and filled in the missing parts as well as the corresponding correctness tests. There is one more correctness test to implement, and then the GammaDistribution class will be complete and [issuue 733](https://github.com/mlpack/mlpack/issues/733) will be closed.

This week, I plan to fill out the remaining parts of the LSHModel and GammaDistribution classes, and leave the last week for testing, optimization, and final changes.
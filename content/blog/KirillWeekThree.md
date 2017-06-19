Title: Cross-Validation and Hyper-Parameter Tuning: Week 3
Date: 2017-06-12 11:00:00
Tags: gsoc
Author: Kirill Mishchenko

During the third week I was working on meta tools that for a given machine
learning algorithm allow to extract meta information about it, e.g. predictions
type, whether it takes a `data::DatasetInfo` parameter along with data and
whether it supports weighted learning
([#1031](https://github.com/mlpack/mlpack/pull/1031)).

Now the developed tools can facilitate implementation of various cross
validation strategies. I will start with a simple one - splitting data into
training and validation sets in according with a given proportion.

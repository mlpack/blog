Title: Cross-Validation and Hyper-Parameter Tuning: Community Bonding Period and Week 1
Date: 2017-06-05 09:00:00
Tags: gsoc
Author: Kirill Mishchenko

Before coding officially began I had done some preparatory work. Specifically, I
had changed the interface for passing responses in LinearRegression and LARS
([#1002](https://github.com/mlpack/mlpack/pull/1002)). Now LinearRegression and
LARS accept column-major responses as all other classification and regression
algorithms in mlpack. The mentioned pull request also separates interfaces for
weighted and non-weighted learning in LinearRegression, which will be handy for
supporting LinearRegression in cross-validation and hyper-parameter tuning
modules.

During the first week I implemented the accuracy and MSE metrics for
cross-validation ([#1016](https://github.com/mlpack/mlpack/pull/1016)). Now I'm
going to start working on cross-validation implementation that simply splits
data into training and validation sets in according with a given proportion. In
order to prevent users from passing redundant information about a machine
learning algorithm (like whether it is a regression algorithm or a
classification algorithm, or whether it supports weighted learning) and to
extract this information automatically from the machine learning algorithm type,
firstly I'm going to implement meta-programming tools that allow to extract such
information.

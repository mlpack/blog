Title: Dataset and Experimentation Tools : Week-3 Highlights
Date: 2016-06-20 24:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

This week, I worked on restructuring imputer and imputation methods.
Here are briefs of what I did.

1) tests for imputer and imputation methods.

2) Restructured imputer and imputation classes.
In this new implementation, imputer works like a wrapper that 
provides a convinient interface of the imputation classes.
Imputation classes can also be used independently if a user wants to replace
a number variable to another. This work took longer than I thought.

I did not make pull requests for standardization and normalization classes yet, 
since they are also structured as the imputer class.
I will be able to make similar changes after getting comments for the imputer class, 
and make the pull request accordingly. (This should be quick)

I also droped one-hot-encoding class that I was working on 
because I did not see the clear use of this in other methods in mlpack.

todo list:

1) apply changes to imputer, imputer classes, and scalers after getting comments

2) make a overload of data::Load function so that it maps using different policy for missing variables.

3) optimize using openmp

4) start working on preprocess_scan, a cli executable which scans through the dataset and finds
missing variables or abrupt gaps.


Notice: I already talked about this before to my mentors, but I have mandatory military training in June 21, 22, and 23.

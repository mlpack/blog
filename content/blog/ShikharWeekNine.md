Title: Profiling for parallelization and parallel stochastic optimization methods - Week 9
Date: 2017-08-02 03:50
Tags: gsoc, openMP, parallel, optimization
Author: Shikhar Bhardwaj

This week was spent implementing some initial ideas for Stochastic Co ordinate descent. I 
have started with a serial implementation first, as I believe parallelizing the serial code
would be trivial with this optimizer. Some changes were made to the Logistic regression function
implementation to be compatible with this new optimizer and provide the required partial gradient
information.

Goals for the next week include : 
1. Optimizing the `FeatureGradient` implementation in Logistic regression. Currently, it does more work than 
necessary.
2. Resolve some potential "serializers" in the computation. For example, the logistic regression
function currently uses an intercept term. I believe dropping the term would be required for AsySCD
to work, as independent threads would block each other trying to update the intercept in addition to the
individual features handed out to each thread.
3. Implement and test the effects of the Greedy descent policy on the optimizers performance.
4. Currently, I have added a simple test for SCD, based on a precalculated minima. Adding some more
extensive tests is needed.

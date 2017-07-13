Title: Profiling for parallelization and parallel stochastic optimization methods - Week 4
Date: 2017-06-27 17:26:00
Tags: gsoc, openMP, parallel, optimization
Author: Shikhar Bhardwaj

This week I completed the initial implementation of parallel SGD, along with a couple of tests
for the new code. The PR ([#1037](https://github.com/mlpack/mlpack/pull/1037))
is nearly ready for an initial review. With further discussion, I would add more sophisticated 
and detailed methods of testing. Some SFINAE code needs to be added to handle the current 
interface of DecomposableFunctionType.

I would like to test this implementation against the original runs mentioned in the paper,
to see the difference in results obtained from an OpenMP based implementation. I have already 
implemented the SparseSVM example.

The next few days would be focussed primarily on implementing more tests, running ParallelSGD
on the datasets mentioned in the paper and possibly profiling mlpack's implementation of
GMM for potential parallelization with OpenMP.

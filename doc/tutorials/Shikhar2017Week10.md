@brief Profiling for parallelization and parallel stochastic optimization methods - Week 10 + 11
@author Shikhar Bhardwaj
@page Shikhar2017WeekTenEleven Profiling for parallelization and parallel stochastic optimization methods - Week 10 + 11
@date 2017-08-17 01:09

@section Shikhar2017WeekTenEleven Profiling for parallelization and parallel stochastic optimization methods - Week 10 + 11

The past two weeks were spent on finishing up the implementation of SCD(adding the Greedy descent 
policy based on GS rule), adding more tests for the new code and making changes to existing
functions to make them compatible with the `ResolvableFunctionType` requirements. Some
documentation outlining the various `FunctionType` interfaces was also added to highlight the
minor differences and applications of these abstractions.

A minor inconsistency needs to be resolved which would require some simple refactoring to make
the layout of the decision variables consistent across various functions in `mlpack` so that
SCD could work on disjoint parts of the decision variable (required for parallelization).

I am planning to finish up the refactoring and parallelisation part within the next 1-2 days.
The next steps would be to benchmark the implemenatation on a few datasets to get an overview
of the performance and find any areas of improvement.
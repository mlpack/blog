Title: Dataset and Experimentation Tools : Week-6 Highlights
Date: 2016-07-05 16:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

I continued working on DatasetMapper & Imputer to finalize the pull request last week.
All DatasetMapper, Imputer, Policy, and Imputation classes and their tests are ready for the last review.

The executable is also ready for the final review.

The changes I made are:

1) Load funciton can now work with any type of DatasetMapper class. Policy can also be decided by the user.

2) MissingPolicy now maps user-defined missing variables to NaN. 

3) We had problem how data::Load maps through the MapToNumerical function.
In order for MissingPolicy to work, the mapping should be done only for the missing variables,
not the whole variables in the dimension. And IncrementPolicy requires the whole variables in a dimension
to be mapped if at least one variable turns out to be categorical (string).
I solved this by moving MapToNumerical from data::Load to Policy classes, so that
each policies can decide how to map the tokens. I also renamed this function to MapTokens to be clear.

4) completed tests and cleaned the apis so that they are more consistent.

This week, I am going to work on statistics module.
The statistics module would be a simple executable application to start with;
the features we want to add are some what similar to [this application](http://personality-project.org/r/basics.t.html).


Title: Dataset and Experimentation Tools : Week-3 Highlights
Date: 2016-06-13 18:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

Last week, I planned to finalize missing variable and imputation strategies.
Tham gave me advices and ideas for implementing the Imputer and DatasetMapper classes.
So I was able to:

1) Rewrite and finalize Imputer class, DatasetMapper class, and CLI executable that provides imputation methods for missing variables.
I modularized the mapping policies and imputation strategies. So that they could be used interchangably.

2) Implement utility functions, which are: one-hot-encoding, standard-scale (standardization) and min-max-scale (normalization).

One of the concerns I am having is that some features I have planned are already implemented in armadillo library or mlpack.

I think I had more time reading and analyzing the code so far.
As a result, I am getting used to the styles of mlpack and C++ in general.
Next week, I will:

1) Refine and make pull requests for one-hot-encoding and min-max-scale.

2) Start working on statistical analyzing cli executable.

3) Plan and implement proof-of-concept for function that scans through a file and detects faults(can be used independently or before data::Load).
   I have to think how to re-use or modularize the code in data::Load() since it already has tokenizers.

4) Start worrying about how to treat datetime variables.
(As of now, mlpack fails to map variables like "1993.05.12" or "1993/05/12". It just recognizes it as number with the first "1993" and discards the rest)

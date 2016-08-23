Title: Dataset and Experimentation Tools : Summary
Date: 2016-08-23 14:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

In this blog post I'll try to describe my contributions I've made to mlpack this summer.

### Summary

Here is the link for all my pull requests [pull requests](https://github.com/mlpack/mlpack/pulls?q=is%3Apr+is%3Aclosed+author%3Akeonkim).
Below is the list of the major pull requests with self-explanatory descriptions.

 * Descriptive Statistics command-line program : [742]
 * DatasetMapper & Imputer  [694]
 * delete unused string_util : [672]
 * fix default output problem and some styles : [680]
 * Binarize Function + Test : [666]
 * add cli executable for data_split : [650]

### Descriptive Statistics

I originally built a [class](https://github.com/keonkim/mlpack/commit/c2f5c5c2e6cbce084992629e192023519873e4cb) that calculates descriptive statistics. But after a few discussion, I ended up shrinking all of the functions down to minimum to provide maximum performance and maintainability.
I also merged all commits to one to discard unnecessary commits.

Sample output on "iris.csv" would be:
```
[INFO ] dim     var     mean    std     median  min     max     range   skew    kurt    SE      
[INFO ] 0       0.6857  5.8433  0.8281  5.8000  4.3000  7.9000  3.6000  0.3149  -0.5521 0.0676  
[INFO ] 1       0.1880  3.0540  0.4336  3.0000  2.0000  4.4000  2.4000  0.3341  0.2908  0.0354  
[INFO ] 2       3.1132  3.7587  1.7644  4.3500  1.0000  6.9000  5.9000  -0.2745 -1.4019 0.1441  
[INFO ] 3       0.5824  1.1987  0.7632  1.3000  0.1000  2.5000  2.4000  -0.1050 -1.3398 0.0623  
```
Users can control the width and precision using -w and -p flag.
I tested the output using excel and they match perfectly.

### DatasetMapper & Imputer

I renamed DatasetInfo to DatasetMapper, which accepts template parameter of MapPolicy.
( can be used to store different kinds of maps.)
DatasetMapper, however, still provides backward compatibility with typedef:
`using DatasetInfo = DatasetMapper<IncrementPolicy>`.
The IncrementPolicy denotes the original mapping policy used,
which increments numbers for different categories, starting from 0.

Imputer class is also added in this pull request.
Imputer also accepts template parameter called ImputationStrategy,
so that different strategies can be applied.

Lastly, a command line program called "mlpack_preprocess_imputer.cpp" was added to the mlpack.

### Binarizer

This is a simple implementation of binarize function which transforms
values in matrix to 0 or 1 according to the threshold.
You can use `umat A = (B > C)` but this function has a overload
that applies binarize to only one dimension. Plus,
it can produce any type of matrix, not umat.

### Spliter

I added TrainTestSplit() and renamed old ones to LabelTrainTestSplit() as discussed in #651 .
This is just a naive implementation mostly copied from Tham's work.
I believe LabelTrainTestSplit can just reuse the code in TrainTestSplit twice for both data and labels.

I also implemented "mlpack_preprocess_split.cpp".

### Other changes

I also made minor contributions in debugging and fixing styles, especially related to data IO.

### TODOs

I wish to keep contributing to mlpack.
I will try to polish the works a little bit more, and especially,
I would LOVE to contribute to the deep learning modules.
I've been personally reading papers about sequence-to-sequence models,
which are used widely for natural language processing and timeseries data analytics.

### Acknowledgement

I thank the mlpack mentors and especially to Tham who gave me a lot of advises through code reviews.

[742]: https://github.com/mlpack/mlpack/pull/742
[694]: https://github.com/mlpack/mlpack/pull/694
[672]: https://github.com/mlpack/mlpack/pull/672
[680]: https://github.com/mlpack/mlpack/pull/680
[666]: https://github.com/mlpack/mlpack/pull/666
[650]: https://github.com/mlpack/mlpack/pull/650

@brief Visualization Tool - Week 02
@author Jeffin Sam
@page Jeffin2020Week02 Visualization Tool - Week 02
@date 2020-06-14 21:11:28

@section Jeffin2020Week02 Visualization Tool - Week 02

The second week of GSOC concluded successfully. During the week I resolved the comments made during multiple reviews on the first PR, and now it has finally been approved and ready to be merged. So we do have our first look of `mlboard` ready. 

Also during the week two separate [PR#3](https://github.com/mlpack/mlboard/pull/3) and [PR#4](https://github.com/mlpack/mlboard/pull/4) were raised to set up the azure pipelines for the CI jobs.

Also during the weekly meeting, it was decided to set up some unit testing for mlboard, and we found `catch2` to be interesting and easy to be adopted since it is a header-only library. A draft [PR#5](https://github.com/mlpack/mlboard/pull/5) was raised to be able to integrate `catch2` into `mlboard` for testing using `CMake`.

Going ahead I plan to complete the cache unit testing work and also add support for Logging Image summary using mlboard. And for both, I am assuming two weeks of the expected time of implementation.

So that was the whole update from the past week and also plan for upcoming weeks, Will keep you all posted. Thanks for reading it through. Good Day.

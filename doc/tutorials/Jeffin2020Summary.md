@brief Visualization Tool - Summary
@author Jeffin Sam
@page Jeffin2020Summary Visualization Tool - Summary
@date 2020-08-27 18:21:28

@section Jeffin2020Summary Visualization Tool - Summary

This post summarize my work for GSoC 2020

# Overview

The proposal for Visualization tool included the implementation of class which would be able to log metrics and a callback function that can be passed to ensmallen optimizer to log metrics.

# Implementation

A separate repo was created to undertake the project to avoid adding dependencies to mlpack main package.

### Initial Setup [PR#1](https://github.com/mlpack/mlboard/pull/1)

* The implementation started with setting up the repo structure and making it compatible to be installed over any os. `FileWriter` class and `SharedQueue` class was implemented in this PR.

### Setup CI pipeline [PR#3](https://github.com/mlpack/mlboard/pull/3)

* Then we setup the pipeline for azure builds so that we continously know that we are not breaking anything.

### Setup Catch Testing [PR#5](https://github.com/mlpack/mlboard/pull/5)

* This PR was raised to add Catch2 as testing framework and write some test.

### Add Image Support [PR#6](https://github.com/mlpack/mlboard/pull/6)

* We added image support in this PR.

### Add Text Support [PR#7](https://github.com/mlpack/mlboard/pull/7)

* We added text support in this PR.

### Add PRCurve Support [PR#12](https://github.com/mlpack/mlboard/pull/12)

* We added PRCurve support in this PR.

### Add Embedding Summary Support [PR#10](https://github.com/mlpack/mlboard/pull/10)

* We added embedding support in this PR.

### Add Histogram Support [PR#13](https://github.com/mlpack/mlboard/pull/13)

* We added Histogram support in this PR.

### Add Callback Support [PR#14](https://github.com/mlpack/mlboard/pull/14)

* We added Callback support in this PR.

# Post GSoC

Improve cmake scripts a litle bit, possible improvements in implementation and Improve callback for bettery visualization.

# Acknowledgement

A big thanks to Toshal, Brim, Rcurtin, Zoq and the whole `mlpack` community. This was my second GSoC with mlpack, and I am happy that once again I was successful in it. I gathered a lot of knowledge in these past 3 months. I will continue to be in touch with the `mlpack` community and seek to do more contributions to the project in the future. 

Also, I think its time to order some mlpack stickers :)

Thanks :)

You can find my weekly reports here

* [week1](https://www.mlpack.org/gsocblog/Jeffin2020Week01.html)
* [week2](https://www.mlpack.org/gsocblog/Jeffin2020Week02.html)
* [week3](https://www.mlpack.org/gsocblog/Jeffin2020Week03.html)
* [week4](https://www.mlpack.org/gsocblog/Jeffin2020Week04.html)
* [week5](https://www.mlpack.org/gsocblog/Jeffin2020Week05.html)
* [week6-7](https://www.mlpack.org/gsocblog/Jeffin2020Week06-07.html)
* [week8-11](https://www.mlpack.org/gsocblog/Jeffin2020Week08-11.html)

Thanks, Signing off :)


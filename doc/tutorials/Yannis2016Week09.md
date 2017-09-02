Title: Modeling LSH - Implementation Week 1
Date: 2016-07-26 20:20:20
Tags: gsoc, lsh, modeling, gamma
Author: Yannis Mentekidis

This past week I began making the changes that will be required in order to make the LSH model a part of mlpack.

One of the basic parts of the model is the extrapolation, from data, of the distribution of squared euclidean distances. This is obviously very important - if we know what distances to expect, we can tune our LSH to correctly separate points that are too far away while grouping together nearby points more efficiently.

The authors propose using the Gamma Distribution, because
 a. It fits a lot of multimedia datasets
 b. It has an intuitive explanation of why distances would follow it and
 c. It is easy to fit its parameters to data.

So, in this first week, I implemented a new mlpack distribution - the Gamma Distribution. The implementation is incomplete - I've listed in Issue [`#733`][1] what else needs to be done in order for it to be a proper and usable mlpack distribution.

The implementation required backporting a small part of Boost 1.58, since our dependency is Boost 1.49.0 or older. Specifically, I backported the part of Boost that calculates the functions [trigamma(.)][2] and [polygamma(.)][3], which were necessary for the Maximum Likelihood Estimation.

With this implemented and tested, I can start working on the body of the LSH model.

[1]: https://github.com/mlpack/mlpack/issues/733
[2]: http://www.boost.org/doc/libs/1_58_0/libs/math/doc/html/math_toolkit/sf_gamma/trigamma.html
[3]: http://www.boost.org/doc/libs/1_58_0/libs/math/doc/html/math_toolkit/sf_gamma/polygamma.html
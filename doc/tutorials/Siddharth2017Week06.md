Title: Regularized SVD
Date: 2014-07-07 22:45:00
Tags: gsoc, svd, cf
Author: Siddharth Agrawal

I spent the past two weeks writing and testing Regularized SVD, which has been the most popular algorithm for Collaborative Filtering and also won the Netflix challenge. Below you can find a description of the algorithm that I included in my application:

Regularized SVD is a matrix factorization technique that seeks to reduce the error on the training set, that is on the examples for which the ratings have been provided by the users. It is a fairly straightforward technique where the user and item matrices are updated with the help of Stochastic Gradient Descent(SGD) updates. The updates also penalize the learning of large feature values by means of regularization. Unlike QUIC-SVD, here the rank of the user and item matrices has to be passed as a parameter in addition to the regularization parameter 'lambda'. The model can also be improved upon, by introducing bias terms for each of the users and items, which leads to a reduction in the Root Mean Squared Error(RMSE). Regularized SVD has been found to be the most accurate model available for collaborative filtering, for datasets having a rating matrix density of 2-5%, which for all practical purposes includes most of the datasets.

While implementing the algorithm, I discovered a drawback in the SGD optimizer abstraction of MLPACK. SVD algorithms used for Collaborative Filtering decompose the rating matrix into latent user and item matrices. While this performs fairly well in terms of recommendations, it also introduces a large number of parameters. I use the term 'large' relatively over here, it is large compared to the parameters we update in one SGD iteration.

This results in SGD execution being extremely slow. This was, ofcourse, improved, by carrying out updates over all the examples at one go. L_BFGS was used to test it out and performs reasonably well over the GroupLens dataset.

The unit tests for the module still need to be written, but this should be fairly straightforward compared to QUIC-SVD.

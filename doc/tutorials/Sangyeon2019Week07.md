@brief Quantum Gaussian Mixture Models - Week 7
@author Sangyeon Kim
@page Sangyeon2019WeekSeven Quantum Gaussian Mixture Models - Week 7
@date 2019-07-11 19:11:00

@section Sangyeon2019WeekSeven Quantum Gaussian Mixture Models - Week 7

This week, I tested the training performance of QGMM using Adam optimizer with learning rate = 0.001 and the lambda is 1.

Below are the findings.

1. Covariance become negative.
: When optimizing the full covariance, I found some elements of covariance became negative and it
was the cause of errors in calculating Cholesky’s decomposition and drawing it.
Therefore, I changed the full covariance form into lower triangular form and it is composed later
into the full covariance matrix ( L∗L
T
) when calculating the unnormalized gaussian to make all
the element positive and the covariance symmetric. As a result, a learning process become more
stable.

2. According to the initial values, the training results vary.
: From the results, the initial center position and the shape of covariance had effects on the
performance of training.
From the video t5 in NLL and NLL with constraint, it was a case that one cluster’s initial
normalized gaussian value is almost zero while another isn’t.

3. NLL vs NLL with constraint
: From the video t3 in the NLL and NLL with constraint directory, NLL showed a better result.

Thanks for reading :)

@brief Implementing Improved Training Techniques for GANs - Week 4
@author Saksham Bansal
@page Saksham2019Week4 Implementing Improved Training Techniques for GANs - Week 4
@date 2019-06-25 03:05:00

@section Saksham2019Week4 Implementing Improved Training Techniques for GANs - Week 4

This week I mainly debugged my `VirtualBatchNorm` code as the numerical gradient test was failing. I was re-checking my derivations on paper and getting the same results as before. I checked my implementation where I couldn't find any problems. Later I discovered that I had made a silly mistake in the model for the numerical gradient test. I was adding a `Linear<>` layer of input size 10 whereas the output from the previous layer had size 5. After fixing the model, the numerical gradient test started to pass.

Additionally, I did some more work on the regularizers and making changes to my currently opened PRs. In the upcoming week I hope to finish with the regularizers PR and start working on spectral normalisation which seems more mathematically challenging.

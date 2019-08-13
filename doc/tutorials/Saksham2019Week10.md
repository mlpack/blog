@brief Implementing Improved Training Techniques for GANs - Week 10
@author Saksham Bansal
@page Saksham2019Week10 Implementing Improved Training Techniques for GANs - Week 10
@date 2019-08-12 03:05:00

@section Saksham2019Week10 Implementing Improved Training Techniques for GANs - Week 10

This week has been productive. I was able to finish the regularizers PR and it has been merged. I was able to complete the work for `CGAN<>` after implemneting a `Concat<>` visitor and have also a written a test for that. After we can successfully produce results from the CGAN I think that would also be ready for merge.
I think the major task that remains would be checking the gradient issue in GAN as pointed out by Toshal.
I have also kept my other PRs on `Padding<>` and `MinibatchDiscrimination` layers updated. The work there is complete however is blocked as we are unable to support more than 50 layer types at the momemt. Hopefully we can find a solution in the coming weeks.

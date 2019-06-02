@brief Implementing Essential Deep Learning Modules - Week 1
@author Toshal Agrawal
@page Toshal2019Week01 Implementing Essential Deep Learning Modules - Week 1
@date 2019-06-02 19:20:00

@section Toshal2018Week01 Implementing Essential Deep Learning Modules - Week 1

In this week I have completed my serialization Pull Request. Finally, it is ready to merge. While working on it I faced a `Integer divide by zero` error. Tracking the source of error was quite a tedious and patience testing job. But finally, I was able to find that the Mean Pooling layer is not serializing properly. After that I also figured out that some other layers are also not serilaizing correctly, so fixed them and made Pull Request for same.

After completing my serialization PR. I started working on `Label Smoothing`. Though One-Sided Label Smoothing is preferred in GANS. I am providing option for both side label smoothing. I would require both side label smoothing for LSGANs implementation.

Also in my free time I set up my IRC bouncer correctly. Earlier I was just using ZNC. But later on ShikharJ introduced me to eliteBNC and I realized that we need to have a free bouncer and not just a bouncer.

I am thinking to continue with my Dual Optimizer PR. I got somewhat familiar with `Secure Shell` so I was thinking to start testing it soon.

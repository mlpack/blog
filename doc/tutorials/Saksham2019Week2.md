@brief Implementing Improved Training Techniques for GANs - Week 2
@author Saksham Bansal
@page Saksham2019Week2 Implementing Improved Training Techniques for GANs - Week 2
@date 2019-06-02 22:05:00

@section Saksham2019Week2 Implementing Improved Training Techniques for GANs - Week 2

This week I worked mainly on finishing `MiniBatchDiscrimation` layer. I was able to optimize my previous implementation by using stored results and avoiding re-computation. My work on `Highway` layer is nearly complete and has been approved by ShikharJ. Hopefully it should be merged by next week.
My work on `Inception Score` is also complete but needs to be tested. I am still not sure regarding how testing will be carried out for the metrics but hopefully that would become more clear over next week. I have also started implementing `VirtualBatchNormalization` layer side by side and will open a PR for it by next week.

Also while implementing new layers another problem has shown up. `boost::variant` can only handle up to 50 types and the number of layers for ANN have quickly exceeded that limit. As I will be working on adding many new layers over the coming weeks it is important to find a solution to the problem. One quick solution to the problem is `boost::make_variant_over` which exposes a variant whose bounded types are elements of Sequence. I tried working on this but my general lack of experience with metatemplate programming and knowledge about `boost::mpl` proved to be fatal as I was unable to debug the cryptic messages that were produced after multiple trial and errors.

In the coming weeks I hope to start working on introducing regularisers for layers in mlpack API. I have started testing design ideas for introducing regularizers and I think that regularisers could fit easily inside the mlpack ANN modules.

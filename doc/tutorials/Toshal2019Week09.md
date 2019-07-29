@brief Implementing Essential Deep Learning Modules - Week 9
@author Toshal Agrawal
@page Toshal2019Week09 Implementing Essential Deep Learning Modules - Week 9
@date 2019-07-29 01:10:00

@section Toshal2019Week09 Implementing Essential Deep Learning Modules - Week 9

In this week I have added a visitor for getting `Bias` weight from the layers. It looks like I will need to add one more visitor to make my weight normalization work correctly. I am thinking to implement a visitor which will only set `Non-bias` weights. I am thinking to use the newly added `Bias` visitor to make it work correctly. I also tried to get into `spectral normalization` on which Saksham is working. I need sometime to understand that paper. Saksham needs the dimensions of non-bias weights. If he just needs them for intializing then it's good or else I will need to change the implementation of my visitors.

There are quite a lot of things to work in this week. I will complete my work on the `Inception Layer`. It will need some time for completing it. But yes I am aiming to complete it in this week itself.

Also I wish to complete my work on the `exact-objective` PR. It is one of the top priorities this week. I am also thinking to work on `LSGANs`. There is a quite a lot of todos this week. I hope I can complete everything and would be able to write a big blog on next Sunday. Till then that's it.

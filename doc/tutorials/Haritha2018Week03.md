@brief Neural Collaborative Filtering - Week 3
@author Haritha Nair
@page Haritha2018Week03 Neural Collaborative Filtering - Week 3
@date 2018-06-24 17:20:25

@section Haritha2018Week03 Neural Collaborative Filtering - Week 3

This week I spend time trying to create neural network models for GMF and MLP. But both of them need some features which aren't directly producable using the existing FFN class. I tried to use the sequential layer for the same but that path turned out to be a dead end. Based on suggestions from Marcus, right now I am working on creating a new NCF network class which can provide the necessary methods for model creation for all 3 NCF algorithms. There is a plan on getting some inspiration from the GAN class too, which is currently under development.

Another part I concentrated on was loading and manipulating data as implicit feedback data. The method is working perfectly fine, but I had to put in some effort to reduce the time taken for its processing, which is much needed considering its extensive usage in the training step.

The CF class refactoring PR has been completely debugged and can be merged in a day or two.

Overall, the project is going fine and I hope that the pace will get better once the basic methods are all set up.

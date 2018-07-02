@brief Neural Collaborative Filtering - Week 7
@author Haritha Nair
@page Haritha2018Week07 Neural Collaborative Filtering - Week 7
@date 2018-07-02 18:09:00

@section Haritha2018Week07 Neural Collaborative Filtering - Week 7

Another week has passed and I think it has been a really productive one. There have been a few good developments. The PR for modifying subview layer has been merged. I have also opened a PR for the basic structure of the NCF class and all its member functions with basic documentation. Currently the `CreateModel()` methods, `GetTrainingInstance()`, `CreateNegatives()` etc have been added. There was some issues with running GMF model, which has been resolved with help from Marcus.

Currently I am working on modifying training instances in between epochs and thus working on the `Evaluate()` method of the `NCFNetwork` wrapper class, which already has an open PR. I am also working on `Evaluate()` of NCF, but I think I will keep the training part on priority since its proper implementation is needed for having a working evaluation method. So this week, I consider the main goals to be to keep adding completed methods to NCF class and also to continue working on making training possible using multiple instances.

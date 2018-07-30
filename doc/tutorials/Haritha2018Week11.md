@brief Neural Collaborative Filtering - Week 10 & 11
@author Haritha Nair
@page Haritha2018Week11 Neural Collaborative Filtering - Week 10 & 11
@date 2018-07-31 19:27:00

@section Haritha2018Week11 Neural Collaborative Filtering - Week 10 & 11

Week 10 went a bit slow due to college reopening and shifting etc and that is why I skipped writing a not so significant blog post. Last week I debugged the whole `NCF` class code along with `ncf_main` and it is building successfully now. I have also added support for user choice regarding whether to use implicit or explicit feedback (a normal dataset can be converted to implicit form if necessary). We have decided to move on with two seperate command line executables for `cf` and `ncf` since the CLI arguments and the methods to work upon have nothing much in common. There was a slight issue with the `CreateNeuMF` method which I have been trying to debug and have not been able to identify the source of error.

So this week I intend to debug `neumf` while parallely testing the implemented `GMF` and `MLP` methods. Its finally time to see the results! I have also started writing some proper tests for `ncf` and intend to finish it within this week. If all goes well we can finally get some comparable results, working CLI and tested `NCF` code by end of this week. :)

@brief Neural Collaborative Filtering - Week 8
@author Haritha Nair
@page Haritha2018Week08 Neural Collaborative Filtering - Week 8
@date 2018-07-10 06:30:00

@section Haritha2018Week08 Neural Collaborative Filtering - Week 8

The second phase has ended and at this point I think we are very much close to having a basic implementation of `NCF` in mlpack. I spend this week mainly making modifications to the `GetRecommendations()` method and creating the `EvaluateModel()` method. They have been completed and pushed. `EvaluateModel()` now evaluates the model on two parameters, `hit ratio` and `RMSE`. But the `Train()` method hasn't been completed yet, slight modifications are still necessary to add `Gradient()` and `Evaluate()` in NCF, and work on it is ongoing with input from Marcus. So the entire class can be tested once `Train()` is complete.

Right now I am also working on `ncf_main`, this will hopefully help us use `NCF` from command line interface too. By end of this week I intend to have a proper trainable `NCF` so that all methods can be tested and the network evaluated. There might be some debugging necessary after `Train()` is completed. But apart from that the basic class, along with CLI is expected to be ready by end of the week.

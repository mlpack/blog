@brief Neural Collaborative Filtering - Week 6
@author Haritha Nair
@page Haritha2018Week06 Neural Collaborative Filtering - Week 6
@date 2018-06-25 13:30:00

@section Haritha2018Week06 Neural Collaborative Filtering - Week 6

It has been a very active week with much work on the Subview layer PR with focus on adding batch support and managing all kinds of input parameters to the layer.

We are also much more closer to the completion of the CreateModel() method for all the three algorithms. I spend time this week figuring out the correct way to create models for MLP and Neural matrix factorization. There have been some work on flattening the embeddings using the concat layer which led to further modification in CreateModel() for GMF. Altogether the method is almost ready to be added to NCF. Work has also been ongoing with GetRecommendations() method although I wasn't able to get started with Evaluate() as per plan.

This week I intend to add the GetTrainingInstance(), CreateModel() and GetRecommendations() as part of NCF class and make a PR so that reviewing of it goes parallel to future work. Subview layer has been debugged and can be merged soon enough. I also intend to spend time on Evaluate() this week.

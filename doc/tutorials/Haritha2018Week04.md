@brief Neural Collaborative Filtering - Week 4
@author Haritha Nair
@page Haritha2018Week04 Neural Collaborative Filtering - Week 4
@date 2018-06-11 08:44:53

@section Haritha2018Week04 Neural Collaborative Filtering - Week 4

The best news this week is that the CF refactoring PR finally got merged and thus now adding new decomposition policies in CF module will be much easier.

I have been working on implementing a NCFNetwork class to act as a wrapper network class for creating NCF networks. This was done so that two input matrices, one for item and one for user can act as input matrices to train upon. A PR has been opened for the same although midway the plan changed a bit, to introduce a new Subview layer so as to split training data into user and item, after it has entered the network as merged input. There were some issues with the existing implementation of merge layers which prevented them from being used in FFN-s, which has been debugged by Marcus. I have further tried to implement the subview layer, for which too a PR has been made.

Once the subview layer and the changes in the merge layers are merged, we will be much closer to the final implementation of CreateModel() for both GMF and MLP. I have also started working on the GetRecommendations() for generating K best recommendations.

Hopefully by end of this week, all basic functions needed for NCF, except Evaluate(), will be implemented independently.

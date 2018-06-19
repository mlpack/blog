@brief Neural Collaborative Filtering - Week 5
@author Haritha Nair
@page Haritha2018Week05 Neural Collaborative Filtering - Week 5
@date 2018-06-19 06:03:53

@section Haritha2018Week05 Neural Collaborative Filtering - Week 5

After much modifications I have been able to reduce the execution time of GetTrainingInstance() which creates training instances for given implicit data along with negatives. 

The subview layer PR has been merged although there are a few changes being made to improve the functionality of the layer. I am facing a few issues when using the newly created subview layer is merged with existing neural network models, which I am trying to debug right now. Once it has been completed the CreateModel() method will be ready. There has been progress in the GetRecommendations() method too, but it can be tested well only when the model creation part has been completed.

I intend to concentrate on finalizing CreateModel() and GetRecommendations() this week and also to get started with Evaluate(). All these functions are common to the three algorithms, with only minute changes. So completing their implementation will be a great leap to current workflow.

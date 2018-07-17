@brief Neural Collaborative Filtering - Week 9
@author Haritha Nair
@page Haritha2018Week09 Neural Collaborative Filtering - Week 9
@date 2018-07-17 11:45:00

@section Haritha2018Week09 Neural Collaborative Filtering - Week 9

Another week is over and I think we are a few more steps closer to having Neural Collaborative Filtering implemented in mlpack. This week I modified the `Train()` method, added `Gradient()` and `Evaluate()` based on suggestions from Marcus so that we can deal with training instances within epochs. I also modified the current `NCF` class to accept an AlgorithmType and create a network according to the user specified algorithm. I also completed `ncf_main` so that we can access the NCF algorithms from command line interface. I have also added Neural matrix factorization to the existing `NCF` algorithms.

So now that the basic structure is ready, I am currently spending time on debugging the code. I had initially focussed on making the model work on implicit feedback, but now I am making slight modifications to generalize it to both implicit and explicit feedback cases. This week I intend to work on all the errors and small changes required so that by end of the week we have a working NCF class, trainable on multiple optimizers for both implicit and explicit data.

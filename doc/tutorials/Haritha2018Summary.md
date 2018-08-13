@brief Neural Collaborative Filtering - Summary
@author Haritha Nair
@page Haritha2018Summary Neural Collaborative Filtering - Summary
@date 2018-08-13 18:40:00

@section Haritha2018Summary Neural Collaborative Filtering - Summary

# Overview

The project started with the main aim of implementing a new bunch of algorithms to mlpack which can implement collaborative filtering using neural networks based on the paper [Neural collaborative filtering][ncf-paper] by Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu and Tat-Seng Chua (2017). . The algorithms under neural collaborative filtering was expected to enable usage of implicit feedback along with explicit to train models for recommendations. The model was also expected to represent complex user item interactions which normally get missed out when using matrix factorization based collaborative filtering methods.

# Implementation

#### CF class refactoring

One of the initial challenges was the integration of new collaborative filtering methods to existing class. It was decided upon to modify the `CF` class to a policy based design where a template parameter `DecompositionPolicy` is used to perform CF using different decomposition methods. The [Pull Request #1355][1355] focussed on this and we were able to merge the PR with some useful functionalities such that in future, adding new decomposition methods to CF will be much easier. The PR also added `RandomizedSVD` as a decomposition policy in CF and modified the CF class tests to accommodate these changes.

#### New layers in `ann` module

Another challenge to the project was the unavailability of some necessary layers for creating the NCF networks, like `Embedding`, `MultiplyMerge`, `Flatten` etc. After much discussion, the `lookup` layer in mlpack was aliased to use as embedding layer in [Pull Request #1401][1401]. `MultiplyMerge` layer was created for performing element wise multiplication while merging two networks ([Pull Request #1392][1392]).  

The NCF networks deal with two inputs, user and item and thus the structure which needs to be accommodated cannot be trained with normal `Train()` since it takes only one input. It was decided to create a `Subview` layer which can split input data within the network so that this issue can be managed. The subview layer acts as an intermediate layer with functions of creating submatrix, vectorizing, flattening etc. The [Pull Request #1428][1428] implements this layer and I believe this is a very much useful addition to the codebase.  
The subview layer was further modified in [Pull Request #1435][1435] to adapt it to matrices and enable batch support.

#### NCF class

The major part of the project, the neural collaborative filtering class was added in [Pull Request #1454][1454]. The class started of with basic data members and member functions and methods were added to it during the course of the project. The class currently has the following major methods:  
* `FindNegatives()` - Collect data of items which haven’t been rated by a user and store them in a vector, to be used later while collecting instances to train.  
* `GetTrainingInstance()` - According to whether the user requires the model to be for implicit or explicit feedback, this method creates instances for training, maintaining a user defined ratio between positive (rated) and negative (non rated) instances. The method returns predictors and responses for the network to be trained on.  
* `CreateGMF()`, `CreateMLP()`, `CreateNeuMF()` - These are the methods for creating networks according to the algorithm required. They have unique network structures and implement it using `Sequential`, `MultiplyMerge`, `Linear`, `Concat`, `Subview`, `Embedding` layers.  
* `GetRecommendations()` - Generate n recommendations based on the trained model and predicted rating from it.
* `EvaluateModel()` - This method evaluates the model based on the recommendations it generates, on parameters like RMSE and hit ratio.  
* `Train()`, `Gradient()` and `Evaluate()` - These functions enable training of the model from `NCF` such that the training instances can be changed in between each epoch, and the calls can be forwarded to corresponding functions of `FFN`.

#### Command Line Interface

`NCF` has a command line interface implemented through `ncf_main` in [Pull Request #1454][1454]. It lets the user to use any dataset for training, testing etc where the user can specify whether the dataset is to be considered as implicit or explicit, the algorithm to use among `GMF`, `MLP` and `NeuMF`, the number of negative instances per positive instance to train upon, the embedding size to be used in the network, the optimizer to use while training the network etc. It was decided to have a seperate CLI for `NCF` since the arguments and functions required by `CF` and `NCF` have not much in common.

##### CLI usage

The command line interface provides many options to use the NCF class.  
* --training (-t) defines the training dataset given as a csv file.  
* --algorithm (-a) parameter defines the algorithm to be used which could be 'GMF', 'MLP' or 'NeuMF'.  
* --all_user_recommendations (-A) can be set for generating recommendations for all users and --query (-q) for a specific set of users.  
* --recommendations (-c) can be used to set the number of recommendations to be generated.  
* --optimizer (-z) can be used to choose an optimizer from among 'adagrad', 'rmsprop', 'adam', 'SGD'.

Example usage:

* mlpack_ncf --help : Get full documentation.  
* mlpack_ncf -t "ml-100.csv" -A -o "recommendation.csv" -c 10: Train on ml-100.csv, save 10 recommendations each for all users to recommendations.csv.  
* mlpack_ncf -t "ml-100.csv" -a "GMF" -z "SGD" -t "ml-100test.csv" : Train using GMF algorithm and SGD optimizer and test on dataset ml-100test.csv.

#### Other Work

Some time was spent on dataset collection and modification to suit the requirements of implicit feedback data.  
[Pull Request #1422][1422] was opened to create a wrapper `NCFNetwork` class to enable using multiple input matrices to same network but was later discarded since `Subview` layer was used to come up with an alternate plan.

# Results

Currently, GMF is giving an RMSE of 3.3 on single epoch on movielens 100k dataset. Multiple epoch training and RMSE reduction is ongoing work.

# Summary

[Pull Request #1355][1355] - CF refactoring  
[Pull Request #1392][1392] - Multiply merge layer  
[Pull Request #1401][1401] - Embedding layer  
[Pull Request #1428][1428] - Subview layer  
[Pull Request #1435][1435] - Subview matrix and batch support  
[Pull Request #1422][1422] - NCFNetwork wrapper  
[Pull Request #1454][1454] - NCf Class

# Future Work

* Reduce execution time of methods in NCF like GetTrainingInstances().  
* Improve RMSE and hit ratio.  
* Add proper batch support to training and testing.  
* Write tests for NCF and ncf_main.

# Conclusion

It has been a wonderful summer working with mlpack. There has been a lot of coding, experimentation, a million builds and never ending debugging that to think that it is coming to a wrap up doesn’t feel much real. Now that I have a much better understanding of the mlpack codebase than when the summer began, I would like to keep contributing. Thanks a lot to Marcus for your constant support throughout the summer. You have made it loads easier to work, well, you have the solution to all errors :). I would also like to acknowledge the help from Ryan, who has always been available whenever needed, and the whole team of mlpack. This has been a summer worth remembering!

[1355]: https://github.com/mlpack/mlpack/pull/1355  
[1392]: https://github.com/mlpack/mlpack/pull/1392  
[1401]: https://github.com/mlpack/mlpack/pull/1401  
[1428]: https://github.com/mlpack/mlpack/pull/1428  
[1435]: https://github.com/mlpack/mlpack/pull/1435  
[1422]: https://github.com/mlpack/mlpack/pull/1422  
[1454]: https://github.com/mlpack/mlpack/pull/1454  
[ncf-paper]: https://www.comp.nus.edu.sg/~xiangnan/papers/ncf.pdf


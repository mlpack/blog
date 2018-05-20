@brief Neural Collaborative Filtering - Week 1
@author Haritha Sreedharan Nair
@page Haritha2018Week01 Neural Collaborative Filtering - Week 1
@date 2018-05-20 13:05:00

@section Haritha2018Week01 Neural Collaborative Filtering - Week 1

Its been one successful week with GsoC at mlpack, working on the project ‘Neural Collaborative Filtering’. The overall objective of the project, intended to be fulfilled over summer, is to implement a neural network based collaborative filtering method in mlpack. 

The major features added to the existing CF module would be the ability to generate recommendations based on both implicit (any kind of interaction of user with item) and explicit (ratings given explicitly by user for the item) feedback data. Also, the proposed model will be able to represent complex user-item interactions better than existing matrix factorization methods. The best part is, NCF can also be generalized to normal matrix factorization, when needed.

This week I have majorly devoted time to refactoring the existing CF class to a policy based design, which would hopefully increase the ease of adding new decomposition strategies to CF in future. This has been done in continuation to an already open PR by me for adding randomized SVD as a decomposition method in CF. The project thus intends to add NCF as a new decomposition policy comprising of three new algorithms – Generalized matrix factorization, Multi layer perceptron and Neural matrix factorization. 

I have also worked on adding two new layers in ANN, the multiply_merge layer and embedding layer (this will be an alias to the existing lookup layer). Both these layers are necessary for NCF’s network. Currently, I am resolving certain errors in the refactoring PR, which is under review. I have also started working on the basic NCF class structure and its member functions.

The first week has been exciting and I am sure the summer ahead will be equally interesting and productive.

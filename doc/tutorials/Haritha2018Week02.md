@brief Neural Collaborative Filtering - Week 2
@author Haritha Nair
@page Haritha2018Week02 Neural Collaborative Filtering - Week 2
@date 2018-05-28 16:20:00

@section Haritha2018Week02 Neural Collaborative Filtering - Week 2

Its been two weeks with GsoC at mlpack, working on the project ‘Neural Collaborative Filtering’. Last week, I majorly focused on refactoring the existing CF class to a policy based design. I tried my hand at templatizing it and after a lot of discussion over github and IRC, the PR is close to being merged.

I spend quite some time this week debugging the CF class code after the refactoring. Tests were modified and debugged to accomodate the same.

I also collected some datasets as needed by the NCF module, that is, data of negative instances and other rating based datasets, and converted them to csv format as required by mlpack. Since I had started with the basic structure of NCF class last week itself, I added a few functions to it this week once I got the dataset prepared. I majorly focussed on general matrix factorization(GMF) out of the three algorithms to be implemented. Some of the major additions are: a function to modify the training instances as required by GMF, a function for neural network creation in GMF.

Currently I am working on the CreateModel function which creates a network as needed by GMF and am trying to use the multiply merge layer effectively, for the same, with help from mentor.

This week has been as exciting as the first and the coming days look much more promising to me.

Title: Frank-Wolfe Algorithm for various atom domain - Week-2
Date: 2017-06-14 22:00:00
Tags: gsoc, optimization
Author: Chenzhe Diao

My work this week is mainly about adding more solvers for various atom domain constraint in FW algorithm. 

For the vector case, the atom domain defined by structured group norm is added. This solver is implemented as a template class, so that users can define their own GroupType class for the way to project to each group, as well as the norm for each group. As a special case, I implemented a GroupType class that the projection to each group is just the restriction of some vector support, and the norm in each group is defined as the lp norm. This is used as Jaggi's paper. (Maybe other structured groups, for example, projection to each group could be extracting information from each frequency band, could be added and tested later, if some people is interested in the future.)

For the matrix case, atom domain defined by different Schatten matrix norms is also implemented.

Also, for the update step of Frank-Wolfe algorithm, a line search solver using secant method is implemented.

Next step could be implementing some tricks to make the algorithm work faster, such as regularization or support prune. Tests of sufficiently large scales should also be performed in the future.

Title: FrankWolfe Algorithm and Solving Sparse Solutions of Atom Norm Constraint Problems
Date: 2017-08-28 23:00:00
Tags: gsoc, optimization, atom norm
Author: Chenzhe Diao

This post summarize my work for GSoC 2017.

# My Work
The basic work of my GSoC 2017 is to implement the Frank Wolfe Algorithm (Conditional Gradient Algorithm) in various situations. From the paper of Jaggi [RevisitingFrank-Wolfe](http://m8j.net/math/revisited-FW.pdf), we know that many sparse optimization problem with atom domain constraint could be solved by this Frank-Wolfe type algorithm. So I implemented:

* Classic Frank Wolfe Algorithm. The algorithm is implemented in class template, so that it could be used and extended in general forms. The algorithm needs 2 steps: solving the linear constraint problem and updating the solution. Users could extend the usage of the algorithm by writing their own classes defining these 2 steps. For constraint problem solver, I implemented the common case that the constraint is a unit lp ball. For updating step, I implemented the classic update rule and a line search method. I tested the convergence speed, and confirmed that the line search step, although adds some extra work, will give faster convergence speed.

* Orthogonal Matching Pursuit. Jaggi's paper revealed that if the constraint domain of the FW algorithm is just an atom norm bound, then the linear constraint problem would be very easy to solve. For example, in the vector case, if the constraint is a bound of the lp norm, the solution could be solved explicitly. A straightforward application is the Orthogonal Matching Pursuit (OMP) algorithm, where the update step is just to reoptimize the coefficients in the span of the current solution space. I also implemented the regularization functionality in the constraint problem solver, to help users to get faster convergence.

* Although we can use this Frank-Wolfe type algorithm to solve atom domain problems in a greedy fashion, it is known that using it directly will give slow convergence and large support size. I implemented the tricks in the paper: [RaoShahWright(2015)ForwardBackwardGreedy](https://arxiv.org/abs/1404.5692), which introduced:
  1. Enhancement step. It reoptimizes the atom coefficients within the atom norm constraint domain. It is realized using the projected gradient method.
  2. Truncation step. It tries to delete some inefficient atoms, which cancels the drawbacks of this FW type greedy algorithm. This will help us to get faster convergence, as well as a solution with better sparsity.

* I also implemented the constraint solver for other atom domains, such as the structured group norm constraint domain, and matrix Schatten norm constraint domain. An important application in the matrices case is the matrix completion problem. As MLPACK already has that solver implemented using the sdp optimizer, I changed the original implementation into a class template, which can accept both sdp optimizer and FrankWolfe optimizer to solve the matrix completion problem. I tried to compare the different algorithms, it seems that although the Enhancement step and the Truncation step above were added, the convergence of the Franke Wolfe Type algorithm is still very slow.

I currently made 2 PRs:
* [https://github.com/mlpack/mlpack/pull/1041](https://github.com/mlpack/mlpack/pull/1041)
* [https://github.com/mlpack/mlpack/pull/1087](https://github.com/mlpack/mlpack/pull/1087)

The matrix completion code using Frank-Wolfe type algorithm is already done. I will issue a new PR after my second PR got merged.

# Future Work
A lot of the codes I implemented are tricks to improve the convergence speed of the algorithm. However, most of them are only manually checked with small test problems that these methods are beneficial. We should test on large scale problems and see how everything really works. Also, we can compare the FW algorithm with other optimizers on similar problems, and see the pros and cons of using FW.

# Acknowledgement
I am really grateful to the help from Stephen, Ryan, Marcus, and the whole MLPACK community. It is my first time to join the open source world and it is a wonderful experience. It is also so cool to know so many machine learning people and discuss ideas with them. I will keep in touch with the mlpack community and I hope I can make more contributions to the project in the future.
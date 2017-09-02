Title: Atom domain class - Week 7
Date: 2017-07-24 21:00:00
Tags: gsoc, optimization
Author: Chenzhe Diao

This week, I was trying to get better structure for the atom domain code. When I was trying to add the full correction update method code for constrained problem in atom domain, I found that I need to rewrite a lot of things in the `UpdateSpan` class. So I decided to make a new class for atom domain operations. This structure is more general for atom domain optimization, although might make the OMP code less efficient. I will try some large scale tests to see how does that affect the performance.

Since there has been some API change between my old PR and my current code, I guess I will merge everything first. Also, I will make more tests in vector case for atom domain before I do the matrix completion comparison (which was my plan last week). 

Even for the vector case, I am still excited to see in the experiments how will the atom norm constraint and support prune step would affect the sparsity of the solution, as well as the convergence speed, comparing with the naive OMP solution. (People familiar with LASSO would know that L1 norm constraint would give sparsity automatically. In terms of the algorithm I implemented, the atom norm constraint problem uses projected gradient solver, where the projection step is simply a soft-thresholding on the atom coefficients. So I guess it will give better solution and faster convergence than OMP.)
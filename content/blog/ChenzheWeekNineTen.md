Title: Tests of Atom domain code for vector problems - Week 9 and 10
Date: 2017-08-12 19:00:00
Tags: gsoc, optimization
Author: Chenzhe Diao

I finally fixed all the API issues and many bugs, and opened a new PR for vector problems code. It contains the code for:

1. New Atom class API.
2. Line search update step for classic Frank Wolfe Algorithm.
3. Regularization of lp ball constraint domain.
4. Structured group constraint type in Jaggi's paper.
5. Support prune of OMP.
6. Full Corrective Update rule. (Update with atom norm constraint.)

Almost all the above codes are technologies to make the algorithms either converge faster or give better solutions for ill problems. I tried to design some examples in the `tests/` folder to make the above technologies to show their powers. However, it seems not possible to use small test problems to do that. So, the tests I currently wrote only check the convergence of the algorithms, which basically indicate that the implementation is correct. As Stephen sugggested, to keep one PR not too large to review, I will push all the comparisons codes for large scale problems in my next PR.

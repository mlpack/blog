@brief Matrix Completion Solver - Week 5
@author Chenzhe Diao
@page Chenzhe2017WeekFive Matrix Completion Solver - Week 5
@date 2017-07-07 22:00:00

@section Chenzhe2017WeekFive Matrix Completion Solver - Week 5

The work I did this week is mainly about matrix completion using FrankWolfe type solver.

In `src/mlpack/methods/matrix_completion/`, Stephen already implemented a matrix completion solver with `sdp` optimizer. However, Stephen suggests that it would be better to use FrankWolfe type optimizer or `sgd` optimizer for matrix completion. So I tried to add a new template class interface, which could let the users to choose between different optimizers. In fact, I think it could be an interesting project to compare different solvers on the same problem.

Currently, the FrankWolfe type solver for atom domain problem follows OMP fashion. That is, the update step searches the solution in the space spanned by all current atoms. This update step only cares about sparsity of the solution. [RaoShahWright](https://arxiv.org/abs/1404.5692) uses FrankWolfe type optimizers to solve atom domain problem with solution constrained by bounded atom norm. This would require a more complicated update step, where we need to solve a constrained problem, but it might give better results. I will implement this and compare.
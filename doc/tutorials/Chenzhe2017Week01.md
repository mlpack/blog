@brief Frank-Wolfe algorithm structure and OMP - Week 1
@author Chenzhe Diao
@page Chenzhe2017WeekOne Frank-Wolfe algorithm structure and OMP - Week 1
@date 2017-06-06 22:00:00

@section Chenzhe2017WeekOne Frank-Wolfe algorithm structure and OMP - Week 1

My project in this summer is initially about implementing the Frank-Wolfe algorithm and Orthogonal Matching Pursuit (OMP) algorithm, and to put them in the same code structure. This week, I built a structure of the FW type algorithm, and tried to make it flexible enough for all the variants in Jaggi's paper. I finished the special case to make it the same as OMP, and a simple hand-made test seems to indicate that the basic version of OMP is working now.

The other variants of FW type algorithm need more solvers, which I will add next. Such as an LP solver, a line search solver, optimizers in various atom domains, etc. I will try to add more of them in the following week.

Also, I am so glad to be coding for mlpack in this summer. It is quite pleasant to meet this cool community ^_^
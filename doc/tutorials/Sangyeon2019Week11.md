@brief Quantum Gaussian Mixture Models - Week 11
@author Sangyeon Kim
@page Sangyeon2019WeekEleven Quantum Gaussian Mixture Models - Week 11
@date 2019-08-10 12:00:00

@section Sangyeon2019WeekEleven Quantum Gaussian Mixture Models - Week 11

Current QGMM uses 'Lagrangian multiplier' for contrained optimization when training. In the validity of the objective function experiment, I checked that the optimization method works, but it didn't work sometimes for some cases in which the initial probabilities are almost zero. Therefore, my mentor recommends me to apply penalti method to Lagrangian multiplier to increase the stability and it is called the augmented Lagrangian multiplier. This week, I implemented the augmented Lagrangian mehod and conducted several experiments with it. Next week, I'll test the performance between the augmented Lagrangian method and normal Lagrange method. Also, I'll conduct some experiments to compare QGMM with GMM regarding the covergence to the clusters of the observations

Thanks for reading :)

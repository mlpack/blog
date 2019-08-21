@brief Quantum Gaussian Mixture Models - Week 11
@author Sangyeon Kim
@page Sangyeon2019WeekEleven Quantum Gaussian Mixture Models - Week 11
@date 2019-08-10 12:00:00

@section Sangyeon2019WeekEleven Quantum Gaussian Mixture Models - Week 11

Current QGMM uses 'Lagrangian multiplier' for contrained optimization when training. In the validity of the objective function experiment, I checked that the optimization method works, but it didn't work sometimes for some cases in which the initial probabilities are almost zero. Therefore, my mentor recommends to apply Lagrangian multiplier to the penalty method for stability and it is called the augmented Lagrangian multiplier. This week, I implemented the augmented Lagrangian mehod and conducted several experiments with it. Until now, it is stable, however, there is difference of the performance between them.

This week,  researches for comparing QGMM with GMM. With the 'Old faithful' data set, I calculated the convergence rates 
This week, I've researched the performance of the five clusters case. I generated the data set using mlpack GMM class. When training, the value 0 was good as an initial difference of phi. From some experiments, I figured out that as the difference neared zero, the two clusters showed a tendency to move away, while as the difference neared negative one, the two clusters tended to be close.
Lastly, I think it would be nice to take a closer look at the correlation between phi and other parameters to utilize the variation of phi more efficiently.

<center>
<b>[Visualization for the training process]</b>
<p>
<img src = "images/5_clusters_QGMM.gif" width = "640" height = "480" hspace = "10"/>
</p>
</center>
<br>

Thanks for reading :)

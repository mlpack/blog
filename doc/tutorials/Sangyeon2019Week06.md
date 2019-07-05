@brief Quantum Gaussian Mixture Models - Week 6
@author Sangyeon Kim
@page Sangyeon2019WeekSix Quantum Gaussian Mixture Models - Week 6
@date 2019-07-05 17:05:00

@section Sangyeon2019WeekSix Quantum Gaussian Mixture Models - Week 6

This week, I implemented QGMM. In this implementation, the goal is to minimize the objective function (16) in the paper. The mentor recommends me to try the objective function optimization with approximation constant like Lagrange multiplier.

\note The source code is at https://github.com/KimSangYeon-DGU/GSoC-2019/tree/master/Research/Optimization/Experiments

There are 3 python files and 1 dataset file. In the `qgmm_utils.py` has some utils for running QGMM and in the `draw_utils.py` is a utils function to draw the results of training. Lastly, the `main.py` is to test the performance of training. 

When I check the first implementation, I tried to minimize the NLL + lambda * sum of probabilities - 1, however, it didn't work.
\note The probabiltiies of QGMM is originally unnormalized, so I normalized the probabilities with the sum of probabilities with the help of the mentor

So, this time, I edited the codes again with left the probabilities unnormalized and changed the objective equation to NLL + lambda * sum of probabilities - S, where S is the actual sum of probabilities as it is unnormalized, not 1. As a result, it seems to work, but the performance was a bit unsatisfied on the side of covariance estimation.

<center>
<b>[Case1]</b>
<p>
<img src = "images/qgmm_with_old_faithful.gif" width = "640" height = "480" hspace = "10"/>
</p>
<br>
<b>[Case2]</b>
<p>
<img src = "images/qgmm_with_old_faithful2.gif" width = "640" height = "480" hspace = "10"/>
</p>
</center>
<br>
With the help of the mentor and readings, I think some better methods can be applied like variational approximation or other technologies.

Thanks for reading :)

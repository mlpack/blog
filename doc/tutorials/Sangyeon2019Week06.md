@brief Quantum Gaussian Mixture Models - Week 6
@author Sangyeon Kim
@page Sangyeon2019WeekSix Quantum Gaussian Mixture Models - Week 6
@date 2019-07-05 17:05:00

@section Sangyeon2019WeekSix Quantum Gaussian Mixture Models - Week 6

This week, I implemented QGMM. In this implementation, the goal is to minimize the objective function (16) in the paper. The mentor recommends me to try the objective function optimization with approximation constant like Lagrange multiplier.

\note The source code is at https://github.com/KimSangYeon-DGU/GSoC-2019/tree/master/Research/Optimization/Experiments

There are 3 python files and 1 dataset file. In the `qgmm_utils.py` has some utils for running QGMM and in the `draw_utils.py` is a utils function to draw the results of training. Lastly, the `main.py` is to test the performance of training. 

The objective equation to minimize is `NLL + lambda * sum of probabilities - 1`.

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

To make QGMM more robust, some methods are necessary to initialize parameters properly and solve positive definite covariance problems in Cholesky decomposition.

Thanks for reading :)

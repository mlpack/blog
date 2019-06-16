@brief Quantum Gaussian Mixture Models - Week 1
@author Sangyeon Kim
@page Sangyeon2019WeekTwo Quantum Gaussian Mixture Models - Week 2
@date 2018-06-08 23:00:00

@section Sangyeon2019WeekTwo Quantum Gaussian Mixture Models - Week 2

In the previous week, I made 3D probability space plottings. When I saw the plots, I could see the interference phenomena with phi.

This week, I did work on integral of probability of QGMM. Although the paper presents probability equation, I should check if the integral of the probability of QGMM becomes one.
At first, instead of the integral, I calculated the sum of the probability of the QGMM for approximation.
However, this project is a research, I should experiments the equations more accurately. So, thanks to my mentor, Sumedh, I looked into the Gaussian Integral

\note Gaussian Integral: https://en.wikipedia.org/wiki/Gaussian_integral

At the above link, the equation of Gaussian Integral is for single variate GMM, so I should derivate the equation for multivariate GMM.
The derivation of Gaussian Integral for multivariate GMM was succeeded, but I couldn't get the QGMM version.

This time, I tried to use the integration function of SciPy.

\note SciPy's integration function: https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html

Finally, after several attemps, I could get a proper result.

\note Source codes: https://github.com/KimSangYeon-DGU/GSoC-2019/blob/master/Research/Code/qgmm_2d_integral.py

Next week, I'll check and visualize the 2D probability space plot, and code the EMFit for QGMM in a Python version to see if the equation is valid.

Thanks for reading :)

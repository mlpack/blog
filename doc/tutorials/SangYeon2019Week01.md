@brief Quantum Gaussian Mixture Models - Week 1
@author SangYeon Kim
@page SangYeon2019CommunityBondingPeriod Quantum Gaussian Mixture Models - Week 1
@date 2018-06-01 23:00:00

@section SangYeon2019CBP Quantum Gaussian Mixture Models - Week 1

As I said in the Community Bonding Period report, the work of week 1 is to plot the 3D probability space to visualize and check the interference phenomena of QGMM more clearly.

To draw the 3D probability space, I implemented the GMM and QGMM Python codes.

\note You can check them at https://github.com/KimSangYeon-DGU/GSoC-2019/tree/master/Research/Probability_Space/codes

Below are the 3D probability spaces of GMM and QGMM.

[Classical GMM]
<p>
<img src = "images/classical_gmm.png" width = "600" height = "450" hspace = "10"/>
</p>

[Quantum GMM]
<p>
<img src = "images/qgmm_phis.png" width = "600" height = "218" hspace = "10"/>
</p>

At the above Quanmtum GMM images, we can see how much phis will impact on the distribution shape. Especially, when the phi is equal to 90 degree, the GMM and QGMM's probability space looks similar.

Next week, I will normalize the probability of QGMM and visualize it to check if differences between unnormalized and normalized distributions.

Thanks for reading :)

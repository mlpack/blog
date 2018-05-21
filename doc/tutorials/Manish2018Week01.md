@brief LMNN (via LRSDP) & BoostMetric Implementation - Week 1
@author Manish Kumar
@page Manish2018Week1 LMNN (via LRSDP) & BoostMetric Implementation - Week 1
@date 2018-05-21 07:00:00

@section Manish2018CommunityBondingPeriod LMNN (via LRSDP) & BoostMetric Implementation - Week 1

And the first week came to an end. It's been a week full of learning and overwhelming encounters. Over this period we had numerous reasoning sessions resulting in the conversion of whole SDP problem to a linear optimization problem.

Within these sessions, we tried to touch every aspect of LMNN problem as we move from deciding upon a formulation of its objective function in SDP standard form by including all the slack variables within objective to concluding over a linear objective function. Pros and cons of each formulation reasoned the basis of the conclusion.

Apart from discussions, we had decided over the inclusion of inequality constraints in SDP and changed the related modules accordingly, Though it might not be of use to current LMNN implementation anymore but may prove to be helpful in near future. 

Finally, coming to the current LMNN progress, we decided to have an initial implementation and progress further with the results. As of now, we are using `k` target neighbors and `k` impostors of each data point for calculation of objective and gradient. The results we got using L-BFGS optimizer were just fine, Hopefully, it will improve a lot starting from here. Last Night, I pushed a rough implementation of the same with little to no documentation ツ

Thanks to Ryan, the week brought a great amount of learning experience with it ☺
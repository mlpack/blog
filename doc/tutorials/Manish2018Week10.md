@brief LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 10
@author Manish Kumar
@page Manish2018Week10 LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 10
@date 2018-07-23 13:30:00

@section Manish2018Week10 LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 10

After concluding bounds for slack term PR [#1461](https://github.com/mlpack/mlpack/pull/1461) we move to other optimizations issues. Firstly we outset with impostors bounds PR [#1466](https://github.com/mlpack/mlpack/pull/1466) and tried to pick up where we left off. After solving some merge conflicts and other pending work, we noticed a rather disturbing behavior of KNN which was posing a problem for consistency of LMNN, this led to [#1470](https://github.com/mlpack/mlpack/pull/1470). But then Ryan came up with some good thoughts and we agree over sorting the KNN results on the basis of norms of datapoint as the viable solution. Hopefully,  [#1466](https://github.com/mlpack/mlpack/pull/1466)  is in its final stage and could be merge once PR [#1469](https://github.com/mlpack/mlpack/pull/1469) (dealing with step size decay updates in case we reach local minima) is merged.

Alongside this, we also took out some time for validating BoostMetric accuracy. For this, a rough implementation of the same was done. Apparently, the timings were pretty good (Maybe because it never recalculates impostors) but accuracy was more or less the same. We also made some adjustments for avoiding impostors recalculation over the LMNN to see if we get something similar to that. Evidently, both timings and accuracy were comparable to that of BoostMetric's.

Apart from this, Ryan took up the tree optimization issue [#1445](https://github.com/mlpack/mlpack/pull/1445) and have already worked it out. Hopefully, we will get it done soon enough.
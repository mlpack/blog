@brief LMNN (via LRSDP) & BoostMetric Implementation - Week 9
@author Manish Kumar
@page Manish2018Week09 LMNN (via LRSDP) & BoostMetric Implementation - Week 9
@date 2018-07-16 15:00:00

@section Manish2018Week09 LMNN (via LRSDP) & BoostMetric Implementation - Week 9

Last week, Bounds for LMNN were the topic of prime focus. We started off by debugging _[bounds for slack term](https://github.com/mlpack/mlpack/pull/1461)_ PR, eventually we found out a plenty of problems to be dealt with & quite a number of questions to be answered. Ultimately after answering all the issues in an orderly fashion, we were able to develop much more efficient and scalable bounds for the slack term of optimization problem. As a result, we now have a much higher pruning rate of inactive constraints. Apparantely we have seen that the bounds are highly dataset dependent, that being so, pruning can range from as low as 0 prunes to nearly pruning all the inactive constraints. Generally the number increases as we go up the iterations, making it more or less to a constant value.

We also carried out some correctness and speedups tests. And it is evident, that these bounds have overall added a significant value to LMNN efficiency.

Simultaneously, bounds for avoiding impostors recalculation were also put into effect. Fortunately, they didn't presented us with much of hurdles and are just about ready to get merged, though a good number of merge conflicts needs to be handle as [#1461](https://github.com/mlpack/mlpack/pull/1461) merges.

Hopefully, we will see LMNN growing a lot more in the upcoming days :)
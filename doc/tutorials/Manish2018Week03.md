@brief LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 3
@author Manish Kumar
@page Manish2018Week03 LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 3
@date 2018-06-04 10:00:00

@section Manish2018Week03 LMNN (via Low-Rank optimization) & BoostMetric Implementation - Week 3

Past week we have spent much time on debugging implementation. Now we have a fully functional LMNN method, together with quality output. We made quite a number of tests on some small-scale datasets, the likes of Iris and got considerable results w.r.t KNN accuracy on the same.

After getting a bit of satisfaction from the side of implementation, we decided to move on to optimization part. Here, Ryan suggested some good optimizations w.r.t running time which could definitely help things speedups. Some of the small ones were successfully completed, reducing earlier benchmarked time to almost its half as the value of `k` is increased (The comparison was made on Iris dataset).

Apart from debugging and optimization part, we are also in the process of benchmarking the implementation on Covertype dataset, which is taking quite a time due to its enormous size and decent dimensionality. Hoping, it will converge soon.

The coming week, we will mostly be focussing on optimization part and hopefully will do some in-depth significant optimizations.
@brief LMNN (via LRSDP) & BoostMetric Implementation - Week 6
@author Manish Kumar
@page Manish2018Week06 LMNN (via LRSDP) & BoostMetric Implementation - Week 6
@date 2018-06-24 12:30:00

@section Manish2018Week06 LMNN (via LRSDP) & BoostMetric Implementation - Week 6

Adding some accuracy metrics (like accuracy over 3-NN, 5-NN etc.) to the benchmarks was the first task performed during the week, After successfully pulling that off, we performed some of the benchmarks and the final results ([can be found here](https://github.com/mlpack/mlpack/pull/1407#issuecomment-398772089)) were overall pleasing. Seeing the promising outcomes, we decided to perform benchmarks over LMNN's Matlab implementation as well. The result of which, script for LMNN implementation by **[Laurens van der Maaten](https://lvdmaaten.github.io/drtoolbox/)** was added in addition to Mlpack's and Shogun's. Consequently, benchmarks results over LMNN were noted down at the same place. 

We also decided to merge the LMNN code in the current state and perform other possible optimizations over time. The remaining time of the week was spent on making this happen at the earliest. A part of the code was refactored, and some more optimization w.r.t memory and run-time were performed. Thanks to both Ryan & Marcus, we are now in the position to merge the code.
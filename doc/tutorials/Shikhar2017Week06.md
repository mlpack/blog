@brief Profiling for parallelization and parallel stochastic optimization methods - Week 6
@author Shikhar Bhardwaj
@page Shikhar2017WeekSix Profiling for parallelization and parallel stochastic optimization methods - Week 6
@date 2017-07-12 20:08:00

@section Shikhar2017WeekSix Profiling for parallelization and parallel stochastic optimization methods - Week 6

This week was spent in further research into testing methods for the implementations in 
the PR([#1037](https://github.com/mlpack/mlpack/pull/1037)). Several runs and experiments are
in the Gists linked below : 

 * [Sparse Matrix completion synthetic run #1](https://gist.github.com/shikharbhardwaj/27685f5cbb5d3a465993405b8be3fc6e)
 * [Sparse Matrix completion synthetic run #2](https://gist.github.com/shikharbhardwaj/e487fff3f8d6d67a8a02c724991797ac)
 * [Sparse Matrix completion run on sampled data](https://gist.github.com/shikharbhardwaj/91fe7e5984f32ccd95b78c99c9fcbf20)
 * [Sparse SVM run on RCV1 dataset](https://gist.github.com/shikharbhardwaj/080c7a1503f19e1073926365a9729b9b)

Also, I have started with the initial implementation of another optimizer method, Stochastic 
Co Ordinate descent, and would open up a PR soon with the additions.
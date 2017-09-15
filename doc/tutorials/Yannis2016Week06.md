@brief Multiprobe LSH Finalized, LSH Parallelization - Week 6
@author Yannis Mentekidis
@page Yannis2016WeekSix Multiprobe LSH Finalized, LSH Parallelization - Week 6
@date 2016-07-05 20:20:20

@section Yannis2016WeekSix Multiprobe LSH Finalized, LSH Parallelization - Week 6

I started this week by making the final changes to Multiprobe LSH - I fixed the style issues, corrected some bugs, and implemented or re-implemented some tests.

As I've discussed before, LSH, and by extension Multiprobe LSH, is quite a hard algorithm to test, because it is randomized and furthermore doesn't give any practically usable guarantees on the rate of its error. 

So while fixing the documentation and style, I ran into a few bugs in the code. What was worse, I found bugs in my testing code that made it too tolerant of mistakes. So, I re-implemented all the deterministic tests for Multiprobe LSH.

Before the end of the week, Ryan merged my Pull Request to the master branch, so now Multiprobe LSH is available for users of the github build.

I continued my week by trying to implement parallel versions of `arma::find()` and `arma::unique()`. I failed miserably, for two reasons: (a) because these functions are aggressively optimized, and (b) because there's a big overhead on lock contention and shared memory coherency, so big that the parallel version ends up being slower than the sequential one.

In the end, we are probably going to go only with the first and simpler parallelization of the querying process - where an n-core machine can process n queries in parallel, which is the only thing I have attempted that actually showed any improvement.

In related news, I merged the Multiprobe code into the OpenMP code branch, so AppVeyor could build the Pull Request and tell us if it fails in other platforms. Things look good, which is good news :)
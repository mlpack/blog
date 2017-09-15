@brief FrankWolfe in atom domain for constrained problem - Week 6
@author Chenzhe Diao
@page Chenzhe2017WeekSix FrankWolfe in atom domain for constrained problem - Week 6
@date 2017-07-16 08:00:00

@section Chenzhe2017WeekSix FrankWolfe in atom domain for constrained problem - Week 6

As I mentioned in the blog last week, the problem I focused on this week is the FrankWolfe type solver in atom domain for constrained problem. The update step now involves a projected gradient solver onto the l1 ball spanned by previous atoms. According to [duchi2008efficient](http://dl.acm.org/citation.cfm?id=1390191), this is performed efficiently in `O(nlog(n))` steps. The implementation of this step is basically done.

I will merge my current code with previous [PR](https://github.com/mlpack/mlpack/pull/1041), in the coming week. Also, I think I can perform some serious tests on large scale problems. I will try matrix completion tests in the following week. Hopefully, I can get some comparison plots to show.
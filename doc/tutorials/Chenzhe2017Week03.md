@brief Sparse Optimization with regularization and support truncation - Week 3 + 4
@author Chenzhe Diao
@page Chenzhe2017WeekThreeFour Sparse Optimization with regularization and support truncation - Week 3 + 4
@date 2017-06-27 16:00:00

@section Chenzhe2017WeekThreeFour Sparse Optimization with regularization and support truncation - Week 3 + 4

Sorry that I didn't update blog last week. During these two weeks, I was working on techniques to make the FrankWolfe type sparse optimization algorithm to converge faster.

The first technique is to have regularization on the atom domain. The regularization parameter could be optionally provided by the user. Ideally, it should be equal to the l2 norm of the atoms, or the l2 norm of the columns of the sensing matrix. The second technique is the support truncation, which is mentioned in [RaoShahWright](https://arxiv.org/abs/1404.5692) and [BoydSchiebingerRecht](https://arxiv.org/abs/1507.01562).

Now the code is ready to be more seriously tested with larger problems such as matrix completion. I will implement this in the coming week. Also, [RaoShahWright] paper also talks about constrained problem in this setting, which is also interesting to be implemented.
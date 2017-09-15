@brief Dataset and Experimentation Tools - Week 9
@author Keon Kim
@page Keon2016SWeekNine Dataset and Experimentation Tools - Week 9
@date 2016-07-26 16:00:00

@section Keon2016SWeekNine Dataset and Experimentation Tools - Week 9

This week, pull request for DatasetMapper & Imputer is merged. I thank Zoq, Rcurtin and especially, Tham for all the feedbacks.
I feel like I gave them more work than I did.

DatasetMapper & Imputer

1) I added Impute() function that applies imputation to all dimensions in the given matrix.

2) I made a program called mlpack_preprocess_check (previously called mlpack_preprocess_verify in this blog).
I will make a pull request after adding comments and docs.

Descriptive Statistics

1) After discussing a little how to manage statistics class, I put it into the preprocess/ folder
because it will only be used for preprocess_describe command line program. It's sole purpose is to
provide cleaner interface.
I might even consider removing the class because the code length became too large for a small program.
I will make this decision as soon as possible and make a pull request next week.

2) I optimized some functions in statistics class.

3) changed class Statistics to DescriptiveStatistics to be more specific.

Documentations

1) I made lists of algorithms implemented in mlpack in README.md and updated to date.

Other

1) I replaced cross_validation's split function with data::Split() inside dt_utils.
I will make a pull request regarding this after a few performance checks.
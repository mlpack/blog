@brief Augmented Recurrent Neural Networks - Week 9
@author Konstantin Sidorov
@page Konstantin2017WeekNine Augmented Recurrent Neural Networks - Week 9
@date 2017-08-02 21:09:00

@section Konstantin2017WeekNine Augmented Recurrent Neural Networks - Week 9

As we're entering into the final month of the GSoC '17, the work is naturally heating up. The main feature of the week was the wrap-up of the long-running benhchmarking PR.

Aside of various style issues, there was also a fix of the non-trivial uniform generation bug (courtesy of Ryan Curtin for pointing this one out). The problem was that in `AddTask` and `CopyTask` generating uniform length and sampling a sequence was *not* equivalent to sampling uniformly from the sample space of all sequences. For example, there are 2 sequences of length 1 but 1024 sequences of length 10 - correspondingly, the latter set should be more frequent than the former set.
@brief Augmented Recurrent Neural Networks - Week 10
@author Konstantin Sidorov
@page Konstantin2017WeekTen Augmented Recurrent Neural Networks - Week 10
@date 2017-08-10 11:07:35

@section Konstantin2017WeekTen Augmented Recurrent Neural Networks - Week 10

Since my benchmarking PR was finally merged, I started working full-time on implementing HAM unit. Of course, this is a very complicated task, so it also deserves some segmentation.

Currently we have (implicitly) agreed on these parts:

- implementing `TreeMemory` (*status*: almost done, but some new changes don't compile);
- implementing forward pass of `HAMUnit` (*status*: there is some plausible code, but we can't really test it due to the `TreeMemory` bug);
- testing forward pass of `HAMUnit` (*status*: all components for test case are ready and waiting for the first two stages to resolve);
- implementing and testing backward pass of `HAMUnit` (*status*: there are some ideas on how to implement it - more in the final two weeks).

As you can see, there is a lot of ongoing work - more details to follow in the final two weeks.
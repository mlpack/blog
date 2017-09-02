@brief Deep Reinforcement Learning Methods - Week 4
@author Shangtong Zhang
@page Shangtong2017WeekFour Deep Reinforcement Learning Methods - Week 4
@date 2017-06-24 11:00:00

@section Shangtong2017WeekFour Deep Reinforcement Learning Methods - Week 4

This week I finished the update of optimizer API. I think the PR is now ready to merge. Thanks Ryan for helping me with some complicated optimizers. I also worked on exposing `Forward` and `Backward` of FFN, and the support of real batch mode. To do this, we need to look into all the `LayerType` and make sure they are compatible with matrix (before this we only use vector). Thanks Marcus for helping me with conv related layers. There is also another PR about this, which is almost ready to merge. I also investigated OpenMP, it's really amazing that OpenMP doesn't support shared class memeber variable -- to do this, I have to copy the class member variable to a new local variable http://forum.openmp.org/forum/viewtopic.php?f=3&t=553. I also learned some synchronization mechanism of OpenMP. In addition I noticed in the mailing list that some guy is going to implement HOGWILD, but I don't think my async RL will benefit much from that -- the key point of async RL I think is async agents rather than async gradient computation.

BTW I will have a two-week break starting from tomorrow due to DLSS/RLSS in Montreal. During that period I'm afraid I can't work on new PRs. But I think I can still work on the two existing PRs to fix some issues if necessary and make sure they get merged before I'm back.
@brief Deep Reinforcement Learning Methods - Week 6
@author Shangtong Zhang
@page Shangtong2017WeekSix Deep Reinforcement Learning Methods - Week 6
@date 2017-07-22 21:00:00

@section Shangtong2017WeekSix Deep Reinforcement Learning Methods - Week 6

This week I continued working on async one-step q-learning. The major challenge this week is to make the test case success in the Travis CI. It's quite tricky. I tuned the architecture of the network and hyper-parameters, it only costs 2s in my mac but still costs almost 10 minutes in the server, even I reduce the amount of the workers to 4. So I have to try pre-trained network. It's weird that if I set the amount of workers to 0 and only have test process with the pre-trained converged network, it will fail (this only happens in ther server). So I have to set the amount of the workers to 1. Although I don't know why it works. `TrainingConfig`class is quite useful in terms of passing in hyper-parameters, however it doesn't conform with the newest mlpack API style. But I assume rl methods won't interact with `CrossValidation` helper, so I guess the newest API style won't influence my project much. The PR for async one step q-learning is almost ready, hopefully it can be merged within 2 days.
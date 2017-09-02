@brief Deep Reinforcement Learning Methods - Week 1
@author Shangtong Zhang
@page Shangtong2017WeekOne Deep Reinforcement Learning Methods - Week 1
@date 2017-06-02 20:00:00

@section Shangtong2017WeekOne Deep Reinforcement Learning Methods - Week 1

This post contains work that has been done until now from about Feb.

This Deep RL project will implement DQN (and its variants) and several asynchronous deep rl methods. Until now basic DQN (ready for classical tasks like CartPole) has been finished and is being merged. Skeleton of async methods is also finished.

I have surveyed bunch of DQN and A3C implementations in TensorFlow and PyTorch to find the best practice. Furthermore, I implemented DQN, async Q-learning, async n-step Q-learning and async Sarsa from scratch in PyTorch. This highly modularized PyTorch implementation can be found [here](https://github.com/ShangtongZhang/DeepRL). All these implementations work well with CartPole. And I also tested DQN with BreakOut and A3C with Pong.

The future work will mainly be porting my PyTorch implementation to mlpack.
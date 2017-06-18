Title: Deep Reinforcement Learning Methods - Week-2 Highlights
Date: 2017-06-10 20:00:00
Tags: gsoc
Author: Shangtong Zhang

This week I continue working on the DQN PR, and finally make it merged. It's amazing that for CartPole with Double DQN, a samll network with only 20 hidden units is better than a bigger one. I also worked on updating optimizer API. It's really a huge project, with much much more work than I expected. During this process, I started to miss pointer -- pointer parameter can have default value but non-const reference parameter cannot. So I have to write overloaded function to allow default parameter. It is still confusing me why c++ doesn't allow binding a rvalue to a non-const lvalue reference, I think sometimes we do need this feature.

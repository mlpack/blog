Title: Deep Reinforcement Learning Methods - Summary 
Date: 2017-08-21 22:00:00 
Tags: gsoc 
Author: Shangtong Zhang

This blog is the summary of my gsoc project -- implementation of popular deep reinforcement learning methods.
During this project, I implemented deep (double) q learning, asynchronous one/n step q learning, asynchronous one step sarsa and asynchronous advantage actor critic (in progress), as well as two classical control problems, i.e. mountain car and cart pole, to test my implementations.

# Introduction

My work mainly locates in `methods/reinforcement_learning` folder

- `q_learning.hpp`: the main entrance for (double) q learning

- `async_learning.hpp`: the main entrance for async methods

- `training_config.hpp`: wrapper for hyper parameters

- `environment`: implementation of two classical control problems, i.e. mountain car and cart pole

- `policy`: implementation of several behavior policies

- `replay`: implementation of experience replay

- `network`: wrapper for non-standard networks (e.g actor critic network without shared layers)

- `worker`: implementation of async rl methods

Refactoring of existing neural network components is another important part of my work

- Detachment of `module` and `optimizer`: This influences all the optimizers and most test cases.

- PVS convention: Now many of mlpack components comply with `pass-by-reference`, which is less flexible. I proposed the idea of `pass-by-value` in combination with `std::move`. This is assumed to be a very huge change, now only newly added components adopts this convention. Ryan is working on old codebase. 

- Exposure of `Forward` and `Backward`: Before this we only have `Predict` and `Train`, which may lead to duplicate computation in some case. By the exposure of `Forward` and `Backward`, we can address this issue.

- Support for shared layers: This is still in progress, however I think it's very important for A3C to work with Atari. We proposed the `Alias` layer to address this issue. This is also a huge change, which will influence all the visitors.

- Misc update of old APIs.

Detailed usage can be found in the two test cases: `async_learning_test.cpp` and `q_learning_test.cpp`. You can run the test cases by `bin/mlpack_test -t QLearningTest` and `bin/mlpack_test -t AsyncLearningTest`.

In total, I contributed following PRs:

- [Implementation of Alias layer](https://github.com/mlpack/mlpack/pull/1091)

- [Async n-step q-learning and one step sarsa](https://github.com/mlpack/mlpack/pull/1084)

- [Implement a framework of DQN and asynchronous learning methods](https://github.com/mlpack/mlpack/pull/934)

- [Implementation of async one step q-learning](https://github.com/mlpack/mlpack/pull/1064)

- [Add aggregated policy for async rl methods](https://github.com/mlpack/mlpack/pull/1056)

- [Support batched forward and backward for FFN](https://github.com/mlpack/mlpack/pull/1034)

- [Update Optimizer API](https://github.com/mlpack/mlpack/pull/1032)

- [Add new API for some optimizers](https://github.com/mlpack/mlpack/pull/1026)

- [Basic DQN](https://github.com/mlpack/mlpack/pull/1014)

- [Add epsilon greedy policy for DQN](https://github.com/mlpack/mlpack/pull/1012)

- [Add random replay for DQN](https://github.com/mlpack/mlpack/pull/1001)

- [Fix a bug in gaussian init](https://github.com/mlpack/mlpack/pull/1000)

- [Refactor FFN](https://github.com/mlpack/mlpack/pull/995)

- [Implement two classical control problems for testing reinforcement learning method](https://github.com/mlpack/mlpack/pull/989)

- [Fix bug of variadic template parameters of Optimizer](https://github.com/mlpack/mlpack/pull/967)

# Highlights

The most challenging parts are:

- Making amount of threads independent with amount of workers in async rl methods: This is really a fantastic idea. To my best knowledge, I haven't seen any public implementation of this idea. All the available implementations in the Internet simply assume them to be equal. To achieve this, we need to build a worker pool and use `step` instead of `episode` as a job unit.

- `Alias` layer: This blocked me most and is still blocking me. We need a deep understanding of `armadillo` memory management, `boost::variant` and `#include` directives.

# Future Work

Apparently RL support of MLPack is far from complete. Supporting classical control problems is an important milestone -- we are almost there. However we are still far from the next milestone -- Atari games. At least we need GPU support, infrastructure of basic image processing and an effective communication method with popular simulators (e.g. OpenAI gym, ALE).

# Acknowledgment

I thank Marcus for his mentorship during the project and detailed code review. I also want to thank Ryan for his thoughtful suggestions. I also appreciate the generous funding from Google.

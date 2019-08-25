@brief PPO - Summary
@author Xiaohong
@page Xiaohong2019Summary Proximal Policy Optimization method - Summary
@date 2019-08-23 10:30:09

@section Xiaohong2019Summary Proximal Policy Optimization method - Summary


Time flies, the summer is coming to end, we come to the final week of GSoC.
This blog is the summary of my GSoC project -- implementation of one of the
most promising dee reinforcement learning method. During this project, I
implemented policy optimization method, one classical continuous task, i.e.
Lunar lander, to test my implementation. Also my pull request for prioritized
experience replay was merged into master.


# Introduction

My work mainly locates in `methods/reinforcement_learning`, `methods/ann/
loss_functions` and `methods/ann/dists` folder

- `ppo.hpp`: the main entrance for proximal policy optimization.

- `ppo_impl.hpp`: the main implementation for proximal policy optimization.

- `lunarlander.hpp`: the implementation of the continuous task.

- `prioritized_replay.hpp`: the implementation of prioritized experience replay.

- `sumtree.hpp`: the implementation of segment tree structure for prioritized experience replay.

- `environment`: the implementation of two classical control problems, i.e. mountain car and cart pole

- `normal_distribution.hpp`: the implementation of normal distribution which accept `mean` and `variance`
                             to construct distribution.

- `empty_loss.hpp`: the implementation of empty loss which used in proximal policy optimization class,
                    we calculate the loss outside the model declaration, the loss does nothing just
                    backward the gradient.


In total, I contributed following PRs, most of the implementations are combined into the single Pull request in
proximal policy optimization.

[Proximal Policy Optimization](https://github.com/mlpack/mlpack/pull/1912)

[Prioritized Experience Replay ](https://github.com/mlpack/mlpack/pull/1614)

[Change the pendulum action type to double](https://github.com/mlpack/mlpack/pull/1931)

[Fix typo in Bernoulli distribution](https://github.com/mlpack/mlpack/pull/1730)

[remove move() statement in hoeffding_tree_test.cpp](https://github.com/mlpack/mlpack/pull/1914)

[minor fix up](https://github.com/mlpack/mlpack/pull/1762)

# Highlights

The most challenging parts are:

- One of the most challenging parts of the work is that how to calculate the surrogate loss for updating
the actor-network, it is different from the updater for the critic network which can be optimized by
regression on mean square error. The actor-network is optimized by maximizing the  PPO-clip objective,
it is a little difficult to implement it like the current loss function which calculated by passing
target and predict parameters, so I calculate it outside the model and the declaration of the model is
passed into the empty loss function. All the backward process except the model part are calculated by
my implementation, like the derivation to the normal distribution's mean and variance.

- Another challenging part of the work is that I implement the proximal policy optimization in the continuous
environment, the action is different from the discrete environment. In the discrete environment, the
agent just output one dimension's data to represent the action, while in the continuous environment, the agent
action prediction is more complicated, the common way to achieve predicting the agent action is to predict
a normal distribution, then use the normal distribution to sample an action.

- Also there are other challenging parts of the work, such as tuning the neural network to make the agent
to work. This blocks me now so that I need to tune more parameters to pass the unit test. This part is also
a time-consuming process.


# Future Work

The pull request of proximal policy optimization is still underdeveloped due to the tuning
parameters for the unit test, but it will be fixed soon.

PPO can be used for environments with either discrete or continuous action spaces, so another future work
will be to support the discrete action spaces, even though it is easy than the continuous task.

In some continuous environment task, the dimensions of action are more one, we need to handle this situation.

# Acknowledgment

A great thanks to Marcus for his mentorship during the project and detailed code review. Marucs is helpful and
often tell me that do not hesitate to ask questions. He gives me great help when something blocked
me. I also want to thank Ryan's response in IRC even though at midnight. The community is kind since
the first meeting, we talk about a lot of things which contain different areas. Finally, I also appreciate t
he generous funding from Google. It is a really good project to sharpen our skills. I will continue to commit
to mlpack and make the library more easy to use and more powerful.

Thank for this unforgettable summer session.
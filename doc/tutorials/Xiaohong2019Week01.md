@brief PPO - Week 1
@author Xiaohong
@page Xiaohong2019Week1 Proximal Policy Optimization - Week 1
@date 2019-06-02 18:39:10

@section Xiaohong2019Week 1 Proximal Policy Optimization - Week 1

The goal of my summer project is to implementing the proximal policy
optimization algorithm (PPO). PPO is a new family of policy gradient
methods for reinforcement learning, which alternate between sampling
data through interaction with the environment, and optimizing a
“surrogate” objective function using stochastic gradient ascent.

For the first week, I finished the review comments in PER. such as,
changing all variable name to camel style, adding parameters description
and fixing the code style problem. I add the basic skeleton layout for
the loss function, and begin to add BOOST test case for the PPO
algorithm. Besides, I fix the compiler warning when building the mlpack
on the fly.

For the original schedule:

1: Reading related research papers to get a more robust view of the problem.
    Finished some paper reading, such as the original [PPO paper](https://arxiv.org/pdf/1707.06347.pdf).
    Finished some article reading, such as [Spinning Up PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html#references).

2: Discussing with mentors and get a final idea on how to approach the problem.
    Having an original idea and will build up the project step by step.

3: Setting up the development environment, get familiar with mlpack's coding practices.
    Already done when contributing to the mlpack project.

4: Writing a skeleton layout of the algorithm to implement.
    Writing a basic skeleton for the loss function.

I am trying to make the code more compatible with the mlpack API, so
maybe some late with what I expect. I will devoted more time on it next week.
Thanks for reading.

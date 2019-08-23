@brief NEAT & Multiobjective Optimization - Summary
@author Rahul Ganesh Prabhu
@page Rahul2019Summary NEAT & Multiobjective Optimization - Summary
@date 2019-08-20 01:30:00

# Overview

The aim of my project for Google Summer of Code 2019 was to implement NeuroEvolution of Augmenting Topologies (NEAT) in mlpack based on Kenneth Stanley's paper [Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf). I would also implement support for "phased searching", a searching scheme devised by Colin Green to prevent genome bloat when training NEAT on certain complex tasks.

Besides this, my project aimed to create a framework for multi-objective optimization within mlpack's optimization library ensmallen. This would involve the implementation of several test functions and indicators, as well as an optimizer, NSGA-III.

# Implementation

#### NEAT

NeuroEvolution of Augmenting Topologies (NEAT) is a genetic algorithm that can evolve networks of unbound complexity by starting from simple networks and "complexifying" through different genetic operators. It has been used to train agents to play Super Mario World and generate "genetic art".

I implemented NEAT in [PR #1908](https://github.com/mlpack/mlpack/pull/1908). The PR includes the entire implementation including phased searching, associated tests and documentation. NEAT was tested on:

* The XOR test, where it's challenge was to create a neural network that emulated a two input XOR gate. NEAT was able to solve this within 150 generations with an error less than 0.1.

* Multiple reinforcement learning environments implemented in mlpack.

* The pole balancing task in OpenAI Gym. This was done using the [Gym TCP API](https://github.com/zoq/gym_tcp_api) implemented by my mentor, Marcus Edel. A short video of the trained agent can be seen [here](https://gym.kurg.org/openaigym.video.9.40957.video000000.mp4).

* The double pole balancing test. I implemented this as an addition to the existing reinforcement learning codebase. NEAT performed well on both the Markovian and non-Markovian versions of the environment.

The pull request is rather large and is still under review.

#### Multi-objective optimization

Multi-Objective Optimization is an area of multiple criteria decision making that is concerned with mathematical optimization problems involving more than one objective function to be optimized simultaneously. NSGA-III (Non-dominated Sorting Genetic Algorithm) is an extension of the popular NSGA-II algorithm, which optimizes multiple objectives by associating members of the population with a reference set of optimal points.

I implemented support for multi-objective optimization in [PR #120](https://github.com/mlpack/ensmallen/pull/120). This PR includes:

* An implementation of NSGA-III. This code is still being debugged and tested.

* Implementation of the DTLZ test functions.

* Implementation of multiple indicators, including the epsilon indicator and the Inverse Generational Distance Plus (IGD+) indicator.

* Associated documentation.

#### Other work

Besides the work explicitly stated in my project, I also made some smaller changes and additions in the reinforcement learning codebase. This includes:

* Implementation of both a Markovian and non-Markovian (velocity information not provided) version of the double pole balancing environments (see [#1901](https://github.com/mlpack/mlpack/pull/1901) and [#1951](https://github.com/mlpack/mlpack/pull/1951)).

* Fixed issues with consistency in mlpack's reinforcement learning API, where certain functions and variables were missing from some environments. Besides this, the environments now have an option to terminate after a given number of steps. See [#1941](https://github.com/mlpack/mlpack/pull/1951).

* Added QLearning tests wherever necessary to prevent issues with consistency in the future. See [#1951](https://github.com/mlpack/mlpack/pull/1951).

# Future Work

* Get the NEAT PR merged.
* Finish testing and debugging the NSGA-III optimizer.
* Write more indicators for multi-objective optimization.

# Final Comments

I would like to thank my mentors, **Marcus Edel** and **Manish Kumar** for all their help and advice, as well as bearing with me through the multiple technical difficulties I faced during this summer. I'd also like to thank all the other mentors and participants for their support. I hope to continue to contribute to this community in the future, and look forward to the same.

If anyone is interested in seeing my weekly progress through the program, please see [my weekly blog](http://www.mlpack.org/gsocblog/RahulGaneshPage.html).

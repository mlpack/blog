Title: Deep Reinforcement Learning Methods - Week-5 Highlights
Date: 2017-07-15 22:00:00
Tags: gsoc
Author: Shangtong Zhang

This week I started to work on implementing async deep rl methods. Async one step q-learning is the first. I had an exaustive discussion with Marcus about the best design pattern and finally made it with policy based design. I succeeded in implementing async one step q-learning with OpenMP, and I believe my framework can be easily extended to async n-step q-learning, async one-step Sarsa. However, for A3C, extra effort is expected. I tested my implementation in Cart Pole domain, it works well and is very stable. However it doesn't work well in Travis CI. My understanding is the machine in Travis CI doesn't have as good performance as my laptop. And this test needs 18 threads simutaneously, if the parallelization of the machine is bad, the performance of the agent will be heavily hurt. I'm still seeking for solution for this.

Title: Deep Reinforcement Learning Methods - Week-7 Highlights
Date: 2017-07-29 18:00:00
Tags: gsoc
Author: Shangtong Zhang

This week I was still working on async one-step q-learning. Ryan gave an important feedback that we should separate number of threads and number of workers. In asynchronous rl methods, it's important that we have enough workers to gain enough uncorrelated experience. In general, the number of threads is equal to the number of workers. But sometimes user may not want the program to occupy all the cpu resources, i.e. they want to use less threads than workers. This is indeed an important user case especially in some resource-limited devices. To address this issue, we have to break down the `Episode` of workers into `Step` and build up a task pool and a thread pool. OpenMP task is a perfect feature for this, but I found MSVC doesn't support OpenMP task for now. So I applied some tricks to make it work with parallelized for-loop. And this design also solved the problem that the test case will run too long in Travis CI. So now we no longer need a pre-trained network. I believe this indeed makes the code more robust to possible future change.

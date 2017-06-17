Title: Deep Reinforcement Learning Methods - Week-2 Highlights
Date: 2017-06-10 20:00:00
Tags: gsoc
Author: Shangtong Zhang

This week I mainly worked on merging my DQN PR. During the merge process, many new ideas came out. For example, we decided to use pass-by-value convention to replace old const lvalue reference and rvalue reference overloads for API. This will give user more flexibility and make mlpack codebase more compact. We also decided to totally separate model instance and optimizer instance, which is necessary for asynchronous deep RL methods and is also helpful for the hyperparameter tuner project.

Furthermore, I realized my old design for the abstract interface of asynchronous methods has a fatal disadvantage -- it cannot support LSTM layer for A3C. So I totally redesigned the abstract interface and tested my new design with PyTorch with Atari games. I also tried some interesting things for async deep RL methods like non-centered target network, target network without lock.

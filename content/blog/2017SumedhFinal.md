Title: Neural Turing Machines : Week 5
Date: 2017-07-06 14:00:00
Tags: gsoc
Author: Sumedh Ghaisas

Another amazing year of GSOC.
This year was more exciting that my previous experiences.
My major contribution in this year, was the Neural Turing Machine, or NTM.
NTM is a neural network with additional external memory.
As the entire architecture is end-to-end differentiable, NTM is able to learn tasks which require memory storage.
Such as, reproducing the given sequence, sorting the sequence and so on.
The code is complete and can be found in PR [#1072](https://github.com/mlpack/mlpack/pull/1072).

I have also implemented GRU as part of my project this year.
While implementing GRU, the current recurrent neural network framework is extended to support variable length sequences.
This involved making changes to current LSTM implementation as well.
Given such changes, both LSTM and GRU are tested with variable length reber grammar sequences.
As an interesting side project, I added something called recursive reber grammar for testing.
Recursive reber grammars are basically reber grammar but they are recursiveky embedded in themselves.
Embedded reber grammar is a special case of recursive reber grammar where the recursive depth is set to 1.
Its good to see that both LSTM and GRU passes recursive reber grammar tests with various recursive depths.
Although I have noiced that the cell state size required to pass the tests differes with recursive depth of the grammar.
It will be a nice expeiment to see what is actually going on in cell state.
Is LSTM/GRU, storing the depth as a stack? That would be really cool.
All this code is already merged but can be accessed by PR [#1018](https://github.com/mlpack/mlpack/pull/1018).

As of now, I am yet to complete the implementation of batch nomalization.
Before batch normalization can be added to the framework, the framework should be refactored to support batch mode.
A lot of people are helping to achieve this task.
Even though the program is over, I will keep working on this issue and complete batch normalization as pat of my project.

I would like to congratulate Marcus and Ryan, my mentors, for surviving this summer project wih me :P I know how hard this must have been :)
Thak you for all your support and guidance.
Its been more than 4 years since I joined MLPACK community and its been a wonderful journey.
I hope the coming years will bring more fun...

Title: Collaborative filtering package improvements : Week 1 Highlights
Date: 2017-06-06 14:00:00
Tags: gsoc
Author: Sumedh Ghaisas

This summer I will working o implementing The Neural Turing Machine(NTM) architecture in MLPACK.
Although at the start, while I get myself familiarized with the mathematics behind NTM, I will be implementing a Grated Recurrent Unit(GRU) and Batch Normalization Layer.
Both of these layers are chosen in a way to help test NTM to a higher degree.
NTM requires a recurrent central processing unit which can be implemeted using LSTM or GRU.
Batch normalization will help in stable learning of this central unit.

At the end of Week 1, the primary GRU implementation is over is minimal testing.
With some more documentation and GRUspecific tests the GRU implementation will hopefully will be over by this week.
Unlike my previous attempt at GSOC, I tend to follow my given timeline this year. :)

For the part of batch normalization, someone else has already beaten me to it :P
With some minor code changes and by adding the support for convolutional layers the batch normalization should be complete.
Adding support for convolutional layers might turn out to be tricky. 
So this week will also be spent in discussing the API for that.

Happy coding everyone...

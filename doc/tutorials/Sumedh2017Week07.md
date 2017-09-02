Title: Neural Turing Machines : Week 7-8
Date: 2017-07-06 14:00:00
Tags: gsoc
Author: Sumedh Ghaisas

Completed Memory Head which is most essential part of Neural Turing Machine Framework.
Memory Head is tested for gradient check and forward pass check.
I have also started working working on NTM framework, and due to high complexity
I am adding 1 operation at a time and making sure the gradients still pass.
For Memory Head implementation I will need backport some Armadillo functions which
is also a task for coming week.

For the PR of GRU, the only thing remaining is the shift to batchSize version.

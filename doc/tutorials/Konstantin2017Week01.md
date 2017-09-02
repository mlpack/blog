@brief Augmented Recurrent Neural Networks - Week 1
@author Konstantin Sidorov
@page Konstantin2017WeekOne Augmented Recurrent Neural Networks - Week 1
@date 2017-06-07 17:15:34

@section Konstantin2017WeekOne Augmented Recurrent Neural Networks - Week 1

This summer, I will be working on the implementation of neural network models augmented with some additional memory structures (hence the name). One notable example of such model is [Neural Turing Machine](http://arxiv.org/abs/1410.5401), which is a straightforward combination of the Turing machine idea and the idea of using "soft" action policies (probabilistic, in contrast to more traditional "hard" policies, which only choose action but don't show any degree of uncertainty). It is reported to be able to handle some *very* simple algorithmic tasks (e.g., copying the sequence) rather well. Of course, there are move advanced models that offer faster convergence and are able to learn in a more complex environments.

During the Community bonding stage and Week 1 I have implemented benchmarking utilities for this kind of models. For instance, I implemented three basic tasks (classes that generate data for specific problems), namely:

- `CopyTask`: given a bit sequence, copy it a required number of times. For example, if the task requires to repeat it three times, the input/output pair may look like this: `001 -> 001001001`.
- `SortTask`: given a sequence of *n*-bit numbers, generate a sequence with the same numbers, but ordered from the smallest to the biggest. For example (*n*=3): `[000, 111, 101, 100, 011] -> [000, 011, 100, 101, 111]`.
- `AddTask`: given a sequence representing *two* binary numbers (separated with a special symbol), generate a sequence representing their sum. For example, `0010+1111 -> 10001`, where `+` is some special value used to separate two numbers.

The grand total and the preceding discussion can be seen [here](https://github.com/mlpack/mlpack/pull/1005).

Next up: during Week 2 LSTM & GRU baseline will be implemented. The implementation and preformance test results will be reported here next Wednesday.
Title: Augmented Recurrent Neural Networks: Summary
Date: 2017-08-23 19:33:54
Tags: gsoc, rnn, neural network, lstm
Author: Konstantin Sidorov

This post is the summary of my GSoC work.

# Relevant pull requests

* [Augmented RNN models - benchmarking framework](https://github.com/mlpack/mlpack/pull/1005) - merged. This PR contains documented and tested benchmarking classes for simple "algorithmic" tasks - `CopyTask`, `AddTask`, `SortTask`.
* [Added LSTM baseline model with copy task benchmark](https://github.com/mlpack/models/pull/1) - paused. This PR contains the working implementation for LSTM model working on the three tasks from the previous PR.
* [Adding optimization features not related with my GSoC project](https://github.com/mlpack/mlpack/pull/1070) - merged. This PR contains gradient clipping implementation and implementation of `CrossEntropyError` function. The name turned out to be a misnomer - the former helped to work around the gradient explosion problem, and the latter one accelerated training (as it was mentioned earlier, this error function is penalizing the mistakes more sharply than `MeanSquareError`)
* [Implementing Hierarchical Memory Unit](https://github.com/mlpack/mlpack/pull/1048) - work in progress. Right now this PR contains:
    * A documented implementation of the `TreeMemory` - a tree-like data structure used for memory access in HAM unit + unit tests for it.
    * A documented implementation of the `HAMUnit` forward pass + unit tests for it.

# Highlights

First of all, I should admit that my main surprise was that I vastly underestimated the benchmarking framework part. During implementation, there appeared a lot of issues with the tasks themselves and making them work properly on LSTM even with small input sizes. This has been resolved, but it took way more time than it was planned initially.

Another source of interesting moments was the optimization PR. Both gradient clipping and cross-entropy error function were comparatively easy to implement. However, a lot of effort was invested into testing it and making it compliant with the rest of the `mlpack` codebase. This is undoubtedly **the** insight into industry programming I made during this summer. To clarify, the "industry" programming here is opposed to the competitive programming, which was my main source of programming experience before GSoC.

# Acknowledgements

I would like to thank my mentors, Marcus Edel and Ryan Curtin, for sharing their technical experience and giving well-timed and clear recommendations during the work. Also, I would like to thank Google for this brilliant program, which gave me a chance to have a cool summer as well as gain new experience in the open-source real-world project. (oh, and to get used to `git` as well ^_^)
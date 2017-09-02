Title: Augmented Recurrent Neural Networks: Week 8
Date: 2017-07-27 09:23:11
Tags: gsoc, rnn, neural network, lstm
Author: Konstantin Sidorov

Unlike previous weeks, this week was rather quiescent. It didn't feature insane bugs, weird behaviors of the code, mind-boggling compiler messages and anything else of the kind.

However, it featured a work on "casting" gradient clipping and cross-entropy performance function to the `mlpack` standard API. The pull request with the entire discussion: [link](https://github.com/mlpack/mlpack/pull/1070). As mentioned in the discussion of the PR, this code is more or less ready for merging into `mlpack/master`.
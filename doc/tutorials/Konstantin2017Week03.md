@brief Augmented Recurrent Neural Networks - Week 3
@author Konstantin Sidorov
@page Konstantin2017WeekThree Augmented Recurrent Neural Networks - Week 3
@date 2017-06-23 21:15:18

@section Konstantin2017WeekThree Augmented Recurrent Neural Networks - Week 3

Week 3 was rather quiescent - it mostly featured fixing weird bugs from previous two weeks and refactoring/cleaning the code. Some of the noteworthy changes and observations:

- We finally managed to feed sequences of vectors to LSTM network model. The solution was rather simple: stretch the sequence of vectors into one long bit sequence while preserving needed `inputSize`. For example, `[(0,0),(0,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1)]` should be fed as `[0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]` (just omitting brackets).
- Also we found out why the second representation from my Week 2 report was so inefficient - the model simply couldn't figure out where does the sequence end. The problem is more or less resolved (as a preliminary result, the model scored 100% accuracy for `maxLen = 3`). Scores of all three problems will be presented in Week 4 report.
- Finally, Week 3 have seen a massive clean-up of unit test code - the `CopyTask` benchmark solution was transferred to the [models](https://github.com/mlpack/models) repository. This repo will also feature some *real* models, such as the long-waited Hierarchical Attentive Memory unit.

In my opinion, the main result of Week 3 is that we have finally got a clean and lightweight codebase for generating test data and evaluating models on them.
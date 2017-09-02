@brief Augmented Recurrent Neural Networks - Week 4
@author Konstantin Sidorov
@page Konstantin2017WeekFour Augmented Recurrent Neural Networks - Week 4
@date 2017-06-30 19:12:34

@section Konstantin2017WeekFour Augmented Recurrent Neural Networks - Week 4

Unlike Week 3, this week was more eventful, but mostly it revolved around creating baseline for all three tasks. We finally managed to get a clean & working baseline code for `CopyTask`, `AddTask` and `SortTask` - it could be seen in my [pull request to `mlpack/models`](https://github.com/mlpack/models/pull/1).

The results for all three tasks are pending (hope to add them tomorrow morning). As expected, the copy task was moderately easy for LSTM model. However, binary addition task turned out to be much harder - the model didn't quite manage to add 2-bit numbers.

In this situation, a "failure" is, in fact, rather successful - we managed to make a pool of tasks that can check both the sanity of any other model (`CopyTask`) and the superiority of augmented models to vanilla RNN models (`AddTask`, `SortTask`).

*The results are still pending, so the previous paragraph may be updated if the complete result log will disprove any of the findings above*.

Also, we have finally begun the work on the central point of the project - Hierarchical Attentive Memory (HAM) unit implementation. For example, we already have some kind of API for it. We are in process of writing the tree memory structure - the main feature of the HAM unit which allows to access data using only `O(log(SIZE))` queries. This differs it from other augmented models, which use "differentiable" one-hot vector for querying the memory, which can be treated as `O(SIZE)` queries.

Of course, those features weren't really tested yet, but the main work has begun - so stay tuned for our next weekly report!
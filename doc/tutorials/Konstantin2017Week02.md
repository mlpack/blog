@brief Augmented Recurrent Neural Networks - Week 2
@author Konstantin Sidorov
@page Konstantin2017WeekTwo Augmented Recurrent Neural Networks - Week 2
@date 2017-06-15 21:55:34

@section Konstantin2017WeekTwo Augmented Recurrent Neural Networks - Week 2

This week I had fixed various issues of task classes - mostly refactoring old code and rewriting it to use Armadillo native features. Also, I managed to write up a simple baseline solver for `CopyTask` (it crashes on `AddTask` and `SortTask`, though - I'm planning to fix that bug on Week 3).

# LSTM baseline solution

## Data representation

There still an open-ended question on data representation for `CopyTask` - which is, incidentally, going to affect representation choices for two other tasks. (This question will also be resolved on Week 3, so stay tuned for more updates) The current options are:

- Feeding binary sequences to the network *as they stand*. For example, in this case the model may receive `[0,0,1] -> [0,0,1,0,0,1,0,0,1]` as the learning example. Although the current implementation of the LSTM solver can handle this representation almost perfectly, it is unclear how to feed it information about repeat count.
- Aligning input/output sequences to even length, padding the former sequence with zeros *from the right* and the latter - with zeros *from the left*. For example, in this case the model may receive `[0,0,1,0,0,0,0,0,0,0,0,0] -> [0,0,0,0,0,1,0,0,1,0,0,1]`. This representation resolves issue with repeat size information and also aligns the input and output sequences, which also makes the training procedure easier. In fact, this the currently used option, but it has an interesting extension...
- ..., namely, using 2-dimensional vectors as elements of the input sequence. The second cell of the vector is used for storing information on whether the given element of the sequence is the member of the original sequence (from 'standard-compliant' implementation of the `CopyTask`). For example, the example used in the previous two options will transform to: `[(0,0),(0,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1)] -> [0,0,0,0,0,1,0,0,1,0,0,1]`. This variant seem to be the most attractive, because it contains all the necessary for copying information in a very convenient form. However, right now there is a problem with feeding sequences of *vectors* - which will also be resolved on Week 3.

## Benchmarking

Now briefly about the running results. For the first two representations (the last one is so far defunct), the following neural network structure was used:

- linear layer with 30 hidden units;
- LSTM layer with 15 output units with Leaky ReLU nonlinearity (the standard `mlpack` implementation with `alpha=0.03`);
- linear layer + sigmoid nonlinearity with 1 output unit.

For training the network, standard `mlpack`'s `Adam` optimizer was used.

The results for aligned representation:

<table><tr><th /><th /><th colspan="9">Number of repetitions</th></tr><tr><th rowspan="8" style="transform: rotate(-90.0deg); width: 1.5em;">Sequence length</th><th /><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th></tr><tr><th>2</th><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td><td><center>1.000 <br> <small>(25)</small></center></td></tr><tr><th>3</th><td><center>0.300 <br> <small>(30)</small></center></td><td><center>0.200 <br> <small>(30)</small></center></td><td><center>0.300 <br> <small>(30)</small></center></td><td><center>0.233 <br> <small>(30)</small></center></td><td><center>0.000 <br> <small>(30)</small></center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td></tr><tr><th>4</th><td><center>0.114 <br> <small>(35)</small></center></td><td><center>0.229 <br> <small>(35)</small></center></td><td><center>0.171 <br> <small>(35)</small></center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td></tr><tr><th>5</th><td><center>0.025 <br> <small>(40)</small></center></td><td><center>0.100 <br> <small>(40)</small></center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td></tr><tr><th>6</th><td><center>0.111 <br> <small>(45)</small></center></td><td><center>0.000 <br> <small>(45)</small></center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td></tr><tr><th>7</th><td><center>0.040 <br> <small>(50)</small></center></td><td><center>0.040 <br> <small>(50)</small></center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td></tr><tr><th>8</th><td><center>0.127 <br> <small>(55)</small></center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td><td><center>-</center></td></tr></table>

'Vanilla' representation is *very* successful for the case `nRepeats = 1`, because in this representation LSTM passes all the tests from the previous table with 100% precision (sic!) I'm planning to find the explanation to this behavior during Week 3.

# Next up

As I mentioned above, Week 3 will mostly about fixing rather strange bugs that popped up during the implementation of the baseline. However, if they will be resolved promptly, we're going to switch to the central part of the project - implementing the [Hierarchical Attentive Memory unit](https://arxiv.org/abs/1602.03218).
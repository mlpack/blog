Title: Augmented Recurrent Neural Networks: Week 7
Date: 2017-07-18 23:15:18
Tags: gsoc, rnn, neural network, lstm
Author: Konstantin Sidorov

This week featured even more fixes for baseline model. The most notable achievement is that we've finally managed to make an LSTM model that would be able to *completely* learn the CopyTask (even for maximum length and repetitions parameters).

To this end, several small (but important) changes had to be implemented:

- The `CrossEntropyError` layer - earlier the model was learned on MSE objective. Cross entropy penalizes the mistakes sharper than MSE (e.g., assigning 0 probability to the true label results in +infinity loss with cross entropy and in only +1 loss with MSE).
- Gradient clipping - to rectify the problem of *objective explosion*, all gradient components that were bigger in absolute value than some fixed number were replaced with that value. In math: `g0 = min(max(g, minValue), maxValue).

Also, the model was transferred to `MiniBatchSGD` from `Adam` - the latter exposed gradient explosion problem, which resulted in a heavy overfitting.

To avoid the overfitting problem completely, the testing scheme was changed. Here's what happens now on every training epoch:

- The model is trained on some train samples;
- After that, the model is evaluated on validation set (we use three datasets, not two);
- If this iteration gave the best validation score, run it on the test set and record the score on it.

In other words, now we pick the *best* model among all the model that were visited during training.

Also, now there is a stub (non-functional so far) for highway layer, as proposed in [arxiv paper](https://arxiv.org/abs/1505.00387).

I think now the task API & representation problem is more or less solved. Now we switch to the long-waited part - HAM unit implementation. (As I mentioned in the IRC chat, we already have a head start with ready API for HAM unit + *implemented and tested* memory structure for it). Stay tuned!
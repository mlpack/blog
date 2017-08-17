Title: Augmented Recurrent Neural Networks: Week 11
Date: 2017-08-17 14:49:57
Tags: gsoc, rnn, neural network, lstm
Author: Konstantin Sidorov

As we keep approaching the finale of the GSoC program, the HAM work also gets deeper into the implementation stage. For instance, we have finally implemented *and tested* the implementation of `HAMUnit` forward pass.

Right now, we're trying to implement the backward pass, but there is still a technical question about the representation of the HAM parts. The current ideas are:

- Adding `FFN` to `LayerTypes`. Although the declaration becomes template-less, it has a drawback of not supporting `FFN<T>` for *all* `T`.
- Using `FFN` objects "as-is" (e.g., calling their Forward and Backward methods). This is a rather straightforward approach (which I'm following right now to simplify matters), but it has a drawback of constrainting to `FFN` models.
- Taking `FFN` objects and storing their layers *separately*. This approach fixes the drawbacks of the previous two approaches, but it doesn't seem easy to implement - and also we still have to figure out if we do need it in the HAM setting.

So, the final week is going to be interesting - hope to get things done! :)

Title: Augmented Recurrent Neural Networks: Weeks 5 & 6
Date: 2017-07-11 22:09:18
Tags: gsoc, rnn, neural network, lstm
Author: Konstantin Sidorov

This two weeks featured a lot of weird bugs. The most memorable, in my opinion, are:

- The missing closing curly brace drove g++ crazy, which resulted in error message of length 27k lines (sic!). The link to the `make` log: [gist](https://gist.github.com/partobs-mdp/e24d96b07979111c0f8b9a10ac68d348)
- The copy-paste bug in `mlpack/models` repo. Because of that bug the LSTM model in all tasks was iterating the learning 20 times - even if `epochs` parameter was set to another value!

However, there was also several nice code refactorings:
- Automating the parameter check in `mlpack/models`. Unlike previous versions, now we use automated check for parameter validity and error message generation.
- Templating the `RunTask` code in `mlpack/models`. Now the task type is a template, unlike previous versions, where a separate function was crafted for every task.

Also, we keep on working on HAM implementation - for example, there is an [open pull request](https://github.com/mlpack/mlpack/pull/1048) on adding `HAMUnit`, which already features *tested* implementation of tree data structure.

Finally, we have more or less stable experiment results for the three tasks:

- CopyTask: [output log link](https://gist.github.com/zoq/1625cf338d6dca769afd62dbe595ca41)
- AddTask: TBA
- SortTask: TBA
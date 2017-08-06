Title: Deep Reinforcement Learning Methods - Week-8 Highlights
Date: 2017-08-05 22:00:00
Tags: gsoc
Author: Shangtong Zhang

This week I implemented async n-step q learning and async one step sarsa. Both fit into my async learning framework very well. Although those two async algorithms, as well as async q learning and upcoming a3c, share many common code snippets, I find it very difficult to unify them further. I tried that in python, it ended up with many `if` clauses, which heavily hurt the readability of the code. And it will be even more troublesome if we want to support LSTM layers. In the meantime I also worked on the PR of async one step q learning. We introduced `HAS_OPENMP` to be compatible with non-openmp compiler. We also totally eliminated the explicit use of lock by a trick of reordering `push` and `pop` and thus we only need `omp critical`, which I think made the code more clear. I think this PR now is finally ready to merge.

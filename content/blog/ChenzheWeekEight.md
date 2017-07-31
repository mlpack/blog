Title: Atom domain code for vector problems - Week 8
Date: 2017-07-30 22:00:00
Tags: gsoc, optimization
Author: Chenzhe Diao

Firstly, I tried to merge my first PR with my current code this week. Also, I tried to create a new PR with my vector problem code. Unfortunately, I had a bad practice when using git. I didn't separete my commits between vector problems code and matrix problems code. so I had to pick my current files and merge all changes manually. This was quite a painful process since there were a lot of API changes.

Also, I plan to make my next PR consist of code for "solving constraint for structured group", "updating with line search", "using regularization parameters", "support prune steps", "new atoms API", "updating with full correction". Although most of the codes were already written, I haven't tested them with large problems before. So I was writting some exectables in `methods/` folder this week. I tried to generate some comparison plots for convergence speed over iterations and clock time. Since there were a lot to test and to compare, I haven't finished them all. I will open a new PR after all of them are done. I guess these tests would also confirm my codes are correct, and my implementations are ok for large problems.
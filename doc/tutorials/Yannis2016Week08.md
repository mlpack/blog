Title: Some thoughts on the LSH Model
Date: 2016-07-19 20:20:20
Tags: gsoc, lsh, modeling
Author: Yannis Mentekidis

As I've discussed before, LSH has one major problem - a large number of parameters which are difficult to tune. Other approximate nearest neighbors algorithms accept a relative error $\epsilon$ and, through theoretical guarantees, return points that are less than (1+$\epsilon$) times further from the nearest neighbors.

As opposed to that, LSH asks the user to specify a number of hash tables (L), a code length (M), a window size (W) and now a number of additional probes (T). Of course, literature provides explanations towards how these affect performance and time cost, but still they are not as clear.

The idea behind the LSH model is to, eventually, produce two functions:

Recall(Dataset, L, M, W, T)

and

Selectivity(Dataset, L, M, W, T)

which will (hopefully in an efficient manner) estimate the Recall and Selectivity of an LSH run with parameters (L, M, W, T) on the dataset.

To do that, the authors define a statistical expression for Recall(.) and Selectivity(.) and model the data distribution and especially the distribution of distances between points.

If (hopefully) the functions are convex, then we can use binary search to get to their minima efficiently, thus producing a favorable parameter set for LSH.

The statistical models that come from the authors' analysis are quite complex and require a lot of stuff to be done. I have begun by implementing an algorithm that fits the parameters of a gamma distribution to a dataset, and creating a checklist of what needs to be done next.


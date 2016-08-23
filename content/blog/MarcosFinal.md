Title: Approximate Nearest Neighbor Search - Conclusion
Date: 2016-08-23 3:00:00
Tags: gsoc, knn, kfn, spill-tree
Author: Marcos Pividori

I have been working this summer on the GSoC Project:
"Approximate Nearest Neighbor Search" (Project site: [[1]][1]).

The main contribution can be summarized in these pull requests:

 * [[pull/768]][pull/768]  (Api details)
 * [[pull/766]][pull/766]  (Fix furthest neighbor sort policy)
 * [[pull/765]][pull/765]  (Api improvement - move semantics)
 * [[pull/764]][pull/764]  (Fix tests)
 * [[pull/762]][pull/762]  (Greedy Traverser)
 * [[pull/747]][pull/747]  (Spill trees Implementation)
 * [[pull/732]][pull/732]  (Heaps for mlpack)
 * [[pull/731]][pull/731]  (Fix memory leak)
 * [[pull/727]][pull/727]  (Fix TreeTrait for BallTree)
 * [[pull/693]][pull/693]  (Modify NSModel to use boost variant)
 * [[pull/684]][pull/684]  (Approx KNN for Dual tree algorithms)
 * [[pull/682]][pull/682]  (Properly resetting auxBound)
 * [[pull/668]][pull/668]  (Add B_aux according to issue #642)
 * [[pull/655]][pull/655]  (Fix erroneous ball tree definition)
 * [[pull/646]][pull/646]  (Remove duplicated code for traversal info)
 * [[pull/645]][pull/645]  (Properly use Enum type)
 * [[pull/637]][pull/637]  (Fix a mistake in metric policy)
 * [[pull/19]][pull/19]  (Improve programs for ANN and FLANN)
 * [[pull/17]][pull/17]  (Approx KNN for the benchmarking system)
 * [[pull/14]][pull/14]  (Add Num of BaseCases as a metric)

(List of commits: [[link]][commitlist])


## Approximate nearest neighbor search:

I modified mlpack's code to include an *epsilon* value, which represents the
maximum relative error. It is considered by the prune rules when deciding if a
given node combination should be analyzed, (as suggested at the end of the paper
[[2]][2]), with a general implementation that works for both *KFN* and *KNN*.

The command line tools: *mlpack_knn* and *mlpack_kfn*, were updated to include
an extra option *"-e"*, to specify the maximum relative error
(default value: 0).

The main code developed was included in the [[pull/684]][pull/684].

Take into into account that epsilon represents the maximum relative error.
So, the average relative error (effective error) will be much smaller than the
epsilon value provided.

As expected, higher values of the epsilon parameter implies that more nodes are
pruned nodes and, therefore, we have a faster algorithm, as can be seen in the next graphic for the dataset *isolet*:

![graphic1](https://github.com/MarcosPividori/marcospividori.github.io/blob/master/mlpack-pictures/Isolet_EpsilonVsRuntime.png?raw=true)


## Spill Trees:

I have implemented Spill Trees, as defined in: "An Investigation of Practial
Approximate Nearest Neighbor Algorithms" [[3]][3] ([[pull/747]][pull/747]).
It is a variant of binary space trees in which the children of a node
can "spill over" each other, and contain shared datapoints.

One problem with Spill Trees is that their depth varies considerably depending
on the overlapping size $\tau$.

For that reason, I have implemented Hybrid Spill Trees [[3]][3],
which provide better guarantee in the logarithmic depth of the tree.

The extension was incorporated to existing *mlpack_knn*.
You can specify *"-t spill"* to consider spill trees, and the command line
paramenters *"--tau"* to set different values for the overlapping size (default
value is tau=0), and *"--rho"* to set different values for the balance threshold
(default value is rho=0.7).


### Spill Trees's decision boundary:

We have considered many different approaches for the implementation of Spill
Trees, see discussions in:
[[issues/728]][issues/728] and [[spilltrees.pdf]][spilltree.pdf].
Finally, we decided to implement a similar approach to the one mentioned in Ting
Liu's paper.


### Splitting Hyperplanes

Actual implementation of Spill Trees can be configured to choose between different
kind of splitting Hyperplanes:

+) Providing the template parameter `HyperplaneType` between two candidate classes:
`AxisOrthogonalHyperplane` and `Hyperplane` (not necessarily Axis-Orthogonal).
(In both cases the hyperplane with the widest range of projection values will be
chosen).

+) Providing the template parameteter `SplitType`, between two candidate classes:
`MidpointSpaceSplit`, `MeanSpaceSplit`, which determines the splitting value
to be considered.

By default, *mlpack_knn* considers *Axis-Orthogonal Hyperplanes* and *Midpoint
Splits*, because it is the most efficient option (we can project any vector in
O(1) time).


### Defeatist Traversers

I have implemented *Hybrid SP-Tree Search* as defined in [[3]][3].
We can control the hybrid by varying $\tau$. If $\tau$ is zero, we have a pure
spill tree with defeatist search, very efficient but not accurate enough.
If $\tau$ is a very large number, then every node is a non-overlapping node and
we get back to the traditional metric tree, with prunning rules, perfectly
accurate but not very efficient.
By setting different values for $\tau$, we have a trade-off between efficiency
and accuracy.

Also, I implemented a Defeatist Dual Tree Traverser, where the *query tree* is
built without overlapping.

The `DefeatistDualTreeTraverser` is faster than the
`DefeatistSingleTreeTraverser`, specially when the value of tau increases.

Some results can be seen in the next graphic for the dataset *isolet*.

![graphic2](https://github.com/MarcosPividori/marcospividori.github.io/blob/master/mlpack-pictures/1000000-10_Spill_EffectiveErrorVsRuntime.png?raw=true)


## General Greedy Search Traverser:

Also, I implemented a *general greedy single tree traverser* to perform greedy
search, that always chooses the child with the best score when traversing the
tree, and doesn't consider backtracking: `GreedySingleTreeTraverser`.

It is a tree independent implementation (based on the general TreeType API).
As expected, the greedy traverser performs considerably faster than other
approachs, at the cost of some relative error in the results.
(PR: [[pull/762]][pull/762]). Further disccusion in: [[issues/761]][issues/761].

We can simply reduce the relative error by increasing the leaf size of the tree,
as is shown in the next graphic for the dataset *isolet*.

![graphic3](https://github.com/MarcosPividori/marcospividori.github.io/blob/master/mlpack-pictures/Isolet_Greedy_EffectiveErrorVsRuntime.png?raw=true)


## Other improvements

Also, I have been improving some parts of the existing code:


### Bound Issues:

I found some issues in the definition of the B2 bound. We were discussing about
it in [[issues/642]][issues/642] and, after thinking about the different
special cases, we found some examples where actual definition could fail.
I fixed existing code to consider slighty different bounds.


### Improve NSModel implementation:

I have been improving existing code for `NSModel`, as was suggested
in [[issues/674]][issues/674], using boost variant to manage different
options for tree types. (PR: [[pull/694]][pull/693]).


### Heaps for the list of candidates:

I realized in many parts of the code, we were keeping track of the best k
candidates visited through a sorted list. Instead of maintaining a
sorted list, a better approach was to use a priority queue. I implemented
this in [[pull/732]][pull/732].


### Benchmarking system:

I have been updating the benchmarking system to include approximate neighbor
search not only with mlpack, but also with other libraries like [[ANN]][ANN] and
[[FLANN]][FLANN] (PR: [[pull/14]][pull/14] and [[pull/19]][pull/19] ).

Also, I created a new view to plot the progress of a specific metric for
different values of a method parameter. For example, for knn, it is possible
to analyze the number of base cases and runtime for different values of
approximation error (epsilon), with different libraries/configurations.
(PR: [[pull/17]][pull/17]).


## Acknowledgement:

I want to thank the mlpack community for giving me the opportunity to work with
them this summer, it has been a fascinating experience!
They were very responsive, I always found someone to talk in the IRC channel,
willing to offer their time to discuss ideas or help me with my project! :)


For further information see my previous [[blog posts]][blog-posts].


[1]: https://summerofcode.withgoogle.com/projects/#6292674801827840
[2]: http://www.ratml.org/pub/pdf/2015faster.pdf
[3]: http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2005_187.pdf
[issues/642]: http://github.com/mlpack/mlpack/issues/642
[issues/728]: http://github.com/mlpack/mlpack/issues/728
[issues/674]: http://github.com/mlpack/mlpack/issues/674
[issues/761]: https://github.com/mlpack/mlpack/issues/761
[spilltrees.pdf]: http://github.com/mlpack/mlpack/files/372825/spilltrees.pdf
[blog-posts]: http://mlpack.org/gsocblog/author/marcos-pividori.html
[ANN]: https://www.cs.umd.edu/~mount/ANN/
[FLANN]: http://www.cs.ubc.ca/research/flann/
[commitlist]: https://github.com/mlpack/mlpack/commits/master?author=MarcosPividori
[pull/768]: https://github.com/mlpack/mlpack/pull/768
[pull/766]: https://github.com/mlpack/mlpack/pull/766
[pull/765]: https://github.com/mlpack/mlpack/pull/765
[pull/764]: https://github.com/mlpack/mlpack/pull/764
[pull/762]: https://github.com/mlpack/mlpack/pull/762
[pull/747]: https://github.com/mlpack/mlpack/pull/747
[pull/732]: https://github.com/mlpack/mlpack/pull/732
[pull/731]: https://github.com/mlpack/mlpack/pull/731
[pull/727]: https://github.com/mlpack/mlpack/pull/727
[pull/693]: https://github.com/mlpack/mlpack/pull/693
[pull/684]: https://github.com/mlpack/mlpack/pull/684
[pull/682]: https://github.com/mlpack/mlpack/pull/682
[pull/668]: https://github.com/mlpack/mlpack/pull/668
[pull/655]: https://github.com/mlpack/mlpack/pull/655
[pull/646]: https://github.com/mlpack/mlpack/pull/646
[pull/645]: https://github.com/mlpack/mlpack/pull/645
[pull/637]: https://github.com/mlpack/mlpack/pull/637
[pull/19]: https://github.com/zoq/benchmarks/pull/19
[pull/17]: https://github.com/zoq/benchmarks/pull/17
[pull/14]: https://github.com/zoq/benchmarks/pull/14

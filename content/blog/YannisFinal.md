Title: Summary of LSH changes for GSoC 2016
Date: 2016-08-19 20:20:20
Tags: gsoc, lsh, multiprobe, tuning, parallel
Author: Yannis Mentekidis

As we are approaching the pencils down date, I think it is a good time to create a short summary of my contributions to mlpack this summer. Seeing all the students being very active, and so much code being committed, I believe summing up what I've done in the last months is going to help anyone wanting to come up-to-speed with the part of the changes I'm responsible for.



# Executive Summary

TL;DR: A summary of my commits can be found [here][commits].

Here's a list of my Pull Requests, each with a short description.

 * LSH Non-deterministic Testing: [605][605]
 * LSH Projection Table Access: [663][663]
 * LSH Deterministic Testing: [676][676]
 * LSH Optimization - find() vs unique(): [623][623]
 * LSH Optimization - secondHashTable: [675][675]
 * Multiprobe LSH: [691][691]
 * LSH Parallelization with OpenMP: [700][700]
 * Gamma Distribution, boost backporting: [729][729]
 * Gamma Distribution, more functionality: [751][751]
 * LSH Tuning (under construction): [749][749]

# LSH Testing

This contribution actually started before my GSoC application, and it was based on [Issue 261][261]. The question was: How can we create tests that will verify that the LSH module works correctly, given that LSH is a randomized approximate algorithm and there is no "correct" solution to check for?

The accepted solution was twofold.

First, I discussed with Ryan and we came up with some reasonable assumptions that LSH must fulfill: Increasing the number of tables must increase recall, increasing the number of projections per table must decrease recall. A very "expensive" run should examine nearly 100% of the points and have nearly 100% recall. A very "cheap" run should examine almost no points, and have recall near 0. These tests were added in several commits that are mostly summarized by [Pull Request 605][605].

The second part of the solution needed us to have write access to the (otherwise random) projection tables used by the `LSHSearch` class. I modified the code slightly to be able to do that in [Pull Request 663][663]. That PR also changes the way projection tables are used, going from `std::vector<arma::mat>` to `arma::cube`. Then, in [Pull Request 676][676], I added deterministic tests for LSH, basically exploiting the fact that, if the identity matrix is used as a projection table, the resulting hash buckets are predictable. An intuition of this idea is given in a [comment I made in a different PR][691com].

These three Pull Requests increased LSH testing coverage significantly.

# LSH Optimizations

Before moving to the main course (I'm looking at you, Multiprobe LSH), I want to focus on two Pull Requests that I think are important optimizations to the LSH module.

The first one, [Pull Request 623][623], tries to reduce the memory footprint of `LSHSearch::ReturnIndicesFromTable()`. The original implementation would allocate N spaces for the N points, set them all to 0, then mark the points that were in the same hash bucket as a query and only keep those indices to create the candidate set. The complexity of that was $\mathcal{O}(N)$. Instead, we could simply take note of the indices of all the points we find, and only keep the unique ones. Unique runs in $\mathcal{O}(M log M)$, but if M is significantly smaller than N, we reduce both the memory used and the time needed.

To find the sweet spot between M and N, we did extensive tuning with a number of datasets, and allowed our implementation to pick either the $\mathcal{O}(N)$ or $\mathcal{O}(MlogM)$ method for each point individually.

The second optimization, summarized in [Pull Request 675][675] was made mainly by Ryan, based on our observation that the second-level hash table implementation was too heavy. What the previous implementation did was allocate a `secondHashSize x bucketSize` armadillo matrix, with each row corresponding to the key for hash value i. The first `bucketSize` points hashed to each value were kept, and the rest were discarded. Then, the hash table was condensed.

For the default parameters (`secondHashTable = 99901, bucketSize = 500`), this required almost 50 million objects of type `size_t` to be allocated. `size_t` is usually 8 bytes long, resulting in an allocation of about 400Mb when the program launched. This is bad, but it's even worse if a user sets `bucketSize` to some significantly larger size, like 3000 or 4000 (not unreasonable for larger datasets).

The new version of the code refrains from such excessive allocations, using `std::vec<arma::Col>` instead of a 2-dimensional matrix.

# Multiprobe LSH

Now to the interesting part: Implementation of a state-of-the-art algorithm that (promises to) significantly improve the approximation results of naive LSH. The implementation was based on [this paper][mplsh], and it was introduced to mlpack through [Pull Request 691][691].

The implementation was mostly straight-forward, since the paper is quite clear and even provides pseudocode for the most tricky part.

Of course, many mistakes that were made were much easier to test for, now that we could write (semi-)deterministic tests for LSH.

The `LSHSearch` class of release 2.0.3 does not yet include Multiprobe LSH, so if you want to try it before release 2.0.4 which will (presumably) include all GSoC changes, you should download and install mlpack from the [source](github.com/mlpack/mlpack).

# Parallelization with OpenMP

This was another part I was looking forward to, and which I believe is an important improvement over the old implementation. Using OpenMP directives and minimal extra code, we were able to have the `LSHSearch` class process more than one query in different threads.

[Pull Request 700][700] is merged, so if you're using a multi-core machine (you probably are) running mlpack, you can now process your LSH queries faster (or you will be, from mlpack 2.0.4, and if you're not using Visual Studio to compile).

# Implementation of LSH Tuning

**Fair warning**: LSH Tuning is still under construction.

For the last part of my GSoC contributions, I decided to implement the [LSH Tuning][lshtuning] algorithm. The algorithm helps identify parameter sets for which Multi-probe LSH will perform well for a specific dataset. Without this algorithm, tuning LSH by hand quickly becomes tedious and annoying.

Among other things, LSH Tuning models pairwise distances by fitting a Gamma Distribution to a sample of them. In order to do that fitting, I implemented an algorithm proposed by [Thomas Minka][minka] that converges faster than the method proposed in the original paper. The implementation of the Gamma Distribution is included in [Pull Request 729][729], which includes backporting of several features from Boost 1.58 needed by Minka's algorithm.

The Gamma Distribution implementation was incomplete, as I mention in [Issue 733][733]. I worked towards closing that issue later, and implemented most of the missing functionality in [Pull Request 751][751]. Some work remains to be done, and I will come back to it once everything else is ready.

The rest of the code for the LSHTuning module, a new class and executable that will be added to mlpack, is still in progress. The paper describing the algorithm has been convoluted in a few parts, but I think most of my confusion has been solved (with immeasurable help from Ryan), so I'm confident the code will be ready to ship relatively soon.

I am almost done implementing the core algorithm, but for it to be usable I need to write the code for the corresponding mlpack executable and write useful tests. My progress can be seen in [Pull Request 749][749]. 


# Conclusions

It has been an amazing summer, and although I didn't have the time to complete any of my blue-sky ideas that I discussed in my proposal, I think the experience has made me significantly more aware of the mlpack codebase. I am now much more capable to continue contributing to it, so hopefully I will be implementing many more interesting features soon!


[commits]: https://github.com/mlpack/mlpack/commits?author=mentekid
[261]: https://github.com/mlpack/mlpack/issues/261
[605]: https://github.com/mlpack/mlpack/pull/605
[663]: https://github.com/mlpack/mlpack/pull/663
[676]: https://github.com/mlpack/mlpack/pull/676
[691com]: https://github.com/mlpack/mlpack/pull/691#issuecomment-228315339
[623]: https://github.com/mlpack/mlpack/pull/623
[675]: https://github.com/mlpack/mlpack/pull/675
[mplsh]: http://dl.acm.org/citation.cfm?id=1325958
[691]: https://github.com/mlpack/mlpack/pull/691
[700]: https://github.com/mlpack/mlpack/pull/700
[lshtuning]: http://dl.acm.org/citation.cfm?id=1458172
[minka]: http://research.microsoft.com/en-us/um/people/minka/papers/minka-gamma.pdf
[729]: https://github.com/mlpack/mlpack/pull/729
[733]: https://github.com/mlpack/mlpack/issues/733
[751]: https://github.com/mlpack/mlpack/pull/751
[749]: https://github.com/mlpack/mlpack/pull/749

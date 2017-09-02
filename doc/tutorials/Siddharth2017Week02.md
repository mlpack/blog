Title: QUIC-SVD
Date: 2014-06-03 15:52:00 
Tags: gsoc, cosine tree, svd, cf 
Author: Siddharth Agrawal

My project is titled 'Collaborative Filtering Package Improvements', where I have proposed to add three new matrix factorization techniques, namely QUIC-SVD, Regularized SVD and Probabilistic Matrix Factorization. This blog post is about QUIC-SVD, and the challenges I faced while implementing it.

QUIC-SVD is a matrix factorization technique, which operates in a subspace such that A's approximation in that subspace has minimum error(A being the rating matrix). The subspace is constructed using a cosine tree, which ensures minimum representative rank(and thus a fast running time). It follows a splitting policy based on Length-squared(LS) sampling and constructs the child nodes based on the absolute cosines of the remaining points relative to the pivot. The centroids of the points in the child nodes are added to the subspace span in each step. Each node is then placed into a queue prioritized by its residual error. This is the primary reason why cosine trees improve sampling efficiency as compared to length-squared(LS), residual length-squared(RLS) and random projection(RP) sampling, as they always focus on areas with maximum potential for error reduction. The subspace approximation error of A after each step is calculated using a Monte Carlo estimate. If the error is below a certain threshold, the method proceeds to calculate the Singular Value Decomposition(SVD) in the obtained subspace. Otherwise, the same procedure is repeated until we obtain a subspace of sufficiently low error. QUIC-SVD creates its own subspace to operate in and thus does not require a rank parameter. The original paper can be found at: http://www.cc.gatech.edu/~isbell/papers/isbell-quicsvd-nips-2008.pdf.

The following things have been implemented:

-> CosineNode class which manages the operations of all the nodes in the tree, namely length-squared sampling, split point sampling and node splitting.

-> CosineTree class which has functions for constructing the tree, for orthonormalizing using the Gram Schmidt algorithm and for estimating the subspace reconstruction error using Monte Carlo simulation.

The ExtractSVD() function mentioned in the paper and tests for the algorithm are yet to be implemented.

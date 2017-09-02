Title: QUIC-SVD - Wrapping Up
Date: 2014-06-17 22:45:00
Tags: gsoc, cosine tree, svd
Author: Siddharth Agrawal

The past two weeks was one hell of a ride! It involved wrangling with inefficiencies and punching segmentation faults with a series of tests. Okay, let's be more specific.

The major problem with the code was the unnecessary time being spent with the use of arma::join_rows(), which apparently copies the entire matrix everytime it is called. This was dealt with by storing the basis vector from each node in the CosineNode object itself.
Another inefficiency was the serial access of current basis vectors using a boolean vector. Ryan came up with a great idea, which was to access the basis vectors through the priority queue itself. After a lot of struggling around with the STL 'queue' interface, the boost::heap priority_queue interface proved to provide the solution we needed.

Note: If you are looking for a priority queue implementation to be used with C++, use the boost one. It provides a lot more flexibility compared to its STL counterpart.

The following things have been added, which now almost completes the QUIC-SVD module. Though this comes on 17th June, which is two days later than the deadline I had set, Ryan says and I agree 'coding better is more important than coding faster'.

1. A QUIC-SVD class, which can be used as an interface.
2. Unit tests for the CosineTree class.

QUIC-SVD, I feel, was the most difficult part of my application. Now that it is done, let's see how I cope with the rest of it.

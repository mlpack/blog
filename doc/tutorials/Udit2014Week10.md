Title: Implementation of Multi-Class Adaboost Algorithm: Week 10 and 11 Highlights
Date: 2014-08-03 22:30:00
Tags: gsoc, adaboost, perceptron, decision stump
Author: Udit Saxena

Nearing the end guys ! Two weeks left !

I've finally finished the implementation of the Adaboost.mh algorithm. And after a few suggestions from Ryan, I finally figured out what tests would be required and slowly but surely added those tests to the Adaboost test suite. 

But probably the most important breakthrough I've had was when I actually figured out how to implement Weighted Decision Stumps - it's been an elusive solution for a while, annoying after a while. But after I had added the required methods, adding tests similar to the Perceptron for the Decision Stumps while testing Adaboost was a simple task.

Also, after discussing it with Ryan, I've added tolerance as a parameter for Adaboost.

Now for the optimizations. Even with the tolerance taking care that the number of iterations is controlled, I still think the algorithm can be optimized. Even a bit can help over several thousands of iterations and can help scale up.
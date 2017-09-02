Title: We need to go deeper, Googlenet : Week-3 Highlights
Date: 2016-06-13 20:00:00
Tags: gsoc, edge_boxes
Author: Nilay Jain

This week I cleaned up the code on feature extraction, wrote tests related to it and read mlpack code that will be used for implementation of the next part of edge boxes algorithm. The details follow.

In the feature extraction code, I incorporated the changes suggested by my mentors, made some snippets code adhere to the design guidelines - used size_t instead of int to remove warnings, added const to parameters of function that need to be unchanged, and optimizing some pieces of code that seemed redundant, to name a few.

Then I proceeded to write the tests for the Image Processing functions that were implemented manually using standard libraries as reference. Specifically, the tests were written for Distance Transform, Border, RGB2LUV and Convolution Triangle functions. There were many bugs found in these functions and writing tests for these functions before evaluating the code does seem now to be a fruitful exercise.

After that I read up on PCA, Decision Stump and Hoeffedding tree implementations in mlpack. As these will be used to implement the Structured Random Forest Class.

The coming week I plan to use these classes and complete the Random Forest class.
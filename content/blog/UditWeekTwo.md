Title: Implementation of Multi-Class Adaboost Algorithm: Week 1 and 2 
Date: 2014-06-04 13:30:00
Tags: gsoc, adaboost, decisionstump, 
Author: Udit Saxena

Two weeks into GSoC, I feel I am almost done getting the hang of things - though I'm pretty sure I'll never get around to completely knowing Armadillo, with its vast API. 
Unit testing through Boost has also been a new experience, something which changes the way you think about good programming, completely.

For implementing Multi-Class Adaboost, I have defined a few stages, the first of which includes :
+ Implementing Weak Learners 
  - OneR/Decision Stump
  - C4.5
  - Simple Perceptron

My first two weeks have been about implementing a decision stump (oneR), and the end of the second week saw me having a very important discussion with Ryan as to deciding how to handle continuous attributes. 
I plan to commit by the end of the third week, with help from Ryan and Marcus.

As of now, I have almost completed the decision stump - only CalculateEntropy() needs to be taken care of - and need to provide documentation and proper unit tests. 
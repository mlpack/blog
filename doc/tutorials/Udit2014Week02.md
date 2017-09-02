@brief Implementation of Multi-Class Adaboost Algorithm - Week 2
@author Udit Saxena
@page Udit2015WeekTwo Implementation of Multi-Class Adaboost Algorithm - Week 2
@date 2014-06-04 13:30:00

@section Udit2015WeekTwo Implementation of Multi-Class Adaboost Algorithm - Week 2

Two weeks into GSoC, I feel I am almost done getting the hang of things - though I'm pretty sure I'll never get around to completely knowing Armadillo, with its vast API. 
Unit testing through Boost has also been a new experience, something which changes the way you think about good programming, completely.

For implementing Multi-Class Adaboost, I have defined a few stages, the first of which includes implementing Weak Learners: 
1. OneR/Decision Stump
2. C4.5
3. Simple Perceptron

My first two weeks have been about implementing a decision stump (oneR), and the end of the second week saw me having a very important discussion with Ryan as to deciding how to handle continuous attributes. 
I plan to commit by the end of the third week, with help from Ryan and Marcus.

As of now, I have almost completed the decision stump - only CalculateEntropy() needs to be taken care of - and need to provide documentation and proper unit tests.
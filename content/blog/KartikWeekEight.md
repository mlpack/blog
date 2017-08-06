Title: Neural Evolution Algorithms for NES games - Week 8 Progress
Date: 2017-08-07 00:27:00
Tags: gsoc , neural_evolution
Author: Kartik Nighania

this week have been really exiting for me. I have completed CMAES algorithm. The main highlights are.


1) introduced a new time parameter by which search can be optimised very well. This method uses CPU time and calculates time return according to implementation time for some functions. This solved a major bug in the code which was huge problem back then. Now searching for hard function optimization like the Rosenbrock function upto 50 dimensions was also found to be working accurately.


2) made certain changes to the constructor and other optimization like making own eigen decomposition functions which converges faster than armadillo library maybe as it does not makes sure if the matrix is orthogonal or not.


3) Writing the doxygen tutorial for CMAES was fun and I tried my best to make it simple and to contain everything. It explains the algorithm , the class that the user has to make, the converge method calling and also using it with other functions such as logistic regression.


4) talked to my mentor and have started the code for CNE. Im right now working on the neural network optimization part. The code of Bang Lui from last year GSoC came handy and is very helpful. The FFN library will be used and CNE will be made as an optimizer in it.
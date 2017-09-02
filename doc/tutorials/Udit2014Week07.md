@brief Implementation of Multi-Class Adaboost Algorithm - Week 7 + 8 + 9
@author Udit Saxena
@page Udit2015WeekSevenEightNine Implementation of Multi-Class Adaboost Algorithm - Week 7 + 8 + 9
@date 2014-07-20 22:30:00

@section Udit2015WeekSevenEightNine Implementation of Multi-Class Adaboost Algorithm - Week 7 + 8 + 9

Woah ! It's been a while. A lot of updates to follow.

After the Decision Stump code review, I got down to the Perceptron review. But that was an easy matter - some refactoring and adding another test. Although, I'm still looking at providing the Gradient Descent template before July ends. That has been a (relatively) time consuming and unanticipated hiccup. 

After this I finally did start with the Adaboost algorithm. Lots of implementations and extensions of boosting do float around in the academic circles. I had the choice of starting with the Adaboost.m1, extending it to the Adaboost.mh and finally stopping at the Adaboost.SAMME (stagewise additive modelling). 
I began with the m1 and got stuck for a while when considering how to incorporate the Weight Distributions required by Adaboost into our Weak Learners. I mean, with the Perceptron, it is intuitive as you are only updating the weights of the class weight in weightMatrix. But it isn't so straightforward when you look at Decision Stumps. 

I went ahead with the weighted Perceptron scheme in hand, hoping to read up something that would shed furhter light on the Decision Stump problem. As of now, I've implemented the Adaboost.mh algorithm and am going to design tests this week; extending the adaboost.m1 to SAMME should be a simple job. It's the former which is going to be tricky.

The adaboost.mh algorithm involves going through a 2-Dimensional matrix every time the weights are updated, which I fear will, over hundreds and thousands of iterations, turn out to be quite slow, and this is something I also hope to optimize this week (if possible at all).
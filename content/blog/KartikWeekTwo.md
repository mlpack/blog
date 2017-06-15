Title: Neural Evolution Algorithms for NES games - Week 2 Progress
Date: 2017-06-15 23:00:00
Tags: gsoc , neural_evolution
Author: Kartik Nighania

A new optimizer is made called CMAES which works like the rest of the optimizer that MLPack implements

it takes as parameters -

1) number of dimensions we are working on 
2) Initial start position of optimization
3) Initial standard Deviations 

the rest of the parameters are computed automatically which is convinient as the algorithm is too sensitive
to those parameters and default parameters are fine tuned and found according to an implementation and 
differs from code to code.

the user can if want set some parameters for which appropriate getters and setters are made

moreover the most important parameters that user finds to change according to application is the
algorithms stop criteria for which appropirate getters and setters are made.

the above mentioned things are all coded and two important small changes remains that are -
1) making an optimize() function according to mlpack way of optimization
2) evaluate() function that is used to input the function to optimize

moreover Boost test remains of which i am not aware much 

the above 2 things mentioned will take me one more day to complete..
Also then code clean and passing all 3 builds remains with changes to be made specified by my mentor.

My next weeks goal is to get familiarize with the ann code base and to be able to implement this new optimizer successfully
with good results. Or maybe if my mentor suggests to write some tests i'll be happy to start with that.. :)
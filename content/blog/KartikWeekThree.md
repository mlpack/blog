Title: Neural Evolution Algorithms for NES games - Week 3 Progress
Date: 2017-06-25 01:13:00
Tags: gsoc , neural_evolution
Author: Kartik Nighania

My last week totally went on fixing the CMAES code. It took me a lot of time as the code was
a bit long. But fortunately it works now.
Also certain changes are made for it to support armadillo mat and vec that the previous 
memory pointer passing.


this PR is not yet merged but will be very soon (*fingers crossed*).


BOOST test code is also made referring the test code of stochastic gradient descent..


The next work is to implement the neural network code to do the real evoultion on games.
it will use the ann code in the MLPack library in conjuction with the cmaes optimizer.
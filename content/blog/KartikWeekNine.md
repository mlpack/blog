Title: Neural Evolution Algorithms for NES games - Week 9 Progress
Date: 2017-08-14 19:20:00
Tags: gsoc , neural_evolution
Author: Kartik Nighania

This week was amazing for me. I completed CNE optimizer that converges based on probability. Two things that really speeded
up the process for me was below mentioned paper and last year gsoc student Bang Lui code implemented using his own genome
class structure.  

- "[Training Feedforward Neural Networks Using Genetic Algorithms](http://www.ijcai.org/Proceedings/89-1/Papers/122.pdf)"
- "[Evolving Artificial Neural Networks](http://www.cs.bham.ac.uk/~axk/evoNN.pdf)"

The CNE optimizer have been implemented based on the structure that has tobe followed in MLPack optimizers. Also the code
very well uses the armadillo library and its functions.
My mentor helped me throughout and provided the necessary start points and fast code reviews and corrections.

Boost test case have been written for-

- simple XOR Task
- logistic regression using CNE optimizer
- Vanilla network trained and tested on a larger dataset. (Thyroid dataset in this case)

Apart from that a complete doxgen tutorial have been made. Where step by step example code along with the alogrithm have 
been listed -

- Detailed explanation about the constructor parameters and how to use it.
- About feed forward neural network library and how to use it using simple code.
- Putting it all together and then training a vanilla network for XOR task with a complete example.
- using the optimizer with other model. We converged logistic regression model over here along with sample code.

So now the PR is ready to be merged.

The next part is the most important and interesting part where i will get to run the NEAT implementation of the code 
on the legendary game Super Mario Bros. The code was implemented previously by Bang Lui using his very nicely implemented
genome, species and popluation class. But shows a glitch somewhere in between that stops it to complete level 1. 
Connection is made using Lua scripts and data is transferred using JSON format. My mentor zoq have already done that.
My work would be to find the bug and hopefully get the PR merged in the main repository. 
Title: Summary of Evolution Algorithms
Date: 2017-08-29 06:08:00
Tags: gsoc, neuroevolution, CMAES, CNE, NEAT, HyperNEAT
Author: Kartik Nighania

## Project Goals

My Google Summer of Code project was to create neural evolution algorithms for NES games.
under which:

- CNE: Conventional Neural Evolution.

- CMAES: Covariance Matrix Adaptation Evolution Strategy.

- NEAT: Neural Evolution through Augmented Topologies.


and HyperNEAT which is exactly same as NEAT but the gemones go through a substrate layer to get the links has to be implemented. All the evolution algorithms as planned before was supposed to be neural network optimization algorithms. But we later switched to using it as a generalised optimizer which can be used with other functions and machine learning methods, like logistic regression class implemented in MLPack as well. Therefore CMAES and CNE were designed as an optimizer.



## CMAES Implementation

### My working PR (ready)
This PR is all set to get merged [PR 938](https://github.com/mlpack/mlpack/pull/938)


### References
The research paper that I referred for this algorithm is:

[The CMA Evolution Strategy: A Tutorial](http://www.cmap.polytechnique.fr/~nikolaus.hansen/cmatutorial110628.pdf) by Nikolas Hansen.


### Medium Blog Post
I have a medium blog describing how this algorithm works followed by describing MLPack open source library and a full code tutorial showing the optimization in action. 


[CMAES algorithm in C++ using MLPack](https://medium.com/@kkstrack/cmaes-algorithm-in-c-using-mlpack-1a233af7a1f7)


### Test Cases
CMAES algorithm works by using clever probability distribution (using a modifiable Gaussian distribution) and moving the mean to minima and updating the covariance matrix in the process.
Unlike other derivative methods for optimization this method is great for discontinuous and ill conditioned functions. Therefore one of the performance test was done using Rosenbrock function and that too iteratively upto 50 dimensions. A change in 1e-5 in values leads to very different results. Alot of time was spent to make the algorithm better and removing some major bugs. I can confidently present the optimizer now which works perfectly giving accurate results each time.


### Tutorial
A full descriptive tutorial on using CMAES has been added in the documentation covering step by step:
- The CMAES optimizer class in short.
- Making the function Class.
- Setting up the constructor.
- Complete code example.
- Using as optimizer with other models.


This PR was very challenging for me. The time I decided was way too much less than actually needed. Also during this time I was new to armadillo library for which my mentor came to the rescue. I made a lot of modifications to the PR and also spend alot more in debugging. This PR was indeed a bit scary learning experience. But finally this PR got completed after optimization, improvements and bug fixes.




## CNE Implementation

### PR (merged)
This PR is merged. [PR 1088](https://github.com/mlpack/mlpack/pull/1088)

Divided into three sections:

- [Optimizer](https://github.com/mlpack/mlpack/commit/7af5fd18639740e2cf375333d17393dae39f045a)

- [Test Cases](https://github.com/mlpack/mlpack/commit/99ce3b99b1b0adbec1d6d98f75b981e31f6c2c4e)

- [Tutorial](https://github.com/mlpack/mlpack/commit/49ff33b042e638de67d0c028b15562fb55cf5ab1)


### Optimizer
 Conventional Neural Evolution implemented in MLPack is an optimizer that works like biological evolution in nature which selects best candidates based on their fitness scores and creates new generation by mutation and crossover of population. This then keeps on repeating iteratively till several generations after which healthy candidates are found which perform well in getting the desired output. 


### References
The research paper and reference code that I used to learn CNE were:

- [Training Feedforward Neural Networks Using Genetic Algorithms](http://www.ijcai.org/Proceedings/89-1/Papers/122.pdf)
- [Evolving Artificial Neural Networks](http://www.cs.bham.ac.uk/~axk/evoNN.pdf)
- [Multineat](http://multineat.com/index.html)
- [PR 753](https://github.com/mlpack/mlpack/pull/753)


### Test Cases
Test cases were written for three very different scenarios.
- Optimizing a given function: XOR function.
- Optimizing a vanilla network: It worked for both iris dataset and the thyroid dataset. 
  But for making the test case faster only iris dataset is used.
- Testing with MLPack existing model: Logistic regression model was given the optimizer to
  learn a dataset.


### Tutorial
A full descriptive tutorial on using CNE has been added in the documentation covering step by step:
- The CNE optimizer class in short.
- The constructor parameters.
- Creating a model using MLPack's ANN Class.
- Complete code example.
- Logistic regression using CNE as an optimizer.

This is my first merged PR for any open source project which now rests peacefully in MLPack servers. CNE was not as painful as CMAES and as always my mentor provided his valuable suggestions and code reviews. I loved working on it completely.




## NEAT Implementation

### My Working PR
This PR is not yet complete. [PR 1105](https://github.com/mlpack/mlpack/pull/1105)


### Reference
The main reference paper for NEAT algorithm that i went through is:


- [Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf).


Also a very beutiful implementation video is present on youtube that is worth watching:


- [SethBling MarIO](https://www.youtube.com/watch?v=qv6UVOQ0F44)
- [SethBling marIO code implementation](https://pastebin.com/ZZmSNaHX)
- [Bang Lui PR 752](https://github.com/mlpack/mlpack/pull/752)


This class is already made by previous GSoC 2016 participant Bang Lui and so rather than reinventing the wheel my work was to make it live again and fix an important bug.



 Reading his code was really a nice experience and I think it is one of those best ones in which u can see classes for neurons, links and using them a new class genomes (which is a neural network having links and neurons) and then species as a cluster of genomes and finally population as a cluster of species. To see the true essence of classes and object oriented programming so beautifully implemented.



Some of my time went on to make this one year old PR live and working again. I made more than 270 indentation fixes and other code optimization and style fixes that does not get caught by the cppCheck bot. A tutorial for documentation is also under process. I was able to find some errors which created some critical changes in evolution. Also changes are under testing and debugging for now.





## Future work
My future work is to complete NEAT till it gets merged successfully. Looking at the work done by Bang Lui the code is worth fixing and pushing to the codebase. For hyperNEAT which is a small extention to NEAT a new PR will follow which is not a major task. 


I loved the idea of adding [gaussian process implementation](https://github.com/mlpack/mlpack/issues/851) to MLPack in one of the issues. I would love to contribute for this later.




## Conclusion
I would like to thank MLPack for giving me a chance to contribute to this beautiful library. I have a very different perspective for open source now. A big thanks to my mentor Marcus Edel for tolerating me. There were multiple times i asked for his help and he always responded in no time and with a lot of patience. Also the detailed code review and improvements that he suggested were unmatched and clearly ensure that good quality code gets in the main codebase. Thanks to Ryan for the code review and final edits. Lastly Google for encouraging open source contribution. Looking forward to more contributions from my side and becoming a better engineer.

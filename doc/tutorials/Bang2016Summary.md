@brief Neuroevolution Algorithms Implementation - Summary
@author Bang Liu
@page summary-of-neuroevolution-algorithms-implementation Neuroevolution Algorithms Implementation - Summary
@date 2016-08-22 10:20:00

@section summary-of-neuroevolution-algorithms-implementation Neuroevolution Algorithms Implementation - Summary

In this blog, we summarize our project and our current contributions to `mlpack` project. I wish this will be helpful to anyone who is interested in what we have done, how we did, how to use it, and how to contribute to it if interested.

# Brief Summary

Our project is aiming to implement multiple Neuralevolution algorithms, including CNE, NEAT and HyperNEAT (perhaps implementing more in the future).

Currently, I have created the following Pull Requests:

- My working PR: [PR 686](https://github.com/mlpack/mlpack/pull/686)
- The PR for merging CNE algorithm: [PR 753](https://github.com/mlpack/mlpack/pull/753)
- The PR for merging NEAT algorithm: [PR 752](https://github.com/mlpack/mlpack/pull/752)
- The PR for merging HyperNEAT algorithm: [PR 754](https://github.com/mlpack/mlpack/pull/754)

Currently, the CNE algorithm can be merged after we adjust some coding styles. The NEAT algorithm is finished and tested with a bunch of testings, will will be state in detail in the following. The HyperNEAT algorithm is finished a version and in the progress of debugging by tests.

Before my works being merged to the `mlpack` repository, you can check the most updated implementations under my github account:

[1] Neural Evolution module code:[NE source code](https://github.com/BangLiu/mlpack/tree/ne/src/mlpack/methods/ne)

[2] Neural Evolution tests code:[NE test code](https://github.com/BangLiu/mlpack/blob/ne/src/mlpack/tests/ne_test.cpp)

After they are merged, they can be found in the same directory under `mlpack` repository.

# CNE Algorithm Implementation

The first algorithm is Conventional Neural Evolution (CNE) algorithm. The main reference papers and code for the implementation of CNE includes:

- [Training Feedforward Neural Networks Using Genetic Algorithms](http://www.ijcai.org/Proceedings/89-1/Papers/122.pdf)
- [Evolving Artificial Neural Networks](http://www.cs.bham.ac.uk/~axk/evoNN.pdf)
- [Multineat](http://multineat.com/index.html)

Generally, different neural evolution algorithms are evolving a number of neural networks iteratively to find out a siutable neural network for solving specific tasks. So we first define some classes to represent key concepts in neural evolution algorithms. Including:

1. `LinkGene`: this class defines a link. Basically, a link is defined by the two neurons' id it connected, its own id, and its weight. Detailed implementation is in `mlpack/src/mlpack/methods/ne/link_gene.hpp`.
2. `NeuronGene`: this class defines a neuron. Basically, a neuron is defined by its id, neuron type (INPUT, HIDDEN, OUTPUT, BIAS), activation function type (SIGMOID, LINEAR, RELU, etc.) Detailed implementation is in `mlpack/src/mlpack/methods/ne/neuron_gene.hpp`.
3. `Genome`: this is a critical class. A genome is the encoding format of a neural network. A neural network contains multiple links and neurons. Thus, a genome contains a vector of link genes and neuron genes. Detailed implementation can be found in `mlpack/src/mlpack/methods/ne/genome.hpp`. A novel idea we made is how we calculate a genome's output given an input vector, which is the `Activate` function in the `Genome` class. Briefly speaking, as neural networks in NE algorithms are not in well-defined layered structure, we assign each neuron a *height* attribute. Input neurons are of height 0. Output neurons are of height 1. Heights of hidden neurons are between 0 and 1. Different neurons with same height value cannot be connected (but a neuron can connect to itself to form a recurrent link). In this way, we can have at least three benefits: first, it makes the activation calculation be quite fast (we just need to loop through all links for once); second, calculation logic of any complex neurl network structure is quite clear: neurons are activated in sequence according to its height: from small (0) to big (1); third, different kind of links can be defined by compare the heights of the two neurons it connected. A FORWARD link is connect a small height neuron to a big height neuron.  A BACKWARD link is connect a big height neuron to a small height neuron. And a RECURRENT link is connect a neuron to itself.
4. `Species`: Basically a species contains a vector of genomes which will be evolved by NE algorithms, such as CNE algorithm. Detailed implementation can be found in `mlpack/src/mlpack/methods/ne/species.hpp` .
5. `Population`: Basically a population contains a vector of species. As in algorithms such as NEAT, a number of genomes is not just an array of genomes, but be speciated into different species. Thus, we define the class `Population` to organize a vector of species. Detailed implementation can be found in `mlpack/src/mlpack/methods/ne/population.hpp` .

If each algorithm is a house, then the above classes are the bricks of different style houses. For different algorithms, including CNE, NEAT, and HyperNEAT, the above classes are their basis.

Specially, for CNE algorithm, we define a class CNE, where details are inside `mlpack/src/mlpack/methods/ne/cne.hpp` . For each algorithm, including CNE, NEAT and HyperNEAT, there are same key functions (with different implementation), so that different algorithms can be called in similar style. Here we list some key functions:

1. `Reproduce()`: This is the key function, where how the algorithm evolves its genome groups to get the next generation genomes is defined.
2. `Evolve()`: This is the main function of each algorithm. The whole neural evolution progress is depicted in this function. 
3. `Others`: Other functions are mainly operator functions such as mutate  weight, link or neutron.

Besides all above, we have two more helpful classes defined and being utilized by all neural eolution algorithm classes. 

First, considering a problem: how to evaluate a genome given different tasks to solve? For example, given a same genome, its fitness to XOR task, or to Cart Pole Balancing task, are obviously different. To solve this, we propose to define a task class for each different problem. We test our algorithms with a bunch of tests. Each test task, we defined a corresponding task class. They are inside the file `mlpack/src/mlpack/methods/ne/tasks.hpp`. For example, for the XOR task, we defined class `TaskXor`; for the Cart Pole Balancing task, we defined task `TaskCartPole`, etc. Every task class must implement a `double EvalFitness(Genome& genome)` function, so that different neural evolution algorithms can use this function to evaluate a genome's fitness.

Second, different algorithms will have many parameters. For example, the probability to mutate a weight, the mutate size, the probability to add a new link or neuron, etc. When we create an algorithm instance, we need to specify all these algorithm parameters. If we put all of them as the paramrters of constructor function, the parameter list will be too long. To solve this problem, we define a class `Parameters` which contains all algorithm parameters. Details are in `mlpack/src/mlpack/methods/ne/parameters.hpp`. This way gives at least two benefits: first, we just need to pass a `Parameter` instance to constructor functions of different algorithms, rather than all parameters; second, we can choose the parameters we need to assign values. Different algorithms will share the same parameter name, if they are of the same meaning in different algorithm (for example, all algorithms have the operation to mutate a link's weight. Thus, `aMutateWeightProb` represents the probability to mutate a genome's weight for all algorithms).

# NEAT Algorithm Implementation

The NEAT algorithm is the most critical algorithm we implemented in our project. The main reference paper for NEAT algorithm is: [Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf).

Our detailed class `NEAT` implementation can be found in `mlpack/src/mlpack/methods/ne/neat.hpp`. Compared with CNE algorithm, NEAT contains much more mutate operators. The evolution mechanism is also more complex. To adapt to the increasing complexity, we defined much more functions to model different operators, such as add new link or new neuron. One thing to notice is that the NEAT algorithm also contains a `Reproduce()` function. How to reproduce genomes to get next generation, i.e., how to organize different mutate or crossover operators in each evolution process, is kind of flexible, and also critical to the performance of algorithm. Similarly, `Mutate`, `BreedChild` functions in `NEAT` class are also kind of flexible and can have different implementations.

During the implementation of `NEAT`, we mainly referred to the existing implementation: [NEAT reference](http://pastebin.com/ZZmSNaHX).

An important contribution in our project is that, we implement a bunch of testing tasks to test our algorithms. Currently, we have implemented XOR, Mountain Car, Cart Pole Balancing, Markov/Non-Markov Double Pole Balancing, and Playing Super Mario Game. Here we list the reference materials for different tasks.

`Cart Pole Balancing Problem and Mountain Car Problem`: The materials I referred to for Cart Pole Balancing and Mountain Car problem includes:

- [http://www.ieeecss.org/CSM/library/1993/oct1993/w04-CartpoleExperiment.pdf](http://www.ieeecss.org/CSM/library/1993/oct1993/w04-CartpoleExperiment.pdf)
- [https://github.com/MatKallada/neat-python/blob/master/examples/pole_balancing/single_pole/single_pole.py](https://github.com/MatKallada/neat-python/blob/master/examples/pole_balancing/single_pole/single_pole.py)
- [https://gym.openai.com/evaluations/eval_w8MhbdYUT52bz7dKQrUvA#reproducibility](https://gym.openai.com/evaluations/eval_w8MhbdYUT52bz7dKQrUvA#reproducibility)
- [https://jamh-web.appspot.com/downloads/FAReinforcement_V2.zip](https://jamh-web.appspot.com/downloads/FAReinforcement_V2.zip)

`Double Pole Balancing Problem`: The materials I reffered to for double pole balancing are:

- [https://github.com/CodeReclaimers/neat-python/tree/mstechly-master/examples/pole_balancing/double_pole](https://github.com/CodeReclaimers/neat-python/tree/mstechly-master/examples/pole_balancing/double_pole)
- <u>Evolving neural network controllers for unstable systems</u> by A. P. Wieland et. al (this paper contains the formulations of double pole balancing).
- [https://en.wikipedia.org/wiki/Runge–Kutta_methods](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)

`Play Super Mario Game`: Marcus helps to implemented the testing of playing Super Mario game, and our algorithm successfully passed the first level until now! Detailed implementation and how to repeat the experiment can be found under Marcus's github account: [Playing Super Mario](https://github.com/zoq/nes).

Last but not the least, *how we call the NEAT algorithm to solve different tasks*? First, given a new problem, a user should define his/her own task class, which offers a `EvalFitness` function inside the class. Second, calling NEAT to run evolution is organized in the following steps:

1. Set task parameters and construct a task instance;
2. Set algorithm parameters and construct a `Parameters` instance;
3. Set a seed genome, i.e., the genome used to initialize a population of genomes to evolve;
4. Construct an algorithm instance using the above three input parameters: task, parameters, and seed genome;
5. Call algorithm instances' `Evolve()` function.

For detailed examples, please check  `mlpack/src/mlpack/tests/ne_test.cpp`. 

Here we list a few features that we haven't implement but is going to add soon:

- Save and load genome. So that the learned best genome for tasks can be saved and to solve new inputs.
- Save and load model. So that an algorithm instance can be created by loading a config file, or save to a config file.
- Visualize genome. Currently we visualize genome by printing its links and neurons' information. I wish we can implement a more intuitive graphical method.

# HyperNEAT Algorithm Implementation

The HyperNEAT algorithm is similar with NEAT. The key difference is that the evolved genomes are not used directly, but being applied to a substrate genome to generate the links. The generated genome will be applied to user's task. The main reference for HyperNEAT is: [HyperNEAT](http://eplex.cs.ucf.edu/hyperNEATpage/).

As HyperNEAT needs to query a substrate, i.e., a set of neuron nodes with coordinates, we defined class `Substrate` in the `mlpack/src/mlpack/methods/ne/substrate.hpp`. The algorithm class `HyperNEAT` is defined in `mlpack/src/mlpack/methods/ne/hyperneat.hpp`. Currently we have implemented the HyperNEAT algorithm and it is being tested by various tasks we defined before.

I would like to describe more details about HyperNEAT after it has passed all tests, as we may revise the design a lot during debugging.

# Todos

We have almost achieved all our goals in our proposal. Currently the remain works including:

1. Debugging HyperNEAT to let it pass all tests;
2. Check potential bugs and optimize as much as we can;
3. Clean code and adjust style for merge into `mlpack`.

In the future, maybe we can implement more interesting neural evolution algorithms.

# Acknowledgement

I have enjoied a great summer working on this interesting project! Thanks a lot to my menter Marcus Edel, who has helped me a lot by keep giving me valuable advices during coding, help with debugging, help with implementing Super Mario task, answer all my questions timely with patience, and so on. He is an excellent mentor and I learned a lot from him. Thanks Marcus! Besides, I am also grateful to the `mlpack` team that gives me this chance to participate into such an excited project! Thank you very much!

:)

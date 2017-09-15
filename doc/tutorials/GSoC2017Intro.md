@brief mlpack in Google Summer of Code 2017
@author Marcus Edel
@page GSoC2017Intro mlpack in Google Summer of Code 2017
@date 2017-05-30 18:00:00

@section GSoC2017Intro mlpack in Google Summer of Code 2017

GSoC 2017 just started today, We are very excited to work with 10 awesome
students over the summer. Here is what they will be working on this summer:

### [Better benchmarking](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#better-benchmarking)
**by Dewang Sultania, mentored by Ryan Curtin and Marcus Edel**

Dewang will improve the existing benchmarking system we have in place by
implementing and benchmarking current mlpack methods as well as other
competetive implementations and libaries. He will also work on a makeover of the
visual appeal by introducing new ideas to make the interface more accessible.

Dewang is an undergrad student at Birla Institute of Technology, interested in
algorithms, data structures, and database management systems. When he has free
time, he likes to dance, read sci-fi novels and is the guy you have to ask if
you like rafting.

### [Cross-Validation and Hyper-Parameter Tuning](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#cross-validation-and-hyper-parameter-tuning-infrastructure)

**by Kirill Mishchenko, mentored by Ryan Curtin**

Kirill will design and develop modules for cross-validation and hyper-parameter
tuning in mlpack. Specifically, Kirill will create three separate modules for
working with different mlpack models and methods: (1) cross-validation (the
module can split a training set into some number of folds and evaluate some
average measure over all folds.); (2) hyper-parameter tuning (the module take a
method and tests different values for the training parameters).

Kirill is a Ph.D. student at the Ural Federal Univercity (Ekaterinburg, Russia);
he likes to walk and cycle with friends.

### [Essential Deep Learning Modules](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#essential-deep-learning-modules)

**by Kris Singh, mentored Mikhail Lozhnikov**

Kris will extend the existing network implementation to support RBM that support
Spike and Slab RBM’s, and then implement a system of two neural networks
competing against each other in a zero-sum game framework called Generative
adversarial networks (GANs). Then, he will benchmark the mlpack implementation
against other implementations using the mlpack benchmarking system.

Kris is a master student at the Indian Institute of Technology, Hyderabad; he
likes travel and has been to almost 14 out of 29 in India, which is a lot if you
compare it against other countries like Germany which is about 9 times smaller
than India, okay United States is about 3 times bigger than India, but who has
seen all US states.

### [Frank-Wolfe Algorithm for Sparse Optimization and Regularization of Atom Norms](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#low-ranksparse-optimization-using-frank-wolfe)

**by Chenzhe Diao, mentored Stephen Tu**

Chenzhe will work on an implementation of Frank-Wolfe for the various atomic
norms listed in Jaggi's awesome paper. Moreover, he will test the pieces on real
world problems such as dictionary learning that will call the solver, to give a
further demonstration and comparison of the implementation.

Chenzhe is a Ph.D. student at the University of Alberta; he is far from the only
University of Alberta student who has worked with mlpack in the past, as he is
the third student we have accepted from there. Chenzhe enjoys skiing like a true
Canadian.

### [Augmented Recurrent Neural Networks](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#augmented-recurrent-neural-networks)

**by Konstantin Sidorov, mentored by Marcus Edel and Ryan Curtin**

Konstantin will implement the components of the Hierarchical Attentive Memory
architecture (HAM) including Highway Networks and test it on various tasks. The
pieces of this architecture will be usable for other neural network applications
and will open the possibilities to train even longer sequences.

Konstantin a first-year student in Software Engineering at Astrakhan State
University, interested in playing Go - the ancient Chinese game, you may heard
of it in the news e.g. "AlphaGo retires from competitive Go after defeating
world number one 3-0", I think Konstantin is one of the few members that can
follow and understand the game.

### [Build testing with Docker and VMs](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#build-testing-with-docker-and-vms)

**by Saurabh Gupta, mentored by Ryan Curtin**

Saurabh will redesign and automate the mlpack build process. Specifically,
Saurabh will (1) complete the build matrix (testing mlpack on different
compilers, different architectures, different Boost versions); (2) running
docker with Jenkins (continuous integration and continuous deployment using
plugins to automate the build and deploy process) (3) macOS and Windows builds
(testing mlpack on windows and macOS).

Saurabh is an undergraduate (B. Tech.) majoring in Information Technology and
Mathematics at the University of Delhi. He likes adventure sports and wandering
mountains maybe in the future we can together climb one of the seven summits,
probably we don't start with Everest, but who knows.

### [Neural Network Evolution Algorithms on NES games](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#neuroevolution-algorithms)

**by Kartik Nighania, mentored by Marcus Edel**

Kartik extends and implements the neuroevolution algorithms for the neural
network framework in mlpack, such as CNE, NEAT, and CMAES. These will be tested
on various problems, including applying all these algorithms to NES games. In
addition, benchmarking will be done to verify that mlpack's implementations are
competitive with---or faster than---other implementations of these
neuroevolution algorithms. If time permits he will also work the visual appeal
of the architecture and results.

Kartik is an undergrad student at the National Institute of Technology, Surat,
India; he likes robotics (embedded systems and computer vision), making drones
and playing computer games. Make sure to checkout his
[website](http://www.kartiknighania.com/kartik-nighania.html) and his
[blog](https://kartiknighania.wordpress.com/).

### [Augmented Recurrent Neural Networks](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#augmented-recurrent-neural-networks)

**by Sumedh Ghaisas, mentored by Ryan Curtin and Marcus Edel**

Sumedh will implement the components of the Neural Turing Machine (NTM)
including various tricks to imrpove the overall training process like batch
normalization. The pieces of this architecture will be usable for other neural
network applications and will open the possibilities just like the HAM idea to
train even longer sequences.

Sumedh is a master student at the University of Edinburgh; he likes playing
table tennis in his free time and enjoys listening to the blues.

### [Parallel stochastic optimization methods](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#profiling-for-parallelization)

**by Shikhar Bhardwaj, mentored by Yannis Mentekidis**

Shikhar will implement parallel stochastic optimization methods in mlpack,
namely parallel stochastic gradient descent based on HOGWILD and asynchronous
parallel stochastic coordinate descent based on AsySCD, considering various
available approaches like OpenMP for better efficiency and performance.

Shikhar is an undergraduate student from Delhi, India, studying Mathematics and
Computing Engineering at DTU; He likes to tinker with electronics, everything
from "blink an LED with a 555 timer" to "set up a microcontroller with few
sensors", looks like this year we have two students who know a lot about all
this little building blocks that enable us to write code on a computer instead
of using pen and paper.

### [Reinforcement Learning Framework](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#reinforcement-learning)

**by Shangtong Zhang, mentored by Marcus Edel**

Shangtong will implement a Reinforcement Learning framework and will compare the
implementations against other competetiv methods. Specifically, Shangtong will
work on (1) DQN (Double DQN algorithm - adds stability to the learning by using
a Q evaluation); (2) A3C (Asynchronous Actor-Critic Agents is probably the
universal agent that can be used as a stable baseline for solving various tasks)

Shangtong is a master student at the University of Alberta; he likes to run, and
if I say run I don't talk about run around the block a few times, no he runs
21-43 km (half marathon/marathon).


You can find more information on each of the projects on the [Summer of Code website](https://summerofcode.withgoogle.com/organizations/5066356388003840/).

Anyway, congratulations to Dewang, Kirill, Kris, Chenzhe, Konstantin, Saurabh,
Kartik, Sumedh, Shikhar, and Shangtong! The coding period starts today (May 30).
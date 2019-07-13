@brief NEAT & Multiobjective Optimization
@author Rahul Ganesh Prabhu
@page Rahul2019Week05 NEAT & Multiobjective Optimization - Week 5
@date 2019-06-30 8:30:00

@section Rahul2019Week05 NEAT & Multiobjective Optimization - Week 5

This week I was finally able to finish debugging my NEAT implementation and got some good results. It performs well on the XOR test, reaching total squared error under 0.5 within 100 generations with a population size of 100 consistently. I also reworked my implementation of a cyclic neural network and tested NEAT on the Double Pole Balancing Test. When provided with all information, the algorithm performs exceedingly well, with the initial population itself normally being able to balance the poles (presumably by wiggling the cart back and forth). However, if velocity information is hidden from the cart, the algorithm is struggling to find an agent that can go further than 400 time steps. I think it's because of the fitness function and the parameters though, and I am making the implementation of the test more consistent with the paper and other implementations.

I also noticed that the API for the RL environments in mlpack were inconsistent, which broke the code I had written for templatized wrappers of the environments. Moreover, I made a pretty big mistake in my implementation of the multiple pole balancing environments, causing it to segfault. I opened a PR for this (see [#1941](https://github.com/mlpack/mlpack/pull/1941)). Once this is merged, the API of the environments should be uniform and they will have the option to terminate after a certain number of steps.

Over the next week or two, I plan to:

- Finish testing and decided on a group of tests to include in the final testing framework.

- Address the review comments on #1941 and the NEAT PR. In the process of doing this, I'll revise my code and clean it up.

- Add support for a config file and serialization in NEAT. This will give the user adequate customizability as well as the ability to save progress.

- Implement Phased Searching, where the population undergoes phases of complexification and simplification, to prevent genome bloat, which is a phenomenon where genomes become larger and larger over time with little increase in performance.

- Perhaps use OpenAI to record NEAT's performance on the OpenAI Gym? That would be pretty neat! (pun intended, sorry :P)

Something interesting I noticed was that NEAT actually does not need innovation IDs. The paper uses them as "historical markings" and to compare different topologies. It states that equivalent mutations within the same generation must recieve the same innovation ID. However,if implemented like this, it leads to an explosion of innovation IDs, reaching the 2000 or 3000s very quickly, and slowing down speciation. It then occurred to me that these innovation IDs were in fact just unique IDs for a connection, and every equivalent connection across generations must have the same ID for speciation and crossover to work. On further inspection, I realized the python implementation does not use innovation IDs, while SharpNEAT uses it purely for K-Means speciation. On making these changes, I was able to make a 3x speed-up of the implementation.

My favourite album this week is **The Miseducation of Lauryn Hill** by **Lauryn Hill**. I had listened to a lot of her work as part of the The Fugees, but not this solo album. It's a classic soul and R&B album, check it out!

Thanks for reading!

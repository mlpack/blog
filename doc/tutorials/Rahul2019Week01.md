@brief NEAT & Multiobjective Optimization
@author Rahul Ganesh Prabhu
@page Rahul2019Week01 NEAT & Multiobjective Optimization - Week 1
@date 2019-06-01 23:30:00

@section NEAT & Multiobjective Optimization - Week 1

Having been selected for GSoC 2019, this is my first major contribution to the open source community. This summer, I will be implementing NeuroEvolution of Augmenting Topologies (NEAT) as well as the framework for multi-objective optimization in ensmallen. My mentors for this project will be **Marcus Edel** and **Manish Kumar**.

After discussing the project with my mentors, I finally started on the project this week. During this week, I have:

-Implemented a multiple pole balancing environment (see [#1901](https://github.com/mlpack/mlpack/pull/1901#pullrequestreview-242319420)). This will be useful to create a double pole balancing environment to test NEAT on.

-Implemented a test suite for NEAT. The test suite includes both the discrete and continuous reinforcement learning environments in mlpack, as well as the XOR test and the aforementioned double pole balancing environment.

-Implemented the Gene class for NEAT. This will represent the connections in the neural networks NEAT will create.

-Started on the Genome class implementation for NEAT.

To keep writing these blog posts interesting for me (and hopefully the readers too!), I want to include two things in all my blog posts.

The first being something I learn from being in GSoC every week, which hopefully could help someone else out there :). This week, I accomplished less than I had expected to, mostly because of poor planning on my part. Clearing my head and writing all my ideas on paper really helped, and it'll definitely speed up the implementation. I've realized it's pretty important to slow down for a bit and map things out before such a large and complicated project.

The second is just some music that I want to share, specifically the music that helped me stay in the groove during long coding sessions this week. This week my favourite is **The Mouse and The Mask** by **Danger Doom**. Worth a listen if you're into rap or maybe some old Adult Swim :).

Thanks for reading!

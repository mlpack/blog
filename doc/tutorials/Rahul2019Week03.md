@brief NEAT & Multiobjective Optimization
@author Rahul Ganesh Prabhu
@page Rahul2019Week03 NEAT & Multiobjective Optimization - Week 3
@date 2019-06-16 19:30:00

@section Rahul2019Week03 NEAT & Multiobjective Optimization - Week 3

This week I implemented the higher levels of NEAT - reproduction, speciation and the main loop of the algorithm.

Speciation divides the genomes into groups called "species" to protect topological innovations from dying out too quickly, by making them compete only within their own species. In the original paper by Kenneth Stanley, speciation is done by means of a compatibility metric. However, Colin Green found that speciation can be done more efficiently through K-Means Clustering, which is what I have implemented.

Reproduction is the mechanism by which new genomes are created from old ones. This is much like other genetic algorithms, involving crossover followed by mutation of the child genome. Reproduction is only done within a species.

The main loop brings all of this together and performs Evaluation -> Speciation -> Reproduction in a loop for a set number of generations. Now that this is done, I'm done with the basic implementation of NEAT. Now I must test and debug the code. It's quite tedious and time consuming, considering build times. Hopefully I can get it working soon. I'm currently facing issues where DualTreeKMeans(and other LloydStep variants probably) throw memory access errors, so I've switched to NaiveKMeans for the time being. Moreover, evaluation inexplicably stops at the 8th genome, where it enters an infinite loop for reasons I don't really understand. Hopefully over the week I'll get a handle on things, and be able to provide some meaningful test results.

As for what I learned this week, I can't point towards anything in particular unfortunately. I have realized, though, how compiler errors are sometimes horribly difficult to understand, especially related to templates. A lot of my time was spent wrestling with comprehending errors and warnings this week. I suppose that's something experience will cure.

This week I mostly listened to jazz, since I'm planning to learn to play the saxophone. It's hard for me to pick a favourite, but I quite enjoyed John Coltrane's **A Love Supreme** and Miles Davis' **Kind of Blue**.

Thanks for reading!

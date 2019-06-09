@brief NEAT & Multiobjective Optimization
@author Rahul Ganesh Prabhu
@page Rahul2019Week02 NEAT & Multiobjective Optimization - Week 2
@date 2019-06-09 23:30:00

@section Rahul2019Week02 NEAT & Multiobjective Optimization - Week 2

This week, I worked on building the basic building block for NEAT - the Genome. The genome is the encoding for the neural networks forming the population of NEAT. Besides that, I worked on the implementation of the Phenomes, which are the decoded neural networks that genomes represent. There are two types - cyclic networks, for RNNs, and acyclic networks, for FFNs. When an input is passed to a genome, it is decoded into a phenome which is used to evaluate the input and spit out an output.

For the next week, the plan is to work on the main NEAT algorithm, which will bring everything together. I'll be writing the code for reproduction of genes, their speciation, and the main loop for the algorithm. Hopefully I'll have all the code finished before the first evaluation, after which we can focus on testing and improvements. I'm pretty happy with how progress is going now, despite being sick for a couple days.

Something interesting I learned during the course of this week is how compiling and "making" is done in C++. After a conversation with Ryan, I realized I know next to nothing about how building is done in mlpack (except that it's done by CMake) and how compiling is done in general. I read up on it, and I now have a much deeper understanding on the topic and what exactly is happening under the hood.

I listened to a lot of instrumental music this week to help keep me focussed, and I have to say my favourite is **Modal Soul** by **Nujabes**. Check it out!

Thanks for reading!

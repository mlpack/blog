@brief Neuroevolution Algorithms Implementation - Week 14
@author Bang Liu
@page Bang2016WeekFourteen Neuroevolution Algorithms Implementation - Week 14
@date 2016-08-21 17:43:00

@section Bang2016WeekFourteen Neuroevolution Algorithms Implementation - Week 14

During the last week, we have changed the design of HyperNEAT to avoid class inheritance, and implemented it and its first test case: XOR. We are now debugging this algorithm as it hasn't pass the test. Until now, we have figured out multiple critical bugs through the debugging of XOR. One is the Genome classs's Activate() function. Previously it may skip some neuron's activation due to the disabled links. Another is NEAT's MutateAddNeuron(). Previously it will generate duplicated links. After we figured out why, the problem is now solved. We have re-run previous NEAT's test cases, and they passed.

Now the CNE algorithm is ready to merge once we adjusted its style. The NEAT algorithm may be merged after debugging HyperNEAT. As we may figure out more potential bugs during the debuggingof HyperNEAT, and thus we can optimize it.
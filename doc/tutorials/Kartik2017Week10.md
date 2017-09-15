@brief Neural Evolution Algorithms for NES games - Week 10
@author Kartik Nighania
@page Kartik2017WeekTen Neural Evolution Algorithms for NES games - Week 10
@date 2017-08-21 23:51:00

@section Kartik2017WeekTen Neural Evolution Algorithms for NES games - Week 10

This week started by working on my previous PRs.

After some small final touches the CNE PR is ready. My mentor provided very detailed code review.
The time that he put into for finding small spaces and other style issues that I missed in between
code really ensures that MLPack gets good quality code merged. I am even now more familiar with the codebase and is doing a lot less mistakes.

The next was again working with the CMAES Repo


- The next task was a -nan error that i used to see rarely during test results.
- Also the optimization will some time go a bit wrong and will create very minute deviation from the exact answer. I was converging rosenbrock function for 45 dimension and a very small deviation leads to a different output.


Both the errors got solved and this algorithm now creates accurate result and no error is seen at any time. To make sure i even ran hundreds of iterations in my local machine.


Next was NEAT PR -


The paper i went for is-
- [Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)


also code from sethBling with his famous marIO video on genetic algorithm was helpful.

I finished reading the codebase by last year contributor Bang Lui and is setting up my local machine for 
 running and testing the game today.


This week will be to debug the whole process and see for potential errors in the code.
Also adding a tutorial for NEAT will add my small contribution too :)
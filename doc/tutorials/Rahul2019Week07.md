@brief NEAT & Multiobjective Optimization
@author Rahul Ganesh Prabhu
@page Rahul2019Week07 NEAT & Multiobjective Optimization - Week 6 & 7
@date 2019-07-13 18:30:00

@section Rahul2019Week07 NEAT & Multiobjective Optimization - Week 6 & 7

Unfortunately I was unable to post a blog last week, since I was out of station visiting relatives. I'll be including last week's progress in this blog as well.

These last two weeks have been very eventful, and I think we are close to finishing off the NEAT project now.

- Implemented serialization in NEAT. Now, the user can save his progress and restart at a later time, or create an XML config file to describe the parameters of the NEAT model you plan to use.

- Implemented phased searching, which is a searching scheme proposed by Colin Green, where we perform alternating complexification and simplification. This is done to prevent "genome bloat", which is a problem with some neuroevolution techniques where the network keeps growing with negligible change in fitness.

- Implemented support for the user describing a starting point for the search, by providing a starting genome. The implementation detects whether a starting genome has been provided using SFINAE in the form of enable_if (See [this blog](https://www.bfilipek.com/2016/02/notes-on-c-sfinae.html) for an explanation of SFINAE).

- Used Marcus' OpenAI Gym API to record NEAT's performance on a cart pole environment. Unfortunately, I keep getting a boost_system error when I run the code, but Marcus did, and was able to get [this result](https://gym.kurg.org/openaigym.video.9.40957.video000000.mp4) (AIGym only runs episodes for 200 steps). The cart pole test is extremely easy for NEAT to solve, since it can be done without any hidden nodes, but visualization of an algorithmn and it's work is always really cool :)

- Polished the code and corrected some mistakes. There's still more to do though!

- Finally found the issue with the non-Markovian double pole balancing environment. Though the paper does not mention it, the double pole balancing environment needs	the fourth order Runge-Kutta method to find the next state. After including this, NEAT was able to solve the environment.

Now that all this is done, I think I will be done with NEAT in time for the second evaluation. Before that, some more work needs to be done, which I plan to do over the next week:

- Write a guide for NEAT, since it's usage isn't self explanatory.

- Write neat_main.hpp, which is for bindings.

- Think of a test for phased searching, and implement it.

- Go through the code and clean it up to be ready for review. There are also some small parts that may need a rewrite, such as the tournament selection algorithm.

- Open a PR to fix the multiple pole balancing environment to use RK4. As it turns out, the environment is also incompatible with mlpack's learners due to how I implemented it. Unfortunately, to make it compatible, it will lose it's generality and be a purely double pole balancing environment. I suppose this is fine since I have never seen a three or four pole balancing environment in any literature, but it's a shame nonetheless. It also occurred to me that we seem to be running into problems like this a lot. To prevent this from happening again, I plan to add unit tests where we use learners on the environments, to make sure they have the necessary API and are compatible with our learners.

Something I learned in these last two weeks is how useful it is to maintain a board with your plans, priorities, etc. Inspired by Ryan and Marcus' boards on GitHub, I made one myself on Trello, where I've detailed all the new stuff I want to learn, watch, read and implement. It's amazing how much clearer my mind is now, I've thought of so many cool things I want to do. I strongly suggest others to try out the same, it's pretty great.  

I don't have a music recommendation for the last two week, but I did recently buy an alto saxophone. I still sound like I'm strangling a cat or moving furniture. Practice will make perfect though :)

Thanks for reading!

@brief Neural Evolution Algorithms for NES games - Week 6 + 7
@author Kartik Nighania
@page Kartik2017WeekSixSeven Neural Evolution Algorithms for NES games - Week 6 + 7
@date 2017-07-27 02:50:00

@section Kartik2017WeekSixSeven Neural Evolution Algorithms for NES games - Week 6 + 7

these 2 weeks on writing some more test cases for the CMAES algorithm. I faced a lot of difficulties along the way also and had to spend a lot of time on errors.
i implemented logistic regression using CMAES which is working well and is able to classify accurately.
the rosenbrock function which was used as a test case only converges for 2 dimensions giving accurate value and very close to zero optimization.
The test case fails for functions having higher dimension. I tried a lot of different alterations and spent a lot of time in fixing this but i mostly ended up with flat fitness 
due to which convergence stops in between.

the next was implementing the CMAES optimizer on neural networks. At very high number of iterations the CMAES is able to optimize the vanilla network but fails at small number of evaluations which
it is supposed to do because it will be used in almost real time. 
I tried to fix this using tuning the parameters of the function but nothing happened. Im still working on this and trying to get it converge fast.

If that does not happen in the next 1 days. I will try to rewind the whole commit to the stage where armadillo library was not implemented and carefully change the things to correct
the error, because before when it was implemented in purely C language, I was able to converge rosenbrock for higher dimensions as well. this looks promising and if needed i will spend the time it
will take to do so.

Moreover, i was also in busy in my campus placement last week for software engineering job and due to which I was not able to give a lot of time in last week. Finally I am placed now. 
I am 2.5 weeks behind schedule and will have to pace if selected in second evaluation to complete my gsoc project before time.
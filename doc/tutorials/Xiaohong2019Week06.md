@brief PPO - Week 6
@author Xiaohong
@page Xiaohong2019Week6 Proximal Policy Optimization - Week 6
@date 2019-07-07 19:40:08

@section Xiaohong2019Week 6 Proximal Policy Optimization - Week 6


This week, I am implementing the `Update()` function in ppo_implement.hpp. This 
function is used to update the model of actor and critic. Actor and critic model
use different loss update and updated respectively. 

The actor model is updated by mean square error, which is normal in ML/DL model.
The challenge of this part is that how to optimize the surrogate loss function 
for the actor model. There are two primary variants of PPO: PPO-Penalty and 
PPO-Clip. I am going to implemented the PPO-Clip next week. 

 

@brief PPO - Week 5
@author Xiaohong
@page Xiaohong2019Week4 Proximal Policy Optimization - Week 5
@date 2019-06-29 18:17:11

@section Xiaohong2019Week 5 Proximal Policy Optimization - Week 5


This week, I focus on how to store the transition into experience replay
buffer. The previous codebase only supports the discrete task, so I
spent some time in the continuous task.

With the help of zoq, I got two solutions on how to store the continuous task's
action. One is using the `std::vector` to store the action, while the other
is using compact the attribute of action into one column. I tried both of
them, I choose the `std::vector` in the end. There are some misunderstanding
during the coding period, it is due to my careless.

Thanks for reading :). What's more, I updated my travel note, there are many
beautiful sceneries. If you are interested
in it, please refer to [the page](https://zhuanlan.zhihu.com/p/69014831).
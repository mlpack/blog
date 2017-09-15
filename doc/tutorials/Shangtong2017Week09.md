@brief Deep Reinforcement Learning Methods - Week 9
@author Shangtong Zhang
@page Shangtong2017WeekNine Deep Reinforcement Learning Methods - Week 9
@date 2017-08-12 22:30:00

@section Shangtong2017WeekNine Deep Reinforcement Learning Methods - Week 9

This week I released the PR for async one step q learning and async one step sarsa, it's under review now and I believe it will be merged soon. I also worked on A3C. I implemented a wrapper network for actor and critic, and added a new `reinforce` layer for policy gradient. Current architecture of `ANN` doesn't support shared layers, which is necessary in A3C. Use `shared_ptr` can address this problem, however it may lead to overhead and may make it inconvenient for user to add new layer types. After discussing with Ryan, we decided to use `AliasLayer`, the main challenge is to make it compatible with member function checkers like `HasParameters()`. I thought I could address this issue by overloading or specializing `boost::apply_visitor` before, but soon I realized it's impossible. Maybe I have to add overload functions for `AliasLayer` template argument for all visitors.
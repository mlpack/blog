Title: Deep Reinforcement Learning Methods - Week-10 Highlights
Date: 2017-08-20 21:00:00
Tags: gsoc
Author: Shangtong Zhang

This week I mainly worked on the issue of sharing layers between two networks. We finally figured out that `Alias` layer is the only possible solution, because the memory should be contiguous -- `shared_ptr` cann't do that. However the implementation of `Alias` layer is not easy. I managed to eliminate the strange `void*` and make the `include` clause elegant by rearranging all the visitors. However I sill got stuck with a stange bad memory access error. I spent two days with no progress. So I decided to come back to the implementation of A3C, without shared layers.

Title: Finalized Parallelization, Week 1 of Modeling LSH
Date: 2016-07-12 20:20:20
Tags: gsoc, lsh, parallel, modeling
Author: Yannis Mentekidis

This week's work can be organized in two sections - Finalizing LSH Parallelization and Beginning the LSH Model.

## Parallelization

On the parallelization front, I did some experiments regarding the static or dynamic scheduling of threads, and applied an OpenMP reduction pattern to remove all thread locks in the parallel loop.

Scheduling of threads is an important part of parallelization - load balancing is a very interesting topic and OpenMP has a few nice predetermined modes you can ask for. The basic three are static, dynamic, and guided. 

**Static** scheduling is, well, the static assignment of constant portions of work ("blocks") to threads, for example saying thread 1 will execute loops 1:4, thread 2 loops 5:8 and so on. This is the simplest and lowest-costing work scheduling scheme. 

**Dynamic** scheduling does the same thing with the slight difference that, after the portions of work are divided, if a thread finishes its job it is assigned a new block to process. For iterations of unequal length, dynamic scheduling is usually good because it doesn't allow threads to slack after they finish their allocated block. 

**Guided** scheduling reduces the block size as time progresses, assigning smaller and smaller blocks. This is useful for situations where, as the loop progresses, iterations last longer, so it is better to schedule work as it comes.

In our case, because different query points might have varying candidate set sizes, going with Dynamic was the best choice even though the scheduling overhead is nontrivial. Running a few tests confirmed that theory - for most datasets, Dynamic scheduling was faster than Static.

## Modeling LSH

Now that Multiprobe LSH is implemented and working, I've started examining my next planned contribution - attempting to predict values for each parameter (W, M, L, T - Hash width, Number of Projections, Number of Hash tables, Number of Additional Probes) that will have satisfactory recall (= level of approximation) with the lowest possible cost (interpreted as time or selectivity).

The paper [Modeling LSH For Performance Tuning](http://dx.doi.org/10.1145/1458082.1458172) proposes a model of LSH and the data distribution that is able to produce estimations of recall and selectivity based on a set of parameters and a small sample of the dataset, to which the parameters of a specific data distribution (the Gamma Distribution) are fit.

The authors' approach is very theoretical, and although they do produce usable mathematical results, they do not explain how to implement them in code - they are more interested in the *what* the model does, not *how* it does it.

So, my task is to decrypt their mathematical formulas and bring them to computable form. This might prove to not be a trivial task, but I have already started diving into the specifics and I hope I will be able to produce at least a prototype by this week's end.
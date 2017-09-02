Title: Deep Learning Module in MLpack(Week 3)
Date: 2017-06-22
Author: Kris Singh

### Week Three
This week I tried to finish the PR of the BinaryRBM implmentation.
I expected t is would not take much time. But as the famous saying goes "We make plans and god laugh". Most of the time this week was spent in debuggin the existing implmentation of the RBM implementation.This code majority of my time this week though the code alse went through some major changes. 
Some of the major Changes it underwent were as follows:
1. Change of the evaluation function
2. Major Style Fixes
3. Cd-k code addition.
4. Addition of batch training to cd-k algorithm

The important thing I learnt this week how important is to intialise the variable.

We finally were able to solve the problem of training and we kind of get okay results now have a look here.
Here is parmaeters list we got results by.
cd-1, batch size: 20, learning rate:0.1

<p style="text-align: center;">The samples are generated from 1-step gibbs sampling.</p>
<p style="text-align: center;">
<img src="images/mnist_50K_sample.jpg" style="float:left;" width="200" height="200" hspace="10"/>
<img src="images/mnist_250_sample.jpg" style="float:left;" width="200" height="200" hspace="2"/>
<img src="images/mnist-binary.png" width="200" height="200" hspace="2"/>
</p>
<p style="text-align: center;">The last image uses mnist-binary dataset with threshold value of 0.2</p>

### Next Week
I had hoped to finish Binary RBM in the previous week but now it has to be extended this week. Major goals for this week include
1. Writing test for Binary RBM(write now i am planning to add reconstruction loss and classification accuray as test)
2. Merge Binary RBM PR
3. Start with ssRBM

*Hopefull this week we would be able to achive are targets. :)

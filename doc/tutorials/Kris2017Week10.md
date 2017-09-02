@brief Deep Learning Module in mlpack - Week 10
@author Kris Singh
@page Kris2017WeekTen Deep Learning Module in mlpack - Week 10
@date 2017-08-10 13:00:00

@section Kris2017WeekTen Deep Learning Module in mlpack - Week 10

### Week Ten
The past week has seen some good progress. I was finally able to finish the
ssRBM & binary RBM PR. I also made some progress on fixing the GAN network.
Mostly I just cleaned up the code for the GAN network and just added a diff
rent initialization strategy( Insitalising weights based on per layer basis).
This actually fixed the error with the vanishing gradients that we were experincning with the GAN PR. I also a added a simpler test to check our
implementation of this was based upon the Edwin Chen's blog and the test
that Goodfellow's original paper is based on. Though the test meant more for showing that the generated outputs are very close to the real data.

The goal for the next week is mainly finishing up with the GAN PR. The major
problem as pointed out by Mikhail is that of the CreateBatch function. I think
that needs refactoring.
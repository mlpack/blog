@brief Collaborative filtering package improvements - Week 5 + 6
@author Sumedh Ghaisas
@page Sumedh2014WeekSix Collaborative filtering package improvements - Week 5 + 6
@date 2014-07-10 00:00:00

@section Sumedh2014WeekSix Collaborative filtering package improvements - Week 5 + 6

Finally after 6 weeks Collaborative Filtering model of MLPACK has 2 more SVD algorithms
namely SVDBatch and SVDBatchWithMomentum. As these algorithms share many common features 
they are implemented in a single update rule of Alternating Matrix Factorization module.
As SVD can also decompose matrices with negative entries now CF module can use some 
preprocessing techniques which involves adding negative entries. 
Along with this major thing many important changes have been introduced in AMF module

1) Addition of Termination Policies 
  SimpleResidueTermination: Termination policy used in old NMF implementation.
  ValidationRMSETermination: New termination policy introduced for SVD implementation.
  SimpleToleranceTermination: somewhat hybrid between residue termination and tolerance of validation termination
2) Addition of tests for SVDBatchWithMomentum

SVD incomplete incremental learning is under testing so completing that update rule is going to be my next task.
Ohh and all these update rules need to be added to CF executable. Many more ideas to implement, providing simple
typedefs so users can make use of these without knowing the internal template functionality. And many more to come...
Thank you for visiting...
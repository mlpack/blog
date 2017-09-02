Title: Collaborative filtering package improvements : Week 3-4 Highlights
Date: 2014-06-17 07:30:00
Tags: gsoc
Author: Sumedh Ghaisas

Week 4 is over. Had fun with segmentation faults and undecodable generic programming errors. :)
In past week the following things have been added to the AMF module -

1) The stopping criterion is shifted from minResidue to tolerance measurement between two iteration. This Helps terminate 
   both NMF and SVD factorizations.
2) Each call to AMF apply (actual factorization function) will call Initialize on given update rule before starting the 
   procedure of alternating updation. This will allow update rules to have local variables.
3) Added SVDBatchLearning update rule. Tested on MovieLens and matrices with neagative entries.
4) Added momentum to BatchLearning which decreases its time overhead while maintaining the efficiency.

Next week's task will be writing rigorous tests for this module and benchmarking it with known results. 
Thank you for visiting...

Title: Neural Turing Machines : Week 2 Highlights
Date: 2017-06-18 14:00:00
Tags: gsoc
Author: Sumedh Ghaisas

The second week of gsoc went harder than I thought. Encountered lot of 
roadblocks in testing Grated Recurrent Unit in RNN.  While testing, we came up with 
couple of improvements to the framework. These improvement will help me in turn with 
implementation of Neural Turing Machines. First improvement is the support of 
variable length sequences in RNN framework. The current GRU, and also LSTM for 
that matter, store the outputs in a vector which may incur high cost in variable 
length sequences due to memory rellocation. Another improvement is saving 
an extra call to Forward while optimizing FNN and RNN. This can be achieved 
by using the Forward call in Gradient to return the error in Evaluate call.
Both of these features will be implemented in Week 2 and Week 3. 

GRU is currently tested with Reber Grammar. Some Forward and Backward call tests 
will also be written. For Batchnorm implementation the priliminary implementation 
is complete for FNN. The support for CNN is yet to be added. 

Hopefully I will be able to get on track with the implementation in the coming
week.

@brief Neural Turing Machines - Week 3 + 4
@author Sumedh Ghaisas
@page Sumedh2017WeekFour Neural Turing Machines - Week 3 + 4
@date 2017-06-06 14:00:00

@section Sumedh2017WeekFour Neural Turing Machines - Week 3 + 4

Past two weeks were spent on designing and implementing the variable length 
support for RNN. The new framework now can break 
Backpropagation Through Time(BPTT) by setting appropriate 'rho' value in 
LSTM or GRU gates. This 'rho' value can be different than the 'rho' value of RNN which
signifies the overall sequence length. This variable length support has been 
tested with ReberGrammar and EmbeddedReberGrammar, and to my surprise the error 
value achieved in these tests is zero.

Batch normalization for convolutional layer has been completed, although I am 
running little behind on the schedule there with BatchNorm tests for convolutional 
networks being unfinished. it seems I have to put in 3 extra days of efforts to 
get back on track there.

Excited to start the work on NTM next week. I also spent some time last week 
on computing the derivatives of all the functions used in NTM. This will help
me a lot in implementing the memory unit. See you all next week...
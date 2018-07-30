@brief Automatically-Generated Go Bindings - Week 11
@author Yasmine Dumouchel
@page Yasmine2018Week11 Automatically-Generated Go Bindings - Week 11
@date 2018-07-30 11:11:00

@section Yasmine2018Week11 Automatically-Generated Go Bindings - Week 11

This week has been very exciting, as I managed to generate some C and some Go code for the first time. I first made a CMake file with three sections. The first generates a generate_cpp_method executable who then prints a method.cpp (where method is any mlpack method). The second generates a generate_h_method who then prints a method.h, and lastly, a generate_go_method who then prints a method.go. I have then started to implement the programs that would print the those three files. To do so I have created a GoOption, and some utility files. I then stopped implementing the programs to print out the bindings and got back to doing the handmade perceptron go binding, to handle the passing of model from go to C++ and vice versa. 

My goal for next Sunday is to have the the programs that prints the method.cpp, method.h, and  method.go files done. It might seem like a lot, but I think that now that everything is printing correctly, implementing those programs by the end of the week is a reasonable task!

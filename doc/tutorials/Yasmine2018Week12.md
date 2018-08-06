@brief Automatically-Generated Go Bindings - Week 12
@author Yasmine Dumouchel
@page Yasmine2018Week12 Automatically-Generated Go Bindings - Week 12
@date 2018-08-06 11:01:00

@section Yasmine2018Week12 Automatically-Generated Go Bindings - Week 12

During the past week, I have mostly been implementing the function that would print the bindings for every methods (the .cpp, .h, and the .go binding file). Tuesday, Ryan made me realize that the perceptron model passing was not working fully, in fact, I was able to pass a model from Go to C++, but passing back the 'output_model' parameter as the 'input_modelÍ  parameter was not working correctly. Thus, I made sure the latter issue was fixed. As for the generator, I have finish the program which prints the binding files, with the exception of printing the documentation. I am still not done with the generator, so I will continue working on it this week. I will finish implementing the printing of the documentation and will start testing them. I will also need to make sure it compiles with Go and that CGO links properly with the bindings and thus, will probably require some adjusting of the bindings or the CMake files. 

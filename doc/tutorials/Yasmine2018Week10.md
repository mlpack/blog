@brief Automatically-Generated Go Bindings - Week 10
@author Yasmine Dumouchel
@page Yasmine2018Week10 Automatically-Generated Go Bindings - Week 10
@date 2018-07-23 18:10:00

@section Yasmine2018Week10 Automatically-Generated Go Bindings - Week 10

Last week, I first dealt with serialization and passing back models. I then started generating the C header files for the individual methods. To do so two files will be generated, a .h header file that acts as a C API to link cgo and c++ and a .cpp file to glue the mlpack code and the header file. I am not able to do so as of yet as I am having trouble with compiling. As time is flying and we are already at week 10, I will make sure that these are done by tomorrow morning. I will then start generating the Go bindings. To do so, I will write a program which will generate based on the PARAM_*() used. 


@brief Automatically-Generated Go Bindings - Week 07
@author Yasmine Dumouchel
@page Yasmine2018Week07 Automatically-Generated Go Bindings - Week 07
@date 2018-07-01 12:08:00

@section Yasmine2018Week07 Automatically-Generated Go Bindings - Week 07

Last week I have focused on passing matrices.  I was able to copy them using first class array in Go. With the help of Ryan, we are now also able to pass a matrix using the advanced armadillo constructor and a const_cast hack.  I am having a lot of difficulty passing a Gonum matrix as CGO does not allow the passing of go object that have underlying go pointers in their structure, which has resulted in a "cgo argument has Go pointer to Go pointer" panic when running the program. However, Ryan has pointed out to me that a gonum matrix holds a []float64 data member. I have also started to look at how to pass the memory pointer back to Go. Thus, I will  try to pass the matrix as a []float64 structure this week and will look at passing back matrices from C++ to Go without having to copy memory.

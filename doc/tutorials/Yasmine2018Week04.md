@brief Automatically-Generated Go Bindings - Week 04
@author Yasmine Dumouchel
@page Yasmine2018Week04 Automatically-Generated Go Bindings - Week 04
@date 2018-06-11 10:46:00

@section Yasmine2018Week04 Automatically-Generated Go Bindings - Week 04

This past week, I continued to implement the bindings by hand. The overall process to bind C++ with Go is to create a C API which can than share memory, pass pointers, call functions and so on with Go. For instance, for the pca method, the pca_main.cpp file will have a pca_capi.cpp and pca_capi.h which will be the C interface and its implementation, and a pca.go file which will include the pca_capi.h with cgo. The process of binding is pretty straight forward and easy to implement with cgo. However, the last week, I have struggled a bit more with the C API. More specifically, I am having trouble binding the templates functions since templates are not defined in C. To wrap C++ functions, using extern "C" is used to declare the C linkage, however templates have the restriction that the name can't have C linkage. For the following week, my plan is therefore to find how to wrap template functions, afterwhich I will work on passing the matrices.

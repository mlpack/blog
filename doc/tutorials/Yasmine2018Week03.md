@brief Automatically-Generated Go Bindings - Week 02
@author Yasmine Dumouchel
@page Yasmine2018Week02 Automatically-Generated Go Bindings - Week 02
@date 2018-06-04 1:41:00

@section Yasmine2018Week02 Automatically-Generated Go Bindings - Week 02

This week, I started trying to build bindings for the pca method as it is a simple method to practice on. I am handwriting the binding and not generating it. To do so, I wrote a C API in order to use cgo, which binds C and Go. I am also using the Go build mode "buildmode=c-shared" which create a shared object (.so) library file and allows the C++ and Go code to be called back and forth. At this point I am able to bind simple data structure, but am still trying to pass a matrix without having to copy the whole matrix. I am testing how to pass a pointer instead and wrap a armadillo object around it.

For this week, my plan is to continue building a fully functionning pca binding for go and the matrix utility code that will be need as well.

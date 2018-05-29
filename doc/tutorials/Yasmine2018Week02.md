@brief Automatically-Generated Go Bindings - Week 02
@author Yasmine Dumouchel
@page Yasmine2018Week02 Automatically-Generated Go Bindings - Week 02
@date 2018-05-29 10:15:00

@section Yasmine2018Week02 Automatically-Generated Go Bindings - Week 02

This week I have finalized my concept for the bindings and started building a prototype. Ihave encountered a few problems which has led me to do a bit more reasearch and change my concept. For instance, although CGO can be used to bind C++, in order to be able to pass more than simple data such as integers or chars, I will need to generate a C API from the C++ headers. This API will also allow us not to use SWIG. Thus, when generating a binding for  program, first a .h file will be generated afterwhich a .go file will be generated. The .go file will be make use of CGO. 

This week, my goal is to finishing testing out the concept and building a prototype and I will try to also code some matrix utilities to wrap a armadillo object around a gonum matrix. 

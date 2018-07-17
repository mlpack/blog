@brief Automatically-Generated Go Bindings - Week 09
@author Yasmine Dumouchel
@page Yasmine2018Week09 Automatically-Generated Go Bindings - Week 09
@date 2018-07-17 10:25:00

@section Yasmine2018Week09 Automatically-Generated Go Bindings - Week 09

This week I finished passing back and forth the matrix, which entails I have working handwritten bindings for the PCA method. I have also dealt  with small issue such how will we pass default value, how to return multiple values, as well as how will we print out documentation. For the first issue, since Go doesn't have method overloading or default value in function prototypes, I made a struct with the optional parameters which when initialized, aree initialized to their default values. For the second, go has built-in support for multilple value, therefore we will simply have multiple value returned in the funciton prototype and won't need to pass a dictionnary or data structure to hold the multiple output variables. For the last issue, we will use godoc, which is a tool that prints out the comment above un function prototype.This week, I will focus on finishing passing a model ptr to go, afterwhich I will start generating the C code!

@brief Automatically-Generated Go Bindings - Week 06
@author Yasmine Dumouchel
@page Yasmine2018Week06 Automatically-Generated Go Bindings - Week 06
@date 2018-06-25 23:20:00

@section Yasmine2018Week06 Automatically-Generated Go Bindings - Week 06

I started the week with understanding how to properly link the files when they are outside the go workspace. After, I focused on the matrices. I have encountered an issue with cgo when passing matrices because the underlying structure of a gonum matrices or vector has a pointer. Go code may pass a Go pointer to C provided the Go memory to which it points does not contain any Go pointers. Thus, trying to pass a gonum matrices, by passing the pointer to the matrice, has resulted in an error. I will continue to work on passing these matrices this week. I will also look at serialization.

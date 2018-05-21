@brief Automatically-Generated Go Bindings - Week 01
@author Yasmine Dumouchel
@page Yasmine2018Week01 Automatically-Generated Go Bindings - Week 01
@date 2018-05-20 21:41:00

@section Yasmine2018CBP Automatically-Generated Go Bindings - Week 01

At the beginning of the week, I had in mind to implement a strategy for the Go bindings that was very similar to the strategy that is implemented to generate the Python bindings. I started the week by playing and testing interoperations between C++ and Go code and passing memory and pointers by using cgo as well as playing with Cmake which I was a bit less familiar with. I then started trying to implement a prototype. However, I quickly realized that the Python binding strategy, although being a reference point and being very useful in understanding how the CLI singleton works and how it can or can't be used, might not be the most efficient way for the Go language. I realized using the Python strategy as a "step-by-step guide" might end-up being counter-productive and should instead be used as general guidance. I decided to take a few steps back and make sure that the underlying strategy will work for/is optimized for the Go language before building a prototype. 

I looked at open source project where Go bindings were created for a C++ libraries and project were those bindings were automatically generated. I have then learned more about/played with specific Go commands and program that could be used for the project, such as the "go generate" command to generate Go code,  the "go build" and "go imports" functionalities which are useful for multistep compilation, the cgo program and most importantly its limitations and alternative to using SWIG, the possibility of using Go's Prototype Buffers for serialization of the models, etc. I will be fine-tuning my concept for the bindings Monday (and Tuesday if needed) and plan on building the prototype starting Tuesday or Wednesday.

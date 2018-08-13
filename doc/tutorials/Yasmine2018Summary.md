@brief Automatically-Generated Go Bindings - Summary
@author Yasmine Dumouchel
@page Yasmine2018Summary Automatically-Generated Go Bindings - Summary
@date 2018-08-13 16:20:00

@section Yasmine2018Summary Automatically-Generated Go Bindings - Summary

This following is the summary of my GSoC project.
My weekly progress blog posts can be found in the following link: http://mlpack.org/gsocblog/YasmineDumouchelPage.html

# The Go Binding Generator

For the past 3 months, I have been implementing an Go binding generator. Like discussed in my weekly progress post, the generator produces three files for every binding:
1. A .go file: This file is the go interface for Go users. It uses cgo in order to sharing data and communicate with C. When generated, the .go file is build in the mlpack/binding/go/mlpack/ directory.
2. A .h file: This file is used as a C interface. This file includes the function which can be called by Go.
3. A .cpp file: This file acts as 'glue code' between the C interface (the .h file) and mlpack methods' code.

Additionally, a method specific library is created the method_main.cpp in order for Go to call the mlpack_main() function.

Several utility files for the cli object and armadillo object have also been implemented. The .cpp, .hpp and .h utility files can be found in the mlpack/binding/go/mlpack/capi directory, and the .go utility files in the mlpack/binding/go/mlpack/ directory.

# Pull Request

My pull re	quest can be found here: https://github.com/mlpack/mlpack/pull/1492

This PR hasn't been merged as of yet, as I am not yet finish implementing the binding generator. More precisely, two specific parameter type have yet to be finished and implemented. Precisely the matrix with dataset info parameter type, which would allow to one to generate bindings for the hoeffding and decision tree method  and the vector of strings and int parameter type. After these are implemented, additional test for these parameter would be needed. Furthermore, documenting the generator with example and tutorials for the user would also useful. I plan on doing those task and continuing the Go bindings generator until they are fully done. 

# How To Use The Binding Generator

GENERATING THE BINDING

First, to generate the bindings get mlpack in your go workspace:

	$  go get https://github.com/yaswagner/mlpack/

Then in your terminal go to the mlpack folder create your build directory and build cmake as desired.
For example:

	$ cd ${GOPATH}/src/mlpack.
	$ mkdir build
	$ cd build
	$ cmake -D BUILD_GO_BINDINGS=ON -D BUILD_PYTHON_BINDINGS=OFF ../
	$ make 

You can generate a specific binding to generate by using the mlpack_go_{method} target.
For instance, for the pca method:

	$ make mlpack_go_pca

USING THE BINDINGS

To use the bindings in Go, you must import the mlpack package and gonum package.

For example:

	import (
		"mlpack/build/src/mlpack/bindings/go/mlpack"
		"gonum.org/v1/gonum/mat"
	)

Optional parameters need to be set in the methods config struct and then we can set our desired parameters.
For instance, when using the pca method, we initialize the config struct called param and set verbosity to true by doing:

	param := mlpack.InitializePca()
	param.Verbose = true

We can then pass our optional parameters and call the Pca method as such:

	output := mlpack.Pca(input, param)

For output parameters we do not wish to use, we can use an underscore. 
For example, for the perceptron, if we wish to only use the 'output_model' and not 'output'"

	_, output_model := mlpack.Perceptron(param)

In order to get documentation about a method, we use 'godoc'.
For example, for the pca method we would type on the command line:

	$ godoc mlpack/build/src/mlpack/bindings/go/mlpack Pca

TESTING THE BINDINGS

Finally, to test the binding, Go's 'testing' is used. Simply go to the go test file following directory as such:

	$ cd ${GOPATH}/src/mlpack/src/bindings/go/tests/gofile

Then test by using the 'go test' command tool, as such:

	$ go test -v

# Acknowledgements

I want to thank mlpack for having given me the opportunity to work on this project. This was my first open source experience and I am feel beyond lucky to have learned as much valuable tools and knowledge as I did. I also want to thank my mentor, Ryan Curtin, for his help and guidance throughout the summer. I could not have asked more of a mentor. He has made this experience a fun one as well as a great learning opportunity. I look forward to continue implementing the bindings and perhaps even implementing a generator for another language sometime in the future!


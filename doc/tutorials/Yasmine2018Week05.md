@brief Automatically-Generated Go Bindings - Week 05
@author Yasmine Dumouchel
@page Yasmine2018Week05 Automatically-Generated Go Bindings - Week 05
@date 2018-06-18 10:36:00

@section Yasmine2018Week05 Automatically-Generated Go Bindings - Week 05

The past week, I have been focusing on building CLI utility code in order to pass information/register parameters to the CLI singleton. After fighting with the compiler, I have been able to register parameters. I ended the week with passingmatrices, which is where I will continue today. I haven't had problem passing pointers to C++, therefore I don't think it will be a problem.

Another point I will focus on this week is how to integrate mlpack in the go workspace. As of now, I have had go interfacing with mlpack when mlpack is directly downloaded in the go workspace. This weekend, I have tried to have it working with mlpack installed locally on my computer, and I have had difficulty with the linker finding libmlpack.so (or libmlpack.dylib). It seems to be a frequent issue in the Go communitee. I will therefore also try to understand how to have go use the shared library.

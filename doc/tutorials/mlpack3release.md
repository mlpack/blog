@brief mlpack 3.0.0 released!
@author Ryan Curtin
@page mlpack-3-released mlpack 3.0.0 released!
@date 2018-03-30 15:12:00

@section mlpack-3-released mlpack 3.0.0 released!

It is my pleasure to announce the release of mlpack 3.  This is the culmination
of more than a decade worth of development and more than 100 contributors from
around the world---including <a href="https://www.github.com/C0deAi">one AI
contributor</a>.  This release includes, among other things, Python bindings, a
generic optimization infrastructure, support for deep learning, and improved
implementations of machine learning algorithms.

## Community-Led Growth

I'm proud to say that over the years we have grown the project into a
community-led effort for fast machine learning implementations in C++.

In 2007, mlpack was just a small project at a single lab in
Georgia Tech focusing only on nearest neighbor search and related techniques.
Now, in 2018, it's developed and used all around the world (and even <a
href="http://ieeexplore.ieee.org/abstract/document/8001607/">in
space!</a>), it's a regular part of <a
href="http://www.mlpack.org/gsocblog/mlpack-in-google-summer-of-code-2014.html">Google</a>
<a
href="http://www.mlpack.org/gsocblog/mlpack-in-google-summer-of-code-2016.html">Summer
of</a> <a
href="http://www.mlpack.org/gsocblog/mlpack-in-google-summer-of-code-2017.html">Code</a>,
and it implements all manner of general and specialized machine learning
techniques.

The list of contributors is too long to list here, but everyone played a part in
making this release happen.  <a href="http://www.mlpack.org/about.html">The
About page</a> on the mlpack website has a list of all the contributors, and you
could also look at <a
href="https://github.com/mlpack/mlpack/graphs/contributors">Github's contributor
list</a>.  <b>Thank you</b> to each and every contributor!

## Interfaces to Python and Other Languages

For the mlpack 3 release, we have created a system to provide bindings to Python
that have the same interface as our command-line bindings.  In addition, we are
planning to generate bindings for other languages, such as MATLAB, Java, Scala,
and C#, as well as others.

Here are some links to quickstart guides for those bindings:

<p align="center"><a
href="http://www.mlpack.org/docs/mlpack-3.0.0/doxygen/python_quickstart.html">python</a>
| <a
  href="http://www.mlpack.org/docs/mlpack-3.0.0/doxygen/cli_quickstart.html">command-line</a></p>

And you can download the new source package here:

  http://www.mlpack.org/files/mlpack-3.0.0.tar.gz

## New And Improved Functionality

Since the last release (mlpack 2.2.5), lots has been added and changed.  Much of
this is due to projects from Google Summer of Code.  A shortlist of new and
improved functionality:

 - Optimization infrastructure (<a
   href="http://www.mlpack.org/docs/mlpack-3.0.0/doxygen/optimizertutorial.html">more
here</a> and <a href="https://arxiv.org/abs/1711.06581">here</a>

 - Deep learning infrastructure with support for FNNs, CNNs, and RNNs, as well
   as lots of existing layer types and support for custom layers.

 - New optimizers added: <tt>AdaGrad</tt>, <tt>CMAES</tt>, <tt>CNE</tt>,
   <tt>FrankWolfe</tt>, <tt>GradientDescent</tt>, <tt>GridSearch</tt>,
   <tt>IQN</tt>, <tt>Katyusha</tt>, <tt>LineSearch</tt>, <tt>ParallelSGD</tt>,
   <tt>SARAH</tt>, <tt>SCD</tt>, <tt>SGDR</tt>, <tt>SMORMS3</tt>,
   <tt>SPALeRA</tt>, <tt>SVRG</tt>.

 - Fast random forest implementation added to the set of classifiers that mlpack
   implements.

 - Added a <a
   href="http://mlpack.org/docs/mlpack-git/doxygen/hpt.html">hyperparameter
tuning</a> and <a
href="http://mlpack.org/docs/mlpack-git/doxygen/cv.html">cross-validation
infrastructure</a>.

## Modular By Design
Since mlpack is designed in a modular way, you can drop in custom functionality
for a specific task.  For instance, if you want to use a custom metric for
nearest neighbor search or if you want to use a custom criterion for splitting
your decision trees, you simply need to write the code and it plugs in with no
runtime overhead.

In addition, because mlpack is built on <a
href="http://arma.sourceforge.net">Armadillo</a>, you can plug in any BLAS you
like---<a href="http://www.openblas.net">OpenBLAS</a> is a good, fast, choice
with builtin parallelization.  You could even use <a
href="http://docs.nvidia.com/cuda/nvblas/index.html">NVBLAS</a>, which will
outsource heavy-duty matrix computations to the GPU, if you have GPUs available.

## Read, Download, Explore

So, head on over to http://www.mlpack.org/ and check out the new release!  And
if you're interested in following the development or contributing, check out <a
href="https://github.com/mlpack/mlpack">the Github project</a>.

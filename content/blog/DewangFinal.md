Title: Benchmarking mlpack libraries
Date: 2017-08-26 14:00:00
Tags: gsoc, benchmarks
Author: Dewang Sultania

This summer I was quite fortunate to work on the mlpack project with my mentors Ryan Curtin and Marcus Edel as a part of the Google Summer of Code program. I worked on improving their benchmarking system and I would like to now describe what the work was and what I learnt using  plethora of success and failures and what work has to be done in future post GSoC.

### Introduction

There were many mlpack methods that had been added since the previous benchmarking system was built and in many of the current implementations only the runtime metric was being captured. Also many of the implementations were according to the old versions of the benchmarked libraries which used many deprecated methods which needed updating. Many methods were not implemented in MATLAB, Weka and many libraries like annoy, mrpt, nearpy, milk, dlib-ml and R were not yet benchmarked.

### Work done before GSoC

Before officially becoming a Google Summer of Code intern I made the following contributions to the benchmarking system of mlpack library starting March 2017:

 * Added options to the randomforest and Decision tree scikit benchmark code.
 * Added the Code for DecisionTree in mlpy.
 * Implemented Approximate Nearest Neighbors using the Annoy, Mrpt, Sklearn and Nearpy.
 * Added test file for Random Forest, Logistic Regression and Adaboost.
 * Made certain corrections to the svm and LARS implementation of sklearn and to the config file.

### Work done during GSoC

#### Updating Scikit Implementations:

The scikit implementations were updated to facilitate specifying more options and storing metrics like Accuracy, Precision, Recall, MSE along with runtime. The config.yaml file did not have any block for the Logistic Regression and ICA methods, so these were also added. The following table enumerates the parameters added to the various methods:

Method | Parameters Added
--- | ---
LSHForest | Min_hash_match, n_candidates, radius and radius_cutoff_ratio
ALLKNN | Radius, tree_type, metric and n_jobs
Elastic Net | Max_iter, tolerance and selection
GMM | Tolerance and Max_iter
ICA | N_components, algorithm, fun, max_iter and tolerance.
KMEANS | algorithm
Logistic Regression | Tolerance and Max Iterations

*Merged PR's*
.. * https://github.com/mlpack/benchmarks/pull/60
.. * https://github.com/mlpack/benchmarks/pull/61

#### Benchmarking Against Milk Machine Learning Toolkit for Python

Introduced a new library called Milk to benchmark against. Implemented Adaboost, Decision Tree, Kmeans, Logistic Regression and Random Forest in the same. Wrote the Unit test files for them and added the config.yaml block for the same.

*Merged PR's*
.. *  https://github.com/mlpack/benchmarks/pull/64

#### Unit Test file for Adaboost

There was no unit test file for Adaboost present so added the same for the scikit and milk implementations.

*Merged PR's* 
.. * https://github.com/mlpack/benchmarks/pull/65

#### Updating the Shogun implementations.

Shogun had been updated from 5.0.0 to 6.0.0 so most of the implementations needed updation. Also earlier only the runtime metric was being collected in the implementations, so the codes were changed to collect other metrics like Accuracy, Precision, Recall and MSE.

*Merged PR's* 
.. * https://github.com/mlpack/benchmarks/pull/79

#### Avoid building the model twice.

In the scikit and shogun implementations, the model was being built twice, once while calculating the runtime and again while calculating the other metrics. This was avoided by returning the predictions made during runtime to the function calculating other metrics and all the scikit and shogun implementations were updated to do the same. This ensured that the implementations took lesser time to run.

*Merged PR's*
.. * https://github.com/mlpack/benchmarks/pull/80
.. * https://github.com/mlpack/benchmarks/pull/81
.. * https://github.com/mlpack/benchmarks/pull/82
.. * https://github.com/mlpack/benchmarks/pull/83
.. * https://github.com/mlpack/benchmarks/pull/84
.. * https://github.com/mlpack/benchmarks/pull/85
.. * https://github.com/mlpack/benchmarks/pull/86
.. * https://github.com/mlpack/benchmarks/pull/88
.. * https://github.com/mlpack/benchmarks/pull/91

#### Updating MATLAB implementations.

There were around 3-4 MATLAB implementations present and earlier and these were mapping only runtime. Many implementations like Decision Tree, K-Nearest Classifier, Support Vector Classifier, Decision Tree Classifier, Lasso, LDA, QDA, Random Forest and Support Vector Regression were added along with python scripts to call them and unit test files to test them. 

*Merged PR's*
.. * https://github.com/mlpack/benchmarks/pull/89
.. * https://github.com/mlpack/benchmarks/pull/94

#### Updating WEKA implementations.

The current WEKA folder hosted around 3 implementations and after weka got updated those scripts had become outdated . So the presently benchmarked methods had to be re-implemented and many other methods were also added. After updating the weka folder holds Decision Stump, Decision Tree, Logistic Regression, Naive Bayes, Perceptron, Random Forest, ALLKNN, KMEANS, Linear Regression and PCA implementations. The python scripts to call and store the results and the Unit test files were also implemented.

*Merged PR’s* 
.. * https://github.com/mlpack/benchmarks/pull/95

#### Benchmarking against Dlib-ml

Introduced a new C++ Machine Learning library called dlib-ml to the benchmarking system. Added implementations like SVM, KMEANS, Approximate Nearest Neighbors and ALLKNN. Wrote the install script, the python scripts to call them and the unit test files for the same.

*Merged PR's*
.. * https://github.com/mlpack/benchmarks/pull/96
.. * https://github.com/mlpack/benchmarks/pull/97
.. * https://github.com/mlpack/benchmarks/pull/98
.. * https://github.com/mlpack/benchmarks/pull/99

#### Make specifying K Necessary

Some of the K-Nearest Neighbors implementations took the default value of k as 5 while others did not. So to ensure uniformity made the option of specifying k mandatory in the implementations.

*Merged PR's*
.. * https://github.com/mlpack/benchmarks/pull/101

#### Benchmarking Against R

This is something that I was personally inclined to do. There is a worldwide debate on Python vs R and I thought that this is the best platform to settle it to some extent and see which one performs faster. Using mlr - The machine learning framework for R implemented methods like NBC, Adaboost, QDA, LDA, Decision Tree, K-Nearest Classifier, Random Forest, Support Vector Classifier, Lasso, Linear Regression and Support Vector Regression. Also wrote the Python Scripts and Unit Test file for the same. 

*Merged PR’s*
.. * https://github.com/mlpack/benchmarks/pull/102
.. * https://github.com/mlpack/benchmarks/pull/103
.. * https://github.com/mlpack/benchmarks/pull/104
.. * https://github.com/mlpack/benchmarks/pull/105

#### The webpage

This is a work in progress where we are thinking about using JavaScript Visualization libraries to present the results on the webpage in a better way. More on this once the work completes. This work might not get completed during GSoC period itself but I will continue working on this after GSoC.


So basically throughout the summer, I…
.. * Committed around 5000 lines of code.
.. * Had  27 of my Pull Requests merged.

### Technical Skills Developed

 * R:I had little to no experience when it came to working on R. During the course of the project I learnt how to build R from scratch and implement all the major Machine Learning Algorithms in it.

 * MATLAB:  I had never used MATLAB before and now I am well versed in calling MATLAB codes from python scripts, Using Statistical and Machine Learning toolbox and then saving the results and sending them back to the python script that called the code.

 * Weka: I had only used the Weka GUI tool before and had never used it in a JAVA code. My mentors taught me how to do that.

 * Dlib-ml: I had never implemented Machine Learning Algorithms in C++ earlier. This project gave me an opportunity to do that.

### Lessons Learnt

While I learnt useful tools and languages I also gained some general advice.

.. * Don’t be under the assumption that anything is easy: While writing my proposal I assumed that working on new libraries and improving the old ones would be a week's task each but when I started working on them I had to spend far more time that planned originally which resulted in the last part of the project (the webpage) getting delayed.

.. * It is important to be flexible and willing to change your priorities as many obstacles might come up.

.. * Always ask for help as “Help will always be given at mlpack to those who need it.” ( Could not resist quoting Albus Dumbledore :-p).

### Plans after GSoC

I wish to continue contributing to the benchmarking system and the initial plans are adding MachineLearning.jl and Shark libraries to the benchmarks. Thereafter writing a manuscript along with my Mentors Ryan Curtin and Marcus Edel on the results. Looking forward to a long time association with them.

In closing I would like to thank Ryan and Marcus for being such amazing mentors, for teaching me so many things and for putting up with me whenever I used to struggle. This is the best internship experience I’ve ever had and I hope I can meet them in person soon.








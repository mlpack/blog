@brief Benchmarking mlpack libraries - Week 4 + 5 + 6 + 7
@author Dewang Sultania
@page Dewang2017WeekFourSeven Benchmarking mlpack libraries - Week 4 + 5 + 6 + 7
@date 2017-07-28 15:00:00

@section Dewang2017WeekFourSeven Benchmarking mlpack libraries - Week 4 + 5 + 6 + 7

The various implementations done in the benchmark system used to build the model twice :- Once while calculating runtime and then also while calculating various metrics. Those implementations were updated to build the model only once by using the predictions obtained in the first run to calculate the metrics later.The test file timeouts were also upgraded from 9000 to 240 to run the tests faster and avoid longer runtime when some error had occured.

Shogun has been updated from 5.0.0 to 6.0.0 so the implementations were updated according to the latest version of shogun library. Also the shogun implementations were only calculating the runtime metric. Those implementations were updated to calculate other metrics like Accuracy, Precision, Recall, Precision and MSE.

For MATLAB many methods like Support Vector Classifier, Decision Tree, K Nearest Neighbors, Linear Discriminant Analysis, Quadratic Discriminant Analysis, Support Vector Regression, Random forest and Lasso were added including the test file for the same. The other implementations were updated to calculate more metrics like Accuracy, Precision, Recall and MSE.

Weka needed many upgrades and some algorithms added which were not previously benchmarked.Implementations for Decision Tree, Logistic Regression, Random Forest, Perceptron were added including test files for the same. The old implementations were upgraded to calculate more metrics.

The next steps are adding dlib-ml and R to the benchmark systems. The work on that has started and they will get added to the benchmarking systems soon.
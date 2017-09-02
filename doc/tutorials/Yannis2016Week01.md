@brief Implementation of Multiprobe LSH - Week 1
@author Yannis Mentekidis
@page Yannis2016WeekOne Implementation of Multiprobe LSH - Week 1
@date 2016-05-29 20:20:20

@section Yannis2016WeekOne Implementation of Multiprobe LSH - Week 1

This summer my goal is to improve various features of the current Locality Sensitive Hashing implementation of mlpack, making it faster, smarter, and easier to use. LSH is an approximate nearest neighbors algorithm that uses hashing to greatly reduce the amount of points needed to be examined

I was looking forward to GSoC week 1 for a while - I began with the implementation of [Multiprobe LSH](http://dl.acm.org/citation.cfm?id=1325958), an algorithm that improves on the classic LSH by identifying more hash buckets in each table where a query's neighboring points might be. The algorithm better utilizes the tables created by LSH, meaning fewer ones need to be created, which makes the search take less time and memory. 

The implementation required the modification of the LSH code and corresponding mlpack test cases.

The new parameter, number of additional probing bins, is now accessible to users both as a command line argument (-T) and via a new parameter in LSHSearch.Search().


Another mini-feature I implemented, LSHSearch.ComputeRecall() takes two armadillo matrices and computes the recall (% of neighbors found correctly by LSH). This is also accessible from the command line program by using the -t switch to specify a "truth file" - a file of real neighbors.

Using these two features, a user should be able to reduce the number of tables used by LSH and get as good (or better!) recall by increasing the number of additional probing bins.

I am making documentation, testing and style changes and will be opening a pull request in the next few days.
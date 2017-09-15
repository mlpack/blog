@brief Dataset and Experimentation Tools - Week 7
@author Keon Kim
@page Keon2016SWeekSeven Dataset and Experimentation Tools - Week 7
@date 2016-07-11 16:00:00

@section Keon2016SWeekSeven Dataset and Experimentation Tools - Week 7

This week, I:

DatasetMapper & Imputer

1) Applied the changes suggested, add more comments, and debugged DatasetMapper & Imputer pull request.

2) Made an overload for every imputation methods that receives only one input matrix as a paramter.
The result will be overwritten to the input matrix, hopefully providing faster performance.

3) MedianImputation now excludes user-defined missing values and NaNs while it calculates the median.

4) New solution to implement ListwiseDeletion (suggested by rcurtin) is used.

Descriptive Statistics

Last week, I said I am going to work on statistics module.
As a result I made a proof-of-concept work on this [commit](https://github.com/keonkim/mlpack/commit/5aed5ba9c78e4584f445217e9c66e52f79d6daec)

I made a class called Statistics and put all the functions inside it.
I think the Statistics class maybe useful for other things, too.
so I am considering to separate the class from the executable and put it somewhere else independently.

Sample run on iris.csv shows the results like the below.
```
[INFO ] Loading 'iris.csv' as CSV data.  Size is 150 x 4.
[INFO ] dim     var     mean    std     median  min     max     range   skewness  kurtosis  SE        
[INFO ] 0       0.6811225.84333 0.8253015.8     4.3     7.9     3.6     0.175246  1.12569   0.0673856 
[INFO ] 1       0.1867513.054   0.4321473       2       4.4     2.4     0.0266889 0.113048  0.0352846 
[INFO ] 2       3.09242 3.75867 1.75853 4.35    1       6.9     5.9     -1.4776   15.3453   0.143583  
[INFO ] 3       0.5785321.19867 0.7606131.3     0.1     2.5     2.4     -0.04573920.557191  0.0621038 
```

The output of this executable is similar to [this application](http://personality-project.org/r/basics.t.html).
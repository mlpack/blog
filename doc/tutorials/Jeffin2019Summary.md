@brief String Processing Utilities - Summary
@author Jeffin Sam
@page Jeffin2019Summary String Processing Utilities - Summary
@date 2019-08-23 19:44:28

@section Jeffin2019Summary String Processing Utilities - Summary

This post summarize my work for GSoC 2019

# Overview

The proposal for String Processing Utilities involved implementing basic functions which would be helpful in processing and encoding text and then latter implementing machine learning algorithms on it.

# Implementation

### String Cleaning [PR1904](https://github.com/mlpack/mlpack/pull/1904)

* The implementation started with implementing String Cleaning Functions, A class-based approach was used to implement the function, following were the function which was implemented :
  1. `RemovePunctuation()`: The function allows you to pass a string known as punctuation, which could involve all the punctuations to be removed.
  2. `RemoveChar()`: This function allows you to pass a function pointer or function object or a lambda function which return a bool value and if the return value is true, the character would be removed.
  3. `LowerCase()` : Convert the text to lower case.
  4. `UpperCase()` : Convert the text to upper case.
  5. `RemoveStopWords()`: This function accepts a set of stopword and removed all those words from the corpus.

* After implementing the class, I started implementing CLI and python binding, since mlpack used armadillo to load matrix and hence I had to write a function which could read data from a file using basic input output stream. The types of file are limited to .txt or .csv. The binding has different parameters to set and would work as required based on parameters passed.

### String Encoding [PR1960](https://github.com/mlpack/mlpack/pull/1960)

* The initial plan was to implement a different class for different encoding methods such as BOW encoding, Dictionary encoding or Tf-Idf encoding, but we found that the class had lot of codes which we redundant, and hence we decided to implement a policy-based method and the implement different policy for each of the encoding type.

* We implemented `StringEncoding` class which has the function for encoding the corpus (accepts a vector as input) and outputs you the encoded data based on the policy and output type, vector or arma::mat, Also provided an option with padding and to avoid padding depending on the encoding policy

* We also designed a helper class `StringEncodingDictionary`, which maintains a dictionary mapping of the token to its labels, The class is a templated class based on the type of tokens, which involves string_view or int type. We arrived at the conclusion of implementing this helper class based on the speed profiling done by lozhnikov. He concluded some [results](https://github.com/mlpack/mlpack/pull/1814#issuecomment-514687037), and thus we decided to implement a helper class. 

### Policies for String Encoding [PR1969](https://github.com/mlpack/mlpack/pull/1969)

* We decided to implement three policy for encoding, namely as follows :
  1. `Dictionary Encoding`: This encoding policy allows you to encode the corpus by assigning a positive integer number to each unique token and treats the dataset as categorical, it supports both padding and non-padding output.
  2. `Bag of Words Encoding`: The encoder creates a vector of all the unique token and then assigns 1 if the token is present in the document, 0 if not present.
  3. `Tf-Idf Encoding`: The encoder assigns a tf-idf number to each unique token.

### Tokenizer [PR1960](https://github.com/mlpack/mlpack/pull/1960)

* To help with all the string processing and encoding algorithms, we often needed to tokenize the string and thus we implemented two tokenizers in mlpack. The two tokenizers are as follows:
  1. `CharExtract`: This tokenizer is used to split a string into characters.
  2. `SplitByAnyOf`: The SplitByAnyOf class tokenizes a string using a set of delimiters.

After implementing all the encoding policies and tokenizer, I decided to implement CLI and python binding [PR1980](https://github.com/mlpack/mlpack/pull/1980) for String Encoding, Both string encoding and string cleaning function share a lot of common function and hence we decided to share a common file `string_processing_util.hpp` between the two bindings.

My proposal also included Implementation of Word2Vec, but we decided to opt-out since we found that google patented it.

# Post GSoC

A lot of the codes I implemented are sketchy since I have used boost::string_view and other boost algorithms and hence we need to do a speed check and find out the bottlenecks if any. Also, my plan is to implement any substitute for word2vec, such as GLOVE or any other word embedding algorithms. I had implemented a function for One hot Encoding, which I thought could be useful for word2vec, but we found out that it was buggy to a small extent and hence I have to find a way out and also have to implement some overloaded functionality.

Lastly, the most important part, I have to write tutorials for all the functionality provided to allow someone to understand how to drop these functions in their codebase, Also excited to do some machine learning stuff on text dataset using mlpack.

# Acknowledgement

A big thanks to lozhnikov, Rcurtin, Zoq, and the whole `mlpack` community. This was my first attempt at GSoC, and I am happy that I was successful in it. I fell in love with the open-source world and it was a wonderful experience. I gathered a lot of knowledge in these past 3 months. I will continue to be in touch with the `mlpack` community and seek to do more contributions to the project in the future. 

Also, I think its time to order some mlpack stickers :)

Thanks :)
@brief String Processing Utilities - Week 01
@author Jeffin Sam
@page Jeffin2019Week01 String Processing Utilities - Week 01
@date 2019-06-09 19:11:28

@section Jeffin2019Week01 String Processing Utilities - Week 01

Apologies for being late again, but I was probably waiting for a weekend to write the blog.

So, It has been one successful week with GsoC at mlpack, during the first week I tried implementing function useful for string processing such as - function to remove stopwords, punctuation and to convert string to lowercase or uppercase. Initially, I though of implementing them as standalone function but after a small discussion we agreed on to have a class-based implementation. I have opened a work in progress [PR1904](https://github.com/mlpack/mlpack/pull/1904) still a lot of refactoring is needed for the implementation. Also, a concrete plan should be found to implement the bindings for these function. I am lagging behind the schedule a little bit, but I guess I will cover up.

Now coming to my updates about previous [PR1814](https://github.com/mlpack/mlpack/pull/1814), Since to make the functionality efficient both in terms of space and time complexities, to avoid many copies we introduced Boost::string_view, but with that also came many minute issues which had to be resolved. And hence I had to overload copy constructor and assignment operator. Also, serialization was introduced to the PR1814 and also for the [PR1876](https://github.com/mlpack/mlpack/pull/1876).

I will try to be more punctual in updating you all next time. Thank you :)

\note
Since the world is full of memes, [here](https://twitter.com/mcclure111/status/1002648636516282368?s=19) is a particular one which I would like to share with you all.

<p>
<img src = "images/cpp.jpg" width = "150" height = "100"/>
</p>

@brief String Processing Utilities - Week 04-06
@author Jeffin Sam
@page Jeffin2019Week04-06 String Processing Utilities - Week 04-06
@date 2019-07-09 22:21:28

@section Jeffin2019Week04-06 String Processing Utilities - Week 04 - 06

Sorry for not updating for so long, So possibly this post will have updates from week4 to week6.So let's start :)

So I almost finished with the Dictionary Encoding PR, but then we realized that most of the function be it in Dictionary Encoding, or Bag of Words or TF-IDF, has almost same interface and thus We decided to have something of Policy-based design, With Encoding being base class and then substituting being done with Dictionary Policy or BOW Policy or be any other. 

I wasn't so comfortable with policy-based design and hence I took some time out, Went through some links, codes and also a book (Modern C++ Design: Generic Programming and Design Patterns Applied), And came up with the interface, but again there were some issues, since Encoding such as Dictionary Encoding provides option for output without Padding, but other Policies doesn't have such things and hence we had to find a way out. And then Lozhnikov suggested me to us SFINAE. 

Now again, To be frank, I never knew what SFINAE is, and hence had to go through many codes, and links and then came up with the interface. Again, The policy needed some type of traits so that Policies can be differentiated and hence we had to introduce a trait which has some default values, and then add specific specialization for each policy if needed.

I never knew the depth of C++, and to study all these concepts, it took a lot of time for me. Also, I don't understand why there not many resources for C++, Googling doesn't help much in clearing concepts since there is a relatively lesser amount of tutorial available to a web stack or something else.

I know I am currently a lot behind the actual plan, but if we are able to complete the interface, then I think it won't take much time to complete other Policies, Also after completing everything I am planning to write a blog on how to drop the Encoding interface to your code and how to use it. So that people can get used to the interface. I will probably complete with the interface in the coming week, Also will try to be on time with the blogs for next time.

Thank you :)


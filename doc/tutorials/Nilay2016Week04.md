@brief We need to go deeper, Googlenet - Week 4
@author Nilay Jain
@page Nilay2016WeekFour We need to go deeper, Googlenet - Week 4
@date 2016-06-20 20:00:00

@section Nilay2016WeekFour We need to go deeper, Googlenet - Week 4

So this week I spent time on more editing and cleaning, doing some easy optimizations and removing some of the redundant calculations that were there in the code. Also after discussion it was concluded the design of the class needs to be changed, to be similar to other parts of the library code, so we did that.

I added a discretize function to convert the structured labels of pixels, to discreet class labels which can then be an input to the decision trees, for training. Currently this function takes more time than it should so it needs to be seen how we can optimize this better.

I also changed some other parts of the code, making changes to all the functions, passing objects as reference as opposed to returning them, and refactoring according to the style guidelines. I added comments to some of the funcitons in the code, more complete discription will be prepared this week.

For reading this week, I first reviewed CNNs from the deeplearningbook, to get familiar with the terminology, and then I reviewed some of the papers relevant to the project, I read again the paper on GoogleNet, and a paper discussing the architecture of GoogleNet.

Finally for the coming week my task is to implement the inception layer using the layers that are present in ann methods of the library.  I still have to look at the ann code and then I can proceed with the implementation.
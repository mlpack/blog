@brief We need to go deeper, Googlenet - Week 1
@author Nilay Jain
@page Nilay2016WeekOne We need to go deeper, Googlenet - Week 1
@date 2016-05-30 12:09:00

@section Nilay2016WeekOne We need to go deeper, Googlenet - Week 1

The goal of my project is to develop googlenet such that it integrates in mlpack's existing ANN API and the methods developed in this project can be used in any other related applications. After a discussion with my mentors we chose edge boxes method for object localization, as it is a very fast method and gives competing performance with state of the art.

After reading through the research papers and experimenting with the mlpack code in the community bonding period, I discussed the interface with my mentors. My first task was to find to perform feature extraction given images, segmentations and boundaries for the BSDS500 Dataset. It took me some time getting acquainted with the armadillo library as the code I had to write used its functionality rigrously. So the status for my first task is as follows:

The utility functions have all been implemented. I had to look for library implementations and implement them using armadillo to calculate Convolutions, Distance Transforms, and some of the functionalities which armadillo does not provide, to name a few.

For feature extraction part, only method for writing the self similarity features remain with all of the basic underlieing methods to be used already implemented. I expected to complete feature extraction part well within this week, but I am sure all the unimplemented features will be finished by Monday. I guess it took time to read up on Vision and Image Processing concepts that were new to me, and for new functions I had to think about the apt way of implementing and looking up at the armadillo library, for each line that I write, at the same time.

Things I learnt from this week were new some Image Processing concepts, and gaining indepth knowledge of numpy and armadillo libraries. I also developed a habit of reading documentations, where previously I used to just google things and find links on stackoverflow. I also learnt how to search code in open source libraries, I had to look things up in numpy and opencv. Though I accept learning these things is a very basic skill, it took me out of my comfort zone and will definitely make me better. I also brushed up Template Programming and watched introductory slides on template metaprogramming in c++, as I come from a Java background, doing this part was easier for me.

My plans for the week ahead are as follows: To test the code and discussing with my mentors about the methods written and any improvements using a forked repo. After completing the proposed changes open a pull request. Then starting with the Structured Random Forest Implementation to complete the process of edge detection. Hopefully this will take a lesser time as most of the functionalities are implemented in mlpack and can be reused.
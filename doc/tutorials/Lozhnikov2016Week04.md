@brief Implementation of tree types - Week 4
@author Mikhail Lozhnikov
@page Lozhnikov2016WeekFour Implementation of tree types - Week 4
@date 2016-06-20 14:00:00

@section Lozhnikov2016WeekFour Implementation of tree types - Week 4

Last week I had been working on the R+ tree implementation. I came across some curious issues. Namely, the R+ tree appears to be buggy.

The R+ tree requires that the nodes do not overlap each other. This leads to some problems in the insertion algorithm and in the split method. Firstly, the paper does not explain the insertion algorithm in detail. The paper states that we should insert a rectangle in each node that overlaps the rectangle. But the paper does not discuss the case when there are no such nodes. I thought that I can always enlarge a node in order to insert a point but when I tried to implement that a simple test showed that there are some cases when it is impossible. Later I thought out such case in 2D. Another problem of the R+ tree is the split algorithm. Sometimes the split should be propogated downward (because of the disjointness property). Hence the split algorithm does not guarantee that nodes will not be overflowed after the split.

I looked trough many papers and found a curious modification of the R+ tree: R++ tree. The R++ tree suggests to store the maximum bounding rect of a node. And the maximum bounding rects of two nodes do not overlap. This property helps to avoid the R+ tree problems. But sometimes this leads to empty leaf nodes.

So, I implemented the R+ tree and the R++ tree. I solved the problem with the insertion algorithm by addition of a node. But I am not sure that my implementation of the R+ tree has not problems with the split algorithm. The R+ tree definitely has problems on rectangle data (suppose all data rectangles overlap each other). But I do not know an example in case of point data. Right now the R++ tree uses the sweep method of the R+ tree. I'd like to implement some different sweep techniques.
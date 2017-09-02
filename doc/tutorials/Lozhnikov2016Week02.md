@brief Implementation of tree types - Week 2
@author Mikhail Lozhnikov
@page Lozhnikov2016WeekTwo Implementation of tree types - Week 2
@date 2016-06-06 01:00:00

@section Lozhnikov2016WeekTwo Implementation of tree types - Week 2

As I had planned in the previous blog post I spent last week testing, cleaning and refactoring the code. I added a lot of comments and some tests for the Hilbert R tree. Also I corrected a huge number of errors.

Since I decided to use an armadillo object instead of the std::list object in order to store the Hilbert values of points I had to rewrite the DiscreteHilbertValue entirely with a template parameter TreeElemType. The TreeElemType parameter was introduced in order to define the best datatype (uint64_t for double and uint32_t for float) for the Hilbert value.

In addition I removed the dataset variable from the RectangleTree class. After that RectangleTree has to use the local dataset instead of the global dataset. In order to complete the removal I have to correct all tree traversers, base cases and pruning rules. I'll do that soon.
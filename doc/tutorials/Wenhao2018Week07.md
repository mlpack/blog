@brief Alternatives to Neighborhood-Based CF - Week 7
@author Wenhao Huang
@page Wenhao2018Week07 Alternatives to Neighborhood-Based CF - Week 7
@date 2018-07-02 22:00:00

@section Wenhao2018Week07 Alternatives to Neighborhood-Based CF - Week 7

For the past week, I was working on refactoring decomposition policies. Now I have finished refactoring all current decomposition policies, and made necessary modifications in CFType class, cf main program, interpolation policies, and cf tests. The major changes are: 1) model parameters (e.g. `W`, `H`) are moved into decomposition class, 2) decomposition class provides method `GetRating()` to compute prediction and `GetNeighborhood()` to compute neighborhood and similarities, 3) `class CFModel` (similar to `AdaBoostModel`) is added and is used for cf main program. After refactoring decomposition policies, it would be easier to implement `BiasSVDPolicy` and `SVDPlusPlusPolicy` (and perhaps other policies later). I will focus on implementing these two policies next week.
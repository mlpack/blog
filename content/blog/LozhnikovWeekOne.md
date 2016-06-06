Title: Implementation of tree types. Week 1 (Implementation of Hilbert R tree)
Date: 2016-05-30 01:45:00
Tags: gsoc, Hilbert R tree, Hilbert value
Author: Mikhail Lozhnikov

The main goal of my project is to extend the mlpack's list of tree types by implementing R+ trees, Hilbert R trees, vantage point trees, random projection trees and UB trees for the purpose of using them in mlpack's dual-tree algorithms. I decided to begin with the Hilbert R tree.

The Hilbert R tree differs from original Guttman's R tree by a special ordering. All points should be inserted into the tree according to their Hilbert values. In order to do this I implemented a new layer of abstraction for the RectangleTree class. Now each node of the tree contains an auxiliary information which depends on the tree type (AuxiliaryInformationType class). This class can handle the insertion and the deletion process in order to be certain that all points and nodes are arranged according to their Hilbert values. Also this class can contain some extra information like the largest Hilbert value.

The comparison process along the Hilbert curve can be implemented differently. Generally, there are two approaches: a recursive approach and a discrete approach. The recursive approach in contrast to the discrete approach does not compute exact Hilbert values. I implemented two classes: DiscreteHilbertValue and RecursiveHilbertValue. All these classes can be used as template parameters for the HilbertRTreeAuxiliaryInformation class.

Also I implemented the split rules and the descent heuristic rules.

I think I'll spend the next week testing these changes and cleaning the code. Also I should add a bit of documentation.

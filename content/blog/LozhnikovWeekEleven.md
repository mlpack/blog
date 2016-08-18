Title: Implementation of tree types : Week 11
Date: 2016-08-10 11:00:00
Tags: gsoc, space trees, UB-tree, Vantage point tree, random projection tree
Author: Mikhail Lozhnikov

Last week I have been working on fixing various tree types.

### Random projection trees
I made some minor fixes of random projection trees and wrote a simple test that checks if there is a hyperplane that splits a node. I find the hyperplane as a solution of a linear system of inequalities. Curiously, but it seems the easiest iterative method solves the system fine.

### Universal B-tree
I fixed a problem in the address-to-point conversion method. The method had led to wrong results if some addresses correspond to negative numbers. Moreover, since floating point data types have some excess information, some addresses correspond to infinite points. Thus, I have to add some restrictions in the conversion algorithm.

### Vantage point tree
I implemented a method that tries to get a tighter bound by investigating the parent bound. The method calculates the distance to the "corner" (the intersection of two (n-1)-dimensional spheres that is an (n-2)-dimensional sphere) using properties of orthogonal transforms. The results appear to be worse since this calculation requires too many arithmetic operations and the number of base cases has decreased slightly.

### Hollow hyperrectangle vantage point tree
I implemented a bound that consists of an outer rectangle and a number of rectangular hollows. I tried to test the vantage point tree with this bound. Right now, the original VP-tree bound outperforms this one, but I think the hollow-hrect bound should work faster. So, I'll continue working on the optimization of the bound.

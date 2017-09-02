@brief Implementation of tree types - Week 10
@author Mikhail Lozhnikov
@page Lozhnikov2016WeekTen Implementation of tree types - Week 10
@date 2016-08-03 17:15:00

@section Lozhnikov2016WeekTen Implementation of tree types - Week 10

Last week I have been working on the universal B tree. I finished the implementation of the bound and wrote a series of tests.

In order to explain what the bound is I have to introduce the notions $\textbf{area}$ and $\textbf{address}$.

An $\textbf{address}\ \alpha$ for an $\textbf{area}$ in an $n$-dimensional cube is a sequence $i_1.i_2.\ldots.i_l$, where $i_j\in \{1,2,\ldots,2^n\}$.

I'll define the notion $\textbf{area}$ recursively. Let $\alpha$ be an $\textbf{address}$ for an $\textbf{area}$ in an $n$-dimensional cube `C` ($\textbf{area}(C)$). Partition `C` into $2^n$ subcubes $sc(i),\ i=1,2,\ldots,2^n$ by dividing `C` in the middle of each dimension. If $\alpha=k$ then $\textbf{area}(C)[k]=\bigcup_{i=1}^{k}sc(i),\ k=0,1,\ldots,2^n-1$. If $\alpha=k.\beta$ then $\textbf{area}(C)[\alpha]=\textbf{area}(C)[k]\cup \textbf{area}(sc(k+1))[\beta]$, where $\textbf{area}(sc(k+1))[\beta]$ is an area in $sc(k+1)$.

Each child node of the universal B tree is bounded by two addresses i.e. the bound of a node is the difference of two areas. Since I deal with floating point numbers I use fixed-sized addresses in the whole space. The calculation of the distance between two nodes requires a lot of arithmetic operations. So, I decided to restrict the number of steps in the bound. Thus, children may overlap each other.

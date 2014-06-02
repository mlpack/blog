Title: Is this thing on?
Date: 2014-06-01 13:58:00
Tags: gsoc
Author: Andrew Wells

Hello.  I'm, as the author tag hopefully indicates, Andrew Wells--user of
sentences convoluted and loquacious.  Well, actually no.  They're usually
quite short.  Like this.  Or was that a complete sentence?

Anyways, now that I've found out how to use this thing, I can tell you about my
project.  I basically have two goals:

1)  Implement various types of trees useful in neighbor searches.
2)  Improve the tree traversal speed of the current code.

Right now, I'm working on part 1.  There are several trees in development:
R-Trees, R*-Trees, Hilbert R-Trees, and X-Trees.  All of these are quite similar
and with the way the code is setup, it should be fairly simple to add the
functionality of any one of them once I get the first one implemented.

Here, since I can tell you are just dying to hear more, is
the general structure of the code:

*rectangle_tree:  This is a generic type of tree that will be reused for all of the above named type.
*tree_split:  This code controls how the tree is split.  This is where most of 
the differences in the different trees comes in.
*tree_traversal:  This code controls the traversal of the trees.  Existing
algorithms are quite simple and quite good, but are there better ways to 
traverse trees?
*descent_hueristic:  The tree's are not (necessarily) binary, so we have a 
hueristic to try to choose the best node for inserting a point when this is
non-obvious (ie. the point is not inside the hyperrectangle)

As per usual, it seems that the hardest part of programming is learning
the new libraries and the existing code (ignoring algorithm
design or, alternatively, claiming that it isn't PROGRAMMING, per se).
This brings us to the interesting source of flame wars and all things good,
text editors. It seems that people design editors for, well, editting text of
all things.  Saddly, I think this is a mistaken effort.  In reality, I want an
editor designed for reading text.  I would hazard a guess that I spend maybe 25%
of my time writting code.  Most of the time is spent reading and thinking.  
Taking notes on other peoples' code, and wondering why they did that and why
this C++ feature wasn't covered in class.  I've been tinkering with the ACME
editor, and it has some cool features, like right clicking on an included file
to open it, but it seems like what I really want is the ability to search google
for these things, or to see all of the places where this file is called in X, Y,
and Z.  Now granted, ACME could presumably be extended to do this, but
time.  There's just no time.  Which is why I must stick with emacs.  Once again
deadlines triumph over their mortal enemy--progress.
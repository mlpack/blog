Title: mlpack in Google Summer of Code 2016
Date: 2016-05-17 14:25:06
Tags: gsoc
Author: Ryan Curtin

This year is shaping up to be a productive and exciting year for mlpack; after
being accepted into Google Summer of Code 2016, we received an astounding 119
applications and were able to accept 6 talented students.  Here is what they
will be working on this summer:

## Neuroevolution Algorithms Implementation
### by Bang Liu, mentored by Marcus Edel

Bang will implement neuroevolution algorithms for the neural network framework
in mlpack, such as CNE, NEAT, and HyperNEAT.  These will be tested on various
problems, including applying HyperNEAT to NES games.  In addition, benchmarking
will be done to verify that mlpack's implementations are competitive with---or
faster than---other implementations of these neuroevolution algorithms.

Bang is a Ph.D. student at the University of Alberta; he likes swimming, playing
table tennis, and badminton.  His website can be found at
http://www.ualberta.ca/~bang3/.

## Dataset and Experimentation Tools
### by Keon Kim, mentored by Tham Ngap Wei

Keon will design and develop utilities for dataset management in
mlpack.  Specifically, Keon will create four separate modules for
working with datasets: (1) dataset I/O (convert dataset formats, etc.);
(2) data transformation (join/split data, clean missing data, etc.); (3)
statistical analytics (mean/mode/median, t-test, etc.); (4) mathematical
operators (rounding, timezone handling, etc.).  These will supplement
the existing mlpack machine learning algorithms and can be used for
preprocessing (or postprocessing).

Keon is an undergraduate student at New York University an currently works as an
intern for a startup in the financial sector that uses machine learning.

## Approximate Nearest Neighbor Search
### by Marcos Pividori, mentored by Sumedh Ghaisas

Marcos will extend the existing knn/kfn implementation to support
approximation, and then implement spill trees and the "defeatist"
strategy for approximate nearest neighbor search.  Then, he will
benchmark the mlpack aknn implementation against other aknn strategies
using the mlpack benchmarking system.

Marcos is a computer science student from Argentina and is no newcomer to Google
Summer of Code; this is the third year he has participated.  In 2013 he worked
with the Haskell project, and in 2015 he worked with the OpenCog project to
provide Haskell bindings.  He also likes to play table tennis and also regular
tennis.

## Implement tree types
### by Mikhail Lozhnikov, mentored by Ryan Curtin

Mikhail will extend previous years' tree types projects by
implementing several types of trees: R+ trees, Hilbert R Trees, vantage
point trees, random projection trees, and UB trees.  Each of these will
be usable by mlpack's various dual-tree algorithms (like nearest
neighbor search, range search, FastMKS, emst, and others).

Mikhail is a graduate student at Moscow State University, interested in
computational mathematics and programming.  When he has free time, he plays
classical guitar and piano.

## We need to go deeper - GoogLeNeT
### by Nilay Jain, mentored by Tham Ngap Wei and Marcus Edel

Nilay will implement the components of the GoogLeNet architecture (the
inception layer, global average pooling, and other pieces), and then
build a GoogLeNet on a sample of ImageNet data.  The pieces of this
architecture will be usable for other neural network applications.

Nilay is a third year undergraduate CS student from BITS Pilani; he is far from
the only BITS Pilani student who has worked with mlpack in the past, as he is
the fourth student we have accepted from there.  Nilay enjoys football, watching
movies, and reading.

## Implementation of Multiprobe LSH and LSH Tuning
### by Yannis Mentekidis, mentored by Ryan Curtin

Yannis will significantly improve the existing LSH framework we have
in place by implementing multiprobe LSH and also LSH tuning, which is
what the LSHKIT package implements, as well as OpenMP support since many
parts of LSH are embarrassingly parallel.  If time permits, he will
implement more LSH strategies.

Yannis is a student from Thessaloniki who is currently finishing his Bachelor's
thesis, also focused on LSH.  He claims he talks too much and too loudly, and
also doesn't remember what his hobbies are anymore since he has been in school
too long.  Hopefully this summer will leave a little free time so he can
rediscover some fun activities.

You can find more information on each of the projects on the Summer of
Code website:

http://summerofcode.withgoogle.com/organizations/5376684740050944/

Anyway, congratulations to Bang, Keon, Marcos, Mikhail, Nilay, and
Yannis!  The coding period will start next Monday (May 23rd).

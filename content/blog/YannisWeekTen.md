Title: Modeling LSH - Implementation Week 2
Date: 2016-08-01 20:20:20
Tags: gsoc, lsh, modeling
Author: Yannis Mentekidis

Week ten of GSoC was quite productive for me - I finally understood the proposed model in full detail. I am outlining here the design I decided to go with, the outline of which will be pushed to GitHub soon.

## Step 1 - Dataset Analysis

Here, we undersample the dataset and produce useful metrics based on the sample. The most important metrics here are the pairwise distances and the distances from points to their k-nearest neighbor, for k in [1, K], K specified by the user.

It is important to undersample here - otherwise we are running an all-vs-all distance calculation that the user wanted to avoid and might not even be feasible if the set is too big.

To compute the distances from points to their k-nearest neighbor, we use the first few points of the sample as query points and the rest of the sample as a reference set.

## Step 2 - Fitting Distributions

This is the part where we use the data produced by Step 1 to fit distributions that will help us predict the recall and selectivity of LSH when run with a specific parameter set.

The authors propose fitting the Gamma distribution to both the pairwise distances and the kNN distances. In my opinion the user should be able to decide which distribution should be used, so at this part we will probably use a template for the distribution.

As an example, here's the distributions of distances for a sample of [Corel Color Histogram][1]. It definitely looks like a Gamma distribution.

![Corel Color Histogram Distance Distribution](http://i.imgur.com/boj6HHd.png)

On the contrary, the distance distributions for a sample of the [Sift10k][2] dataset looks like either a mixture of Gammas or a mixture of Gaussians, but definitely not like it can be fit by a single distribution.

![Sift10k Distance Distribution](http://i.imgur.com/Vw7luNn.png)

## Step 3 - Parameter Estimation

Once we have a good estimation for the distribution parameters, we can finally put all of this together and find some good parameters to run LSH with.

The user will specify an acceptable recall (in the range [0, 1)) and we will try to maximize selectivity while achieving at least that recall. To do that, we will run our model with different parameters and see what the predicted recall and selectivity are.

We know (from theory and from profiling the LSH implementation) that a larger number of tables decreases selectivity but increases recall, and also that the process of constructing the candidate set is faster when fewer tables are involved. So, while maximizing selectivity, we should try minimize the number of tables as well.

At this stage, there's a lot of options about what to do: We could simply print out a list of parameter sets that work well for this dataset. We could select the first such set or the set that satisfies some additional constraint - for example, maximum recall or minimum number of tables.

For now there's no point in dwelling on this - I'll start considering the options once everything else is prepared.

[1]: [http://archive.ics.uci.edu/ml/datasets/Corel+Image+Features]
[2]: [http://corpus-texmex.irisa.fr/]
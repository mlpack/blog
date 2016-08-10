Title: Dataset and Experimentation Tools : Week - 10 and 11 Highlights
Date: 2016-08-08 16:00:00
Tags: gsoc, dataset, data
Author: Keon Kim

I've been building a preprocess_validate cli-executable,
a simple app that prints out warnings for possible invalid values in a dataset.
The output of this program would be the one like below, which is an ultimately
what we've been trying to achieve from the
[beginning](https://github.com/mlpack/mlpack/wiki/SummerOfCodeIdeas#dataset-and-experimentation-tools).

```
[WARN ] Possibly problematic value at point 1, categorical feature 0 :
5 (numeric value in categorical feature)
[WARN ] Invalid value at point 4, numerical feature 1 : 
[WARN ] Invalid value at point 1, numerical feature 2 : a
[WARN ] Invalid value at point 4, numerical feature 2 : b
```

It took me a longer time to build it because I tried several approaches for
making it.

1) First approach I made a class named Validator that acts similar to
   Imputer class.
2) I found that it is hard to track where the missing values are if there is
   more than two missing values, since every invalid values will be turned
   to "nan". So I tried hacking DatasetMapper class so that it could store
   where the invalid values are.
3) Next decision was to make a new validate_policy which prints out warnings
   as it goes through the tokens of each dimensions.
   (though it still has some issues to fix)
4) Lastly to fundamentally fix the problem, I suggest the approach
   [#758](https://github.com/mlpack/mlpack/issues/758).

Current `maps` object for DatasetMapper can be described as maps of
`map<dimension, pair<bimap<string, MappedType>, numMappings>>`
(NumMappings usually being numeric primitive types.)

I think process of having multiple map policies can be simplified by having
to two mapping objects. For validation & imputation purposes we could have
another mapper (I will call it invalidMaps for now). Which would look like:

```
// MapType =  map<dimension, pair<bimap<string, MappedType>, numMappings>>;
// InvalidMapType = maps<string, std::pair<dimension, point>>;
MapType maps;
InvalidMapType invalidMaps;
size_t numInvalidMappings;
```

invalidMaps and maps serve two different purposes.
maps is used as usual (mapping categorical feature to numeric feature).
invalidMaps is used as temporary holder for future imputation. Both x and y
coordinates have to be stored in order to track the invalid values, since
every invalid values are turned to NaNs.


I made [commits in this branch](https://github.com/keonkim/mlpack/commits/check)
to test its usability.
The code I am referring to is "validate_policy" written in
[this commit.](https://github.com/keonkim/mlpack/commit/2814bb578f1c7953042c585f6a50d58edebe08f2).
I made it to only test, so the code has still a lot to be improved.

When I run the code with the following dataset using validate policy:

```
a, 2, 3
NULL, 6, a
b, 9, 1
a, 2, 3
c, , b
```

The result matrix produced by the above data by data::Load() becomes:

```
[INFO ] 3 mappings in dimension 0.
[INFO ] 0 mappings in dimension 1.
[INFO ] 0 mappings in dimension 2.

[DEBUG]             0          nan   1.0000e+00            0   2.0000e+00
[DEBUG]    2.0000e+00   6.0000e+00   9.0000e+00   2.0000e+00          nan
[DEBUG]    3.0000e+00          nan   1.0000e+00   3.0000e+00          nan
```

3 mappings in dimension 0 would indicate that
it successfully mapped (a->0, b->1, c->2).
NULL was not mapped because I set it as one of the user-defined missingValues.

All `nan`s are mapped using invalidMaps object. And can later be used for
printing errors or imputations.

I think this is intuitively a good approach.
And this can replace the use of all other mapping policies.
I think this way we can make mlpack more user-friendly by reducing
introductions to new concepts.


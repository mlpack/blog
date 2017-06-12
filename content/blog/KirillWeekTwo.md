Title: Cross-Validation and Hyper-Parameter Tuning: Week 2
Date: 2017-06-12 11:00:00
Tags: gsoc
Author: Kirill Mishchenko

During the second week I was working on tools that allow to check whether a
given class has a method with particular name and form
([#1020](https://github.com/mlpack/mlpack/pull/1020)). A usage example can be
found above the
[implementation](https://github.com/micyril/mlpack/blob/has_method_form/src/mlpack/core/util/sfinae_utility.hpp#L164)
of the macro 'HAS_METHOD_FORM`.

The method form detection tool will allow for a given machine learning
algorithm to automatically extract information such as predictions type,
whether it takes `DatasetInfo` parameter along with data and whether it supports
weighted learning. We need to do it to prevent users from passing such
information to prospective cross-validation/hyper-parameter tuning modules.

The next step is to facilitate the implemented macro `HAS_METHOD_FORM` for
things mentioned above. I have already started to work on it and plan to send a
PR this week.

@brief Implementing an mlpack-Tensorflow Translator
@author Sreenik Seal
@page Sreenik2019Week06 Implementing an mlpack-Tensorflow Translator - Week 6
@date 2019-07-10 22:56:10

@section Sreenik2019Week06 Implementing an mlpack-Tensorflow Translator - Week 6

### Where were we before?
We had an onnx to mlpack translator that only supported linear models. Support for convolutional models was not completely implemented. Later, while working on it this week I found that it was way more complicated than I had at first glance apprehended.
Other than this there were some onnx layers which did not match in flexibility with mlpack's and that needed some fixing.
### Where are we now?
- Support for convolutional layers is now available, although onnx itself is not too consistent with its conversions. That leads to a lot of exceptions which have not yet been covered. Moreover, onnx splits certain layers into 4-5 basic operational layers. The ones identified have been taken care of but this translator will improve over time as more and more exceptions are discovered. 
- The batchnorm layer has been modified to support momentum and work on the selu layer is almost done.
- As mentioned in the last blog I had lost almost a week (the 5th week) due to high fever and that had slowed down the progress.
### What's left for the upcoming weeks?
- I am currently restructuring a part of the converter which will make the design much more robust and easily modifiable in the future. That needs to be finished.
- Some layers need to be modified. Part of it has been done but a part that involves adding *group* support to convolutional layers is still left.
- Starting and completing the mlpack to onnx parser.

If you have reached this far, here's something to give a thought about (not to mention, it has been taken from Reddit):

If you ever think English is a straightforward language just remember that *read* and *lead* rhyme and *read* and *lead* rhyme, but *read* and *lead* don't rhyme and neither do *read* and *lead*. This is not the end as we often forget that we drive on a parkway and park on a driveway. Have a nice day, cheers :)

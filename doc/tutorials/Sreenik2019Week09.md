@brief Implementing an mlpack-Tensorflow Translator
@author Sreenik Seal
@page Sreenik2019Week09 Implementing an mlpack-Tensorflow Translator - Week 9
@date 2019-07-29 09:19:10

@section Sreenik2019Week09 Implementing an mlpack-Tensorflow Translator - Week 9

The last couple of weeks were quite exciting as I finally implemented the Softmax layer. Those few lines of code needed a few days of understanding of mlpack's ANN codebase. I am extremely grateful to Atharva for providing me all his support in understanding it. We also worked through the mathematical derivations of the softmax and logsoftmax functions and it was quite satisfying when I pushed the softmax PR (although I have messed up as other commits have also been included in the PR).

I also worked on the unit test for the onnx-mlpack converter. It seems like there is no API for directly building a model in ONNX, so the best C++ solution that I could think of was using Torch. The best thing about Torch is that Torch itself maintains a torch-onnx converter. On the downside, the Torch dependency is around 180MB. Now, it can be so done that instead of creating the Torch model everytime during the test, we maintain a Torch model exported to ONNX format and use that. However, I would like to stick to the former idea if we are already adding Torch as a dependency which we might have to for the mlpack-onnx converter (but we'll have to consult Marcus before we can proceed), the reason simply being that if Torch updates the structure of its modules the test would fail.

If you have reached this far, here's something (from Reddit) in relation to the European weather this Summer:
People are complaining about this being the hottest Summer in the last 150 years. I'm more of a glass half full kind of guy.
I'm thinking of it as the coldest Summer in the next 150 years.

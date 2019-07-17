@brief Implementing an mlpack-Tensorflow Translator
@author Sreenik Seal
@page Sreenik2019Week07 Implementing an mlpack-Tensorflow Translator - Week 7
@date 2019-07-18 01:06:10

@section Sreenik2019Week07 Implementing an mlpack-Tensorflow Translator - Week 7

### Where were we before?
We had an onnx to mlpack translator that supported linear and convolutional models. The code was not structured that well, i.e., modifying the converter required adding special cases for the particular layers to be modified.

### Where are we now?
- The code has been structured in a way that a lot of cases have been generalized and classifying a new layer as one of those is as simple as adding it to a list.
- The above point was little work though, I spent most of my time behind understanding the mlpack implementation of logsoftmx and writing a similar one for softmax. Not sure if I understand it 100% but Atharva has said he will look into it so that I can focus on writing unit tests.
- I also gave some thought about the **mlpack to Onnx** parser. From my interaction with the Onnx community it seems like there is no API of Onnx in C++ that can be used to create models from scratch (there is one in Python though). They suggested to use the protobuf API as the models are of that format (a clumsy way indeed). Another way out is to convert the mlpack model to a torch model (and then to an Onnx model using the Onnx converter if required).

### What's left for the upcoming weeks?
- Improving layer compatibility between Onnx and mlpack.
- Writing test cases.
- Completing the mlpack to Onnx parser.

If you have reached this far,
...well this was really short (and there is literally nothing trending on Reddit except Area 51 memes). Have a nice day, cheers :)

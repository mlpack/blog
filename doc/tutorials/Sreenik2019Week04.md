@brief Implementing an mlpack-Tensorflow Translator
@author Sreenik Seal
@page Sreenik2019Week04 Implementing an mlpack-Tensorflow Translator - Week 4
@date 2019-06-26 17:17:10

@section Sreenik2019Week04 Implementing an mlpack-Tensorflow Translator - Week 4

### Where were we before?
We had a converter that could convert the network architecture of an onnx model to an mlpack model, given they are supported. The weights would not be transferred. Also, speaking of the json parser which we are using as an API here, it was not in a mergeable state as per mlpack's standards.
### Where are we now?
- In week 3, I focussed on extracting the weights from the onnx model when it is stored as raw bytes. That took some time and eventually `https://github.com/lcskrishna/onnx-parser` came of great help.
- There was a lot to put together after that. I was eventually able to convert linear models and also get their weights transferred.
- Support for the transfer of pre-trained weights for convolutional layers were also added but there was some dimension mismatch which I will have to fix.
- I wrapped up the json parser next. Also added a few more layers for support. There is still an issue over the use of namespaces and there was a discussion between Atharva and Marcus on how to fix it.
- Sadly, on Saturday I went out to play cricket with my friends and fell sick with a very high fever. A centurion on and off the field they say. I am still recovering and have not been able to resume work since :(
### What's left for the upcoming weeks?
- The onnx to mlpack converter has to be completed. Not sure if anything is left other than finishing off the convolution support that I have mentioned above.
- Fixing whatever namespace error is there with the json parser.
- Starting and completing the mlpack to onnx parser.

If you have reached this far, here's something for you from Reddit:

My bro asked why I was speaking so softly in the house. I said I was afraid the NSA was listening. There was complete silence for a moment. Then he laughed, I laughed, Alexa laughed.

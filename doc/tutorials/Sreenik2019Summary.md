@brief Implementing an mlpack-Tensorflow Translator
@author Sreenik Seal
@page Sreenik2019Summary Implementing an mlpack-Tensorflow Translator - Summary
@date 2019-08-26 01:06:10

@section Sreenik2019Summary Implementing an mlpack-Tensorflow Translator - Summary

# The Idea
The general objective of this project is to allow the interconversion of trained neural network models among mlpack and all other popular frameworks. For this purpose, two converters have been created:
- ONNX-mlpack-converter
- mlpack-Torch-converter

ONNX being a central junction supporting a number of popular frameworks including but not limited to Tensorflow, Torch, Keras and Caffe, the Tensorflow-Torch-ONNX-mlpack conversion is made possible through this project.

The reason why we chose Torch over ONNX for the **mlpack-Torch-converter** is because the C++ implementation of the ONNX library doesn't *directly* support model creation. It can still be done though, as nothing is impossilbe to achieve and ONNX models are nothing but protobuf files. There was no robust reason of choosing Torch over Tensorflow except for the fact that Torch's C++ API seemed to be more robust. That being said it actually boils down to one's personal choice and it rightly did boil down to my preference of exploiting the opportunity of learning a new framework instead of working with Tensorflow, with which I was largely familiar.

# The Code
The code directly associated with the converters are in the repository https://github.com/sreenikSS/mlpack-Tensorflow-Translator under the [/src](https://github.com/sreenikSS/mlpack-Tensorflow-Translator/tree/master/src) folder, while the tests are under the [/src/Tests](https://github.com/sreenikSS/mlpack-Tensorflow-Translator/tree/master/src/Tests) folder and converted models under the [/Examples](https://github.com/sreenikSS/mlpack-Tensorflow-Translator/tree/master/Examples) folder. The tests need and will receive an updateThis project mainly has three source files:
- **model_parser.hpp** which is a header file supporting the creation of an mlpack model from a user-defined json file
- **model_parser_impl.hpp** which contains the implementation of the definitions present in *model_parser.hpp*
- **onnx_to_mlpack.hpp** which contains the necessary functions to convert ONNX models to mlpack format
- **mlpack_to_torch.hpp** which contains the necessary function to convert mlpack models to Torch format

This project however, has additional dependencies like LibTorch and ONNX and is/will be clearly mentioned in the readme file. This is supposed to exist as a separate repository under [mlpack](https://github.com/mlpack).

### JSON parser
This parser can be used in a number of ways, like obtaining a ```LayerTypes<>``` object corresponding to a string containing the layer type and a map containing the attributes as follows:
```
std::map<string, double> layerParams;
layerParams["insize"] = 4;
layerParams["outsize"] = 10;
LayerTypes<> linearLayer = getNetworkReference("linear", layerParams);
```
It can also be used to convert a json file to an mlpack model by calling the ```convertModel()``` function and if needed overriding the ```trainModel()``` function. An example of the using the converter which will train the model and display the train and validation accuracies is:
```
std::string fileName = "network.json";
arma::mat dataMat;
data::Load("train.csv", dataMat, true);
Log::Info << "Data loaded" << "\n\n";
dataMat = dataMat.submat(0, 1, dataMat.n_rows - 1, dataMat.n_cols - 1);
arma::mat train, valid;
data::Split(dataMat, train, valid, 0.1);
arma::mat trainX = normalise(train.submat(1, 0, train.n_rows-1,
                             train.n_cols-1));
arma::mat trainY = train.row(0) + 1;
arma::mat validX = normalise(valid.submat(1, 0, valid.n_rows-1,
                             valid.n_cols-1));
arma::mat validY = valid.row(0) + 1;
Dataset dataset(trainX, trainY, validX, validY);
convertModel(fileName, dataset);
```
The ```trainModel()``` has not been overridden here but it may be necessary in most cases. However, it should be noted that most but not all layers, initialization types, loss functions and optimizers are supported by this converter.
An example of a JSON file containing all the details can be specified as:
```
{
  "loss": {
    "type": "negativeloglikelihood"
  },
  "init": {
    "type": "glorot"
  },
  "optimizer": {
    "type": "adam",
    "stepsize": 5e-3,
    "batchsize": 64,
    "tolerance": 1e-8,
    "cycles": 20
  },
  "network": [
    {
      "type": "linear",
      "units": 200
    },
    {
      "type": "relu"
    },
    {
      "type": "linear",
      "units":  100
    },
    {
      "type": "relu"
    },
    {
      "type": "dropout",
      "ratio": 0.2
    },
    {
      "type": "linear",
      "units": 10
    },
    {
      "type": "softmax"
    }
  ]
}
```
### ONNX-mlpack converter
Given the ONNX model path and the desired path for storing the converted mlpack model, the converter can do the rest. However, for converting models that take images as input, i.e., convolutional models, the image width and height need to be mentioned too. An example of the usage is:
```
convertModel("LinearModel.onnx", "ConvertedLinearModel.bin"); /* for a linear model */
convertModel("ConvModel.onnx", "ConvertedConvModel.bin", 32, 28); /* for a convolutional model with input image height 32 and width 28 */
```
To be noted is that most but not all layers are till now supported by this converter.
### mlpack-Torch converter
This converter provides an API similar to the previous one. An example would be:
```
convertModel("Model.bin", "ConvertedModel.pth");
```
In case the case of convolutional models too, the input image dimensions **need not be** mentioned.
For directly obtaining the Torch model from a given mlpack model, the ```convert()``` function can be used as shown below:
```
torch::nn::Sequential convertedModel = convert(ffnModel); /* ffnModel is of type mlpack::ann::FFN<> */
```
This converter also has some limitations pertaining to the layers that can be converted. Moreover, this converter is not yet in working state right now because of a number of yet to be merged PRs in the main mlpack repository.
### Additional Pull Requests
The above converters did require a number of changes to the original mlpack repo and are listed as follows:
- [1985](https://github.com/mlpack/mlpack/pull/1985) adds accessor and modifier methods to a number of layers.
- [1958](https://github.com/mlpack/mlpack/pull/1958) originally meant to add the softmax layer to mlpack's ANN module but the PR itself is a bit messed up (has unwanted files associated with it) and needs to be pushed again.

There are also a couple of pull requests that require some rectification before I can push them.

# Acknowledgements
I owe the completion of this project to the entire mlpack community for helping me out whenever I got stuck. My mentor Atharva had given me the exact guidance and support I required during this period. My concepts about backpropagation have been crystal clear after we manually wrote down the steps on [paper](https://lh3.googleusercontent.com/-6Z9VAG_nQ8Q/XTiXp4A5zjI/AAAAAAAABjM/v_T0OsQiEp8Bhd87it8VP4YSQ2prr6neQCK8BGAs/s0/2019-07-24.jpg). He used to give me hints to encourage me and in the end I could do it entirely by myself. Understanding this as well as mlpack's way of implementing them (the matrices *g* and *gy* in the ```Backward()``` function were the confusing ones) took around an entire week but it was a fun experience. This is just one instance, there were many more during this 12 week period. Marcus and Ryan were also no less than pseudo-mentors for me.

Marcus was my go to person during the Summer for any doubt regarding the C++ implementation of the mlpack ANN implementation or pretty much anything [else](https://gist.github.com/zoq/595906a62690befce85e3935ccc84f9f). I have a habit of spending too much time on things that seem difficult to solve, sometimes a couple of days (when I should have ideally tried for a couple of hours before asking for help) and even if I fail to solve it, I would ask Marcus on the IRC and we would arrive at a solution in less than an hour.

Ryan has been a constant source of support since my association with mlpack. When I had started with an [issue](https://github.com/mlpack/mlpack/issues/1254), back sometime in February, Ryan had helped me [design](https://github.com/mlpack/mlpack/issues/1254#issuecomment-475751183) the layout of the program which would later be the JSON model parser. There were numerous other instances during this period (and many more to come) when my code wouldn't work and Ryan would help me solve it.

Last but not the least, I have also learnt a lot from the general discussions in IRC and would like to thank each and everyone in the mlpack community for the brilliant interaction. I would also like to thank Google for giving me this opportunity to get involved in open source and with the mlpack community in particular.

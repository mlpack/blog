@brief  Application of ANN Algorithms Implemented in mlpack - Summary
@author Mehul Kumar Nirala
@page  Mehul2019Summary Application of ANN Algorithms Implemented in mlpack - Summary
@date 2019-08-21 23:00:00

@section Mehul2019Summary Application of ANN Algorithms Implemented in mlpack

# Works

All GSoC contributions can be summarized by the following.

**Contributions to mlpack/models**

**Pull Requests**
* [VGG19 on Imagenet dataset. #32](https://github.com/mlpack/models/pull/32)
* [Added LSTM Sentiment Analysis. #31](https://github.com/mlpack/models/pull/31)
* [Added LSTM Univariate Time series analysis #30](https://github.com/mlpack/models/pull/30)
* [Added LSTM for multivariate time series. #29](https://github.com/mlpack/models/pull/29)
* [Added VGG19 Model for MNIST Dataset. #28](https://github.com/mlpack/models/pull/28)

**Contributions to mlpack/mlpack**

**Pull Requests**
* [Added support for Loading image #1903](https://github.com/mlpack/mlpack/pull/1903)
* [Rectified imports in Python documentation #1820.](https://github.com/mlpack/mlpack/pull/1820)
* [Added cellState as output params in LSTM. #1800.](https://github.com/mlpack/mlpack/pull/1800)
* [Added quoted_strings to regex in LoadCSV #1756.](https://github.com/mlpack/mlpack/pull/1756)
* [Added additional check to LoadARFF #1793.](https://github.com/mlpack/mlpack/pull/1793)
* [Make models more accessible in Python #1771.](https://github.com/mlpack/mlpack/pull/1771)
* [Rectified ann.txt (mlpack/doc) #1731.](https://github.com/mlpack/mlpack/pull/1731)
* [Added .pyc in .gitignore #1721.](https://github.com/mlpack/mlpack/pull/1721)

**Issues Created**
* [LoadARFF gets stuck if file is not found #1791.](https://github.com/mlpack/mlpack/issues/1791)
* [Exposing Cell and hidden state in LSTM #1782.](https://github.com/mlpack/mlpack/issues/1782)
* [Cannot load text in CSV files #1754.](https://github.com/mlpack/mlpack/issues/1754)

**Contributions to zoq/gym_tcp_api**

**Pull Requests**
* [Maintenance work for compatibility with the OpenAI gym #13.](https://github.com/mlpack/mlpack/pull/1791)

## Loading Images
Image utilities supports loading and saving of images.

 It supports filetypes jpg, png, tga,bmp, psd, gif, hdr, pic, pnm for loading and jpg, png, tga, bmp, hdr for saving.

 The datatype associated is unsigned char to support RGB values in the range 1-255. To feed data into the network typecast of `arma::Mat` may be required. Images are stored in matrix as (width * height * channels, NumberOfImages). Therefore imageMatrix.col(0) would be the first image if images are loaded in imageMatrix.

Loading a test image. It also fills up the ImageInfo class object.
@code

    data::ImageInfo info;
    data::Load("test_image.png", matrix, info, false, true);

@endcode

Similarily for saving images.
@code

    const size_t width = 25;
    const size_t height = 25;
    const size_t channels = 3;
    const size_t quality = 90;
    data::ImageInfo info(width, height, channels, quality);
    data::Save("test_image.bmp", matrix, info, false, true);

@endcode

## VGG19
VGG-19 is a convolutional neural network that is trained on more than a
million images from the ImageNet database. The network is 19 layers
deep and can classify images into 1000 object categories. Details about
the network architecture can be found in the following arXiv paper:
For more information, read the following paper:

@code

    @article{Clevert2015,
      author  = {Simonyan, K. and Zisserman, A.},
      title   = {Very Deep Convolutional Networks for Large-Scale Image Recognition},
      journal = {CoRR},
      year    = {2014}
    }

@endcode
 
### Tiny Imagenet

Tiny ImageNet Challenge is the default course project for Stanford [CS231N](http://cs231n.stanford.edu/). It runs similar to the [ImageNet challenge](http://www.image-net.org/challenges/LSVRC/2014/) (ILSVRC). The goal of the challenge is for you to do as well as possible on the Image Classification problem.
The model uses VGG19 to classify the images into 200 classes.

### MNIST handwritten digits

The VGG19 model used for classification. It creates a sequential layer that encompasses the various layers of the VGG19.

@code

    // Input parameters, the dataset contains images with shape 28x28x1.
    const size_t inputWidth = 28, inputHeight = 28, inputChannel = 1;
    bool includeTop = true;

    VGG19 vggnet(inputWidth, inputHeight, inputChannel, numClasses, , "max", "mnist");
    Sequential<>* vgg19 = vggnet.CompileModel();

    // Compiling the architecture.
    FFN<NegativeLogLikelihood<>, XavierInitialization> model;
    model.Add<IdentityLayer<> >();
    model.Add(vgg19);
    model.Add<LogSoftMax<> >();

@encode

## Sentiment Analysis

We will build a classifier on IMDB movie dataset using a Deep Learning technique called RNN which can be implemented using Long Short Term Memory (LSTM) architecture.
The encoded dataset for IMDB contains a vocab file along with sentences encoded as sequences. A sample datapoint [1, 14, 22, 16, 43, 530,..., 973, 1622, 1385, 65]. This sentence contains 1st word, 14th word and so on from the vocabulary.

A vectorized input has to be fed into the LSTM to explot the RNN architecture. To vectorize the sequence dictionary encoding is used. The sample shown would be transformed to [[1, 0, 0,.., 0], [0,..,1,0,...], ....], here the first list has !st position as 1 and rest as 0, similarly the second list has 14th element 1 and rest 0. Each list has a size of the numbers of words in the vocabulary.

**Accuracy Plots**
![SA](https://user-images.githubusercontent.com/23444642/62192158-b7195a80-b392-11e9-819e-c7edc8c8a6dc.png)

## Time Series Analysis

### Multivariate
We want to use the power of the LSTM in Google stock prediction using time series. We will use mlpack and Recurrent Neural Network(RNN).

@code

    // No of timesteps to look in RNN.
    const int rho = 25;
    size_t inputSize = 5, outputSize = 2;
     // RNN model.
    RNN<MeanSquaredError<>,HeInitialization> model(rho);
    model.Add<IdentityLayer<> >();
    model.Add<LSTM<> > (inputSize, 10, maxRho);
    model.Add<Dropout<> >(0.5);
    model.Add<LeakyReLU<> >();
    model.Add<LSTM<> > (10, 10, maxRho);
    model.Add<Dropout<> >(0.5);
    model.Add<LeakyReLU<> >();
    model.Add<LSTM<> > (10, 10, maxRho);
    model.Add<LeakyReLU<> >();
    model.Add<Linear<> >(10, outputSize);

@endcode

**MSE Plot**
![Figure_1-1](https://user-images.githubusercontent.com/23444642/61946563-92069f80-afc0-11e9-9788-c396376a6aa8.png)

### Univariate

Implementation of an example of using Recurrent Neural Network (RNN) to make forcasts on a time series of electric usage (in kWh), which we aim to solve using a recurrent neural network with LSTM.

**MSE Plot**
![Figure_1](https://user-images.githubusercontent.com/23444642/62147853-17b68200-b316-11e9-84d5-1aa4dffaf796.png)

Results on other datasets - International Airline Passengers

This is a problem where, given a year and a month, the task is to predict the number of international airline passengers in units of 1,000. The data ranges from January 1949 to December 1960, or 12 years, with 144 observations.

We will create a dataset where X is the number of passengers at a given time (t) and Y is the number of passengers at the next time (t + 1) over the period of 'rho' frames.

Mean Squared error upto 10 iterations.
Training ...

    1 - MeanSquaredError := 0.146075
    2 - MeanSquaredError := 0.144882
    3 - MeanSquaredError := 0.09501
    4 - MeanSquaredError := 0.0875479
    5 - MeanSquaredError := 0.0836975
    6 - MeanSquaredError := 0.0796567
    7 - MeanSquaredError := 0.0804368
    8 - MeanSquaredError := 0.0803483
    9 - MeanSquaredError := 0.0809061
    10 - MeanSquaredError := 0.076797
    ....

**MSE Plot**

![Plot](https://user-images.githubusercontent.com/23444642/62627150-6e3f4400-b946-11e9-9a24-1542e564da42.png)

# Future Work
The tutorial associated with the models implemented are not published to mlpack webpage. The blogs are needed to be linked to a common place for the user. VGG19 is being trained on tiny-imagenet dataset, the results of which will be added.

# Acknowledgement
I am sincerely grateful to the whole `mlpack` community especially Ryan Curtin, Marcus Edel, Sumedh Ghaisas, Shikhar Jaiswal for the support I received. It was an awesome experience. 

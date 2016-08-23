Title: We need to go deeper, Googlenet : Project Summary
Date: 2016-08-23 11:30:20
Tags: gsoc, googlenet, edge_boxes, CNN, deep learning
Author: Nilay Jain

This blogpost discusses the project summary and my contributions over the summer, as GSoC 2016, approaches its conclusion. First we'll discuss how you can find most of the work that I did, this will be a list of commits from [mlpack][mlpack] or from various branches in my [fork][fork]. Then we'll discuss what were the goals of the project, and how much we accomplished them, and finally what I learnt over the summer and why working on this project with my mentors was great! :)

# Project Summary

The goal of this project was to develop googlenet such that it integrates in mlpack's existing ANN API and the modules developed are reusable to other related applications.

We selected the [edge_boxes][edge_boxes] algorithm for object localization. We performed the feature extraction [703][703] for a sample BSDS500 Dataset. Marcus helped with reusing the Tree implementation to train the structured random forest which detects edges in the image. Next, we started implementing the Neural Net part. We added functionality to the [pooling layer][pooling_layer], [convolutional layer] [conv_layer] and implemented the [inception layer][inception_layer] (which is replicated throughout googlenet), [concatenation layer][concat_layer], [subnetwork layer][subnet_layer] and [connect layer][connect_layer] as additional layers and wrote the [tests][tests] for them. This will give mlpack users a significant flexibility in training more complicated and deep neural nets. We made the [GoogleNet][googlenet] using these layers. Tests of our implementation on standard datasets still need to be finished.
Here is the list of commits and pull requests (from recent to old) in different branches, with their description, you can see to track the work done over summer:

 * [Googlenet, connect_layer implementation][googlenet_commits]
 * [inception_layer, subnet_layer, concat_layer implementation][inception_layer_commits]
 * [conv_layer modified][conv_layer_commits]
 * [pool_layer modified, arma backports][master_commits]
 * [edge boxes feature extraction][fm]
 * [edge boxes PR][703]
 * [inception layer PR][757]

To see the week by week progress of the work done you can look at the [blog][blog].

# Feature Extraction

For feature extraction the objective was that given images, segmentations and boundaries extract over 7000 features for different color spaces, gradient channels to capture the local edge structure in the images. [Fast edge detection using structured forests][edge_detection] and [Sketch tokens][sketch_tokens] are the papers that describe this task.

We began this process by first writing useful Image Processing algorithms to convert between color spaces (RGB to LUV), interpolating & padding images, performing convolutions, computing HOG features and calculating distance transforms. The distance transform algorithm is implemented in [this][distance_transform] paper.
Then we calculated Regular and Self Similarity features on a 16x16 image patches, for 1000 edge locations and 1000 non-edge locations. For this we also shrunk channels to reduce the dimensionality of our data, and then discretized our features into classes by performing PCA, so the data could be represented by a normal decision tree or random forest. The implementations of these algorithms can be seen in [703][703]. Then I wrote the [tests][edge_boxes_test] for the functions implemented in the StructuredForests class and compared values against the reference implementations to verify their correctness. Marcus helped by providing implementation of the structured tree using the feature extraction code.

# Inception Layer

Next, we proceeded to implement the Inception Layer. Before doing this, I needed to read some papers [alexnet][alexnet], [visualizing CNNs][vcnn] to understand some CNN architectures and some ideas like [Network in Network][network_in_network], that Googlenet paper uses by replicating the inception network inside it 9 times. It took time to understand the mlpack CNN class implementation as it uses interesting techniques of generating code using compile time recursion on templates which I was previously oblivious of. Then we made an inception layer as a collection of layers as mentioned in [googlenet paper][googlenet_paper] and wrote the tests for it to verify correctness. The implementation of inception layer can be seen in [757][757].

# Adding functionality to Pooling Layer and Convolution Layer

While writing tests for inception layer, it was noticed that some functionalities of the existing classes need to be modified. For the pooling layer I added the functionality to pool with a given stride [value][pooling_layer]. Then we improved the [convolution layer][conv_layer] to support Forward, Backward and Gradient updates when padding is specified. Padding is very important for deep networks, as we are able to preserve the width of our data by specifying padding, otherwise the data will become smaller as we continue to perform pooling and convolution operations on it, and we will not be able to get a neural net "deep enough". Then I wrote the tests for the pooling layer and convolution layer, and now the test for inception layer passed correctly too!

# Concatenation Layer and Subnetwork Layer

On Examining the structure of the googlenet network, we felt that we need a concatenation layer. This layer will give us the functionality to concatenate the outputs of two or more layers in the forward pass, and then distribute the errors among the constituent layers for the backward pass. So I wrote a concat_layer that does exactly [this][concat_layer] and the corresponding [tests][concat_layer_test].

The goal of this project was to create the components of googlenet so they are also reusable to other applications. So to make duplicating any collection of layers in a deep network easier, we decided to implement a [subnet layer][subnet_layer]. The tests for the subnet layer is still under construction which will implement the inception_layer using the subnet_layer and check for correctness.

# Connect Layer

With the googlenet network we faced one more interesting problem - auxillary classifiers. From one layer, there could be 2 layers diverging, and both of these layers would end up at separate output layers. Auxillary classifiers are added to googlenet to combat [vanishing gradient problem][vanishing_gradients] while providing regularization. In mlpack implementation, the layers are stacked sequentially in the form of a tuple. To support this architectural variant, where 2 layers emerge from one layer, we added a [connect layer][connect_layer], which contains the 2 separate nets that emerge from it, and has responsibility for passing input to and collect errors from these nets. Tests still need to be written to for the connect layer. 

# Googlenet

After all the basic components have completed, creating googlenet is as simple as stacking up all of the layers, put the desired values from the [paper][googlenet_paper] and calling the Train() and Predict() functions of CNN class to evaluate outputs. When we are able to complete all refinements we need to make to, all the components developed in this project, training deep neural nets with mlpack will become effortless. There is also one variant of googlenet which uses [batch normalization][batch_norm], that I plan to contribute to mlpack with the guidance of Marcus after GSoC 2016.

# ToDo

The following things still need to be completed in order to achieve all the goals mentioned in our proposal:
 1. Complete the edge boxes implementation.
 2. Write rigorous tests for googlenet.
 3. Minor improvements suggested by my mentors in the current Pull requests.

# Acknowledgements

I want to thank the mlpack community for giving me this awesome opportunity to work with them on this amazing project over the summer. I was welcomed right from the first day I joined the [irc channel][irc] in the beginning of the student application period, when I wasn't even sure what project I wanted to apply to for GSoC 2016. Special Thanks to my mentors Marcus Edel and Tham Ngap Wei, for clearing all my doubts (sometimes even unrelated to the project :) ) with so much patience and simple explainations, and helping me with design and debugging of the project. I feel I have learnt a lot from them, and I really enjoy being part of the mlpack community. This was a great experience, Thank you very much!

[mlpack]: https://github.com/mlpack/mlpack
[fork]: https://github.com/nilayjain/mlpack
[edge_boxes]: https://www.microsoft.com/en-us/research/publication/edge-boxes-locating-object-proposals-from-edges/
[703]: https://github.com/mlpack/mlpack/pull/703
[pooling_layer]: https://github.com/mlpack/mlpack/blob/master/src/mlpack/methods/ann/layer/pooling_layer.hpp
[conv_layer]: https://github.com/nilayjain/mlpack/blob/convlayer/src/mlpack/methods/ann/layer/conv_layer.hpp
[inception_layer]: https://github.com/nilayjain/mlpack/blob/inception_layer/src/mlpack/methods/ann/layer/inception_layer.hpp
[concat_layer]: https://github.com/nilayjain/mlpack/blob/inception_layer/src/mlpack/methods/ann/layer/concat_layer.hpp
[subnet_layer]: https://github.com/nilayjain/mlpack/blob/googlenet/src/mlpack/methods/ann/layer/subnet_layer.hpp
[connect_layer]: https://github.com/nilayjain/mlpack/blob/googlenet/src/mlpack/methods/ann/layer/connect_layer.hpp
[googlenet]: https://github.com/nilayjain/mlpack/blob/googlenet/src/mlpack/methods/ann/googlenet.hpp
[googlenet_commits]: https://github.com/nilayjain/mlpack/commits/googlenet/?author=nilayjain
[inception_layer_commits]: https://github.com/nilayjain/mlpack/commits/inception_layer/?author=nilayjain
[conv_layer_commits]: https://github.com/nilayjain/mlpack/commits/convlayer/?author=nilayjain
[fm]: https://github.com/nilayjain/mlpack/commits/fm/?author=nilayjain
[master_commits]: https://github.com/mlpack/mlpack/commits/master?author=nilayjain
[757]: https://github.com/mlpack/mlpack/pull/757
[blog]: http://mlpack.org/gsocblog/author/nilay-jain.html
[edge_detection]: https://arxiv.org/pdf/1406.5549.pdf
[sketch_tokens]: http://people.csail.mit.edu/lim/paper/SketchTokens_cvpr13.pdf
[distance_transform]: http://www.cs.cornell.edu/~dph/papers/dt.pdf
[edge_boxes_test]: https://github.com/nilayjain/mlpack/blob/72eb1ef22c7db1ea33af3de1cd043cdb277ec562/src/mlpack/tests/edge_boxes_test.cpp
[alexnet]: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
[vcnn]: https://www.cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf
[network_in_network]: https://arxiv.org/abs/1312.4400
[googlenet_paper]: http://www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf
[concat_layer_test]: https://github.com/nilayjain/mlpack/blob/googlenet/src/mlpack/tests/concat_layer_test.cpp
[vanishing_gradients]: https://en.wikipedia.org/wiki/Vanishing_gradient_problem
[batch_norm]: http://arxiv.org/abs/1502.03167
[irc]: http://webchat.freenode.net/?channels=mlpack
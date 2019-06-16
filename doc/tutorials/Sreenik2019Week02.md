@brief Implementing An Mlpack-Tensorflow Translator
@author Sreenik Seal
@page Sreenik2019Week02 Implementing An Mlpack Tensorflow Translator - Week 2
@date 2019-06-13 00:15:00

@section Sreenik2019Week02 Implementing An Mlpack Tensorflow Translator - Week 2

As I have apparently missed writing a blog on the first week's work, I think it would be a bad idea to directly jump into what I could and not accomplish in the second week before introducing my project. So if I have not yet been able to reach you through this project (reality is often disappointing), the following paragraph is for you.

The project title very purposefully (mis)leads one into thinking that it is just about the interconversion of neural network models between mlpack and Tensorflow. Well, interestingly enough, Microsoft and Facebook have been pouring bitcoins into an open-source initiative called ONNX, which stands for Open Neural Network Exchange. Now, ONNX provides a junction point for the interconversion of pretrained models among a number of supported frameworks like Tensorflow, Pytorch, Caffe, Chainer, etc. So we are taking advantage of this effort run by the big guns and creating a converter for ONNX only. That being said, this is more of an Mlpack-ONNX converter.

This week has seen me fine tuning the json parser (found under unmerged PRs in github) I had created previously, to fit the need of this converter. Having done that, I moved on to start mapping the ONNX network layers I plan to support, to their corresponding mlpack layers. It was a difficult time discovering the layers that cannot be supported as of yet due to incompatibility in the number and types of parameters. One more thing that required planning was deciding the data structure to use for this purpose. However, what I spent more time thinking about was how to transfer the weights of the pretrained model, which I eventually found at the end of the week thanks to Marcus (more on that in my next blog). Sadly, I had a lot of OS issues during this week and had to finally reinstall the OS (thanks to my mentor Atharva for being supportive through this). If I haven't mentioned this already, this is the first phase of this project, i.e., conversion of pretrained ONNX models to mlpack models. The second phase would be the conversion of pretrained mlpack models to ONNX models.

This is all for this week. I plan to accomplish the transfer of weights by next week (spoiler: it was kinda completed just before the author started writing this post :D) along with some small issues that need to be taken care of. The converter would need some testing with pretrained ONNX models before being considered fit for use.

If you've read this far, here's something for you from Reddit:
"When I was little, I had a disease that required me to eat dirt three times a day to survive...
Good thing my elder brother told me about it."

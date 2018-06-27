@brief Variational Autoencoders - Week 6
@author Atharva Khandait
@page Atharva2018Week06 Variational Autoencoders - Week 6
@date 2018-06-27 09:00:00

@section Atharva2018Week06 Variational Autoencoders - Week 6

We finally got the Sampling PR merged which is a huge step towards building models. After the two currently open PRs get merged, I will start building a VAE model in models repository. We have decided to go with normal MNIST against binary MNIST.

The gradient check for the ReconstructionLoss class was finally debugged. It required some changes in the architecture of the NormalDistribution class. The NormalDistribution class had become too specific to the ANN module and hence we decided to move it to the ann folder under a new dists folder. The common functions in ann_layer_test.cpp were moved to a new file ann_test_tools.hpp. The PR was split into two. We decided to test the distributions with jacobian test instead of the reconstruction loss. The jacobian of the NormalDistribution class is currently failing.
@brief Variational Autoencoders - Week 4
@author Atharva Khandait
@page Atharva2018Week04 Variational Autoencoders - Week 4
@date 2018-06-11 22:00:00

@section Atharva2018Week04 Variational Autoencoders - Week 4

This week, I tested the Sampling layer, now renamed to Reparametrization layer without the KL divergence being added to the total loss of the network. Some time went into the debugging of the failing Numerical gradient test.

Sumedh and I decided to come with defined weekly goals to boost productivity. It worked like a charm. The tasks planned for the 5th week have already been completed. It included implementing a Loss visitor to collect loss from intermediate layers of a FFN network and add it in the Evaluate and Backward function of the FFN class. Next task was to test a simple VAE network with both reconstruction and KL loss. Both the tasks have been completed.

We haven't get decided whether or not to have a seperate class for VAE. I think it will be really useful for some of the more complex functions of VAEs which will prove to be too much of a hassle to implement everytime with the FFN class. The decision will be taken on discussion with Sumedh, Marcus and Ryan. If yes, then this week's task will be to implement the VAE class with support for feedforward networks.
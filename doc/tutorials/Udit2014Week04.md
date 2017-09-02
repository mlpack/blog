Title: Implementation of Multi-Class Adaboost Algorithm: Week 4 - Committing Decision Stumps. 
Date: 2014-06-17 23:30:00
Tags: gsoc, adaboost, decisionstump, binning, tests, Jenkins, perceptron
Author: Udit Saxena

Well, that's decision stump for you ! I finally pushed decision stumps on to the main repo, after writing a couple of pretty important tests. Felt exhilirating - that is until Jenkins sent me a couple score of emails regarding warnings, unused variables and uninitialized variables. I never actually thought that the nighthly build would be unstable because of an uninitialized variable. 

There was also the issue of backward compatibilty of armadillo - the older versions were devoid of the ::fill constructors. Instead, I had to go the long way around to solve this. 

I'm glad Ryan was there, otherwise it might have been difficult. Anyways, with some minor changes, I recommitted and Jenkins sent another score of mails, each one concerning the previous warning mails. 

Anyways, Week 5 is about implementing the perceptron, which seems fairly simple and straightforward.
Collaborative filtering package improvements : Week 1-2 Highlights
==================================================================

2 weeks of fun coding. Most of the time is spent designing the abstraction and user interface. 
The following additions/modifications were made -

		1)	Additions of Alternating Matrix Factorization(AMF) module to accomodate both NMF and SVD update rule. 
		2)	All the NMF update rules and initialization rules have been shifted to AMF and NMF module is simplified to basic main function which uses 				AMF 	module.
		3)	Collaborative filtering module modified to use AMF instead of NMF. This change will let CF-module to use SVD factorization.
		4)	WUpdate and HUpdate classes are combined into one class per update rule.
		
The next task would be too to test sparse NMF and implement it as a new update_rule. Addition of regularization will follow. 
Thank you for visiting...



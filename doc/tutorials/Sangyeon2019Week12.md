@brief Quantum Gaussian Mixture Models - Week 12
@author Sangyeon Kim
@page Sangyeon2019WeekTwelve Quantum Gaussian Mixture Models - Week 12
@date 2019-08-17 17:00:00

@section Sangyeon2019WeekTwelve Quantum Gaussian Mixture Models - Week 12

This week, I comapared QGMM with GMM using the percentage of the convergence on the clusters of the observations as an indicator of the training performance. With a total of 200 experiments, I checked QGMM showed good performance when the initial phi 0, while phi 90 was bad. When we set the initial phi as 0, it wasn't changed from the initial value, but when we set the initial phi as 90, it increased between 91 ~ 269. Therefore, the cosine of phi became negative and the two distributions were overlaid. Actually, I tried to control the value of phi, but I didn't get any workaround. Thus, I should come up with the method to control the phi properly for stable performance.

Lastly, I checked the difference between the augmented and normal Lagrangian multipliers updating lambda every 1000 iterations. Surely, when using the augmented Lagrangian method, it's easy to set the initial lambda for some cases in which we don't know the proper initial value, but if we can set the proper lambda initially, the normal Lagrangian showed better performance overall. I think I should look into this research later with additional data sets because there are some hyperparameters in the augmented method as well. 

Thanks for reading :)

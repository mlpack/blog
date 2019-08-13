@brief Quantum Gaussian Mixture Models - Week 10
@author Sangyeon Kim
@page Sangyeon2019WeekTen Quantum Gaussian Mixture Models - Week 10
@date 2019-08-03 14:12:00

@section Sangyeon2019WeekTen Quantum Gaussian Mixture Models - Week 10

This week, I've researched the performance 래 the five clusters case. I generated the data set using mlpack GMM class. When training, the value 0 was good as an initial difference of phi. From some experiments, I figured out that as the difference neared zero, the two clusters showed a tendency to move away, while as the difference neared negative one, the two clusters tended to be close.
Lastly, I think it would be nice to take a closer look at the correlation between phi and other parameters to utilize the variation of phi more efficiently.

<center>
<b>[Visualization for the training process]</b>
<p>
<img src = "images/5_clusters_QGMM.gif" width = "640" height = "480" hspace = "10"/>
</p>
</center>
<br>

Thanks for reading :)

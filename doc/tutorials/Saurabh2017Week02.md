@brief Build testing with Docker and VMs - Week 2
@author Saurabh Gupta
@page Saurabh2017WeekTwo Build testing with Docker and VMs - Week 2
@date 2017-06-12 04:45:00

@section Saurabh2017WeekTwo Build testing with Docker and VMs - Week 2

Building packages from scratch in order to make docker image with mlpack's 
dependencies inside it is found  way too complicated to be pursued. That put
the thought of starting with busybox's image out of question.
So, the only option left (with minimal image size) is to make a debian based
docker image. 

Now, it was required to do some optimizations in order to reduce as much size
as can be done because no one wants a docker image which is too much in size.
Therefore, I followed this [blog](https://wiki.debian.org/ReduceDebian) to 
reduce the size. This step is followed by making the Dockerfile script and
installing necessary dependencies followed by hardening steps which was 
discussed in my previous blog. 

As said by Stephen Hawking's, one of the basic rules of the universe is that 
nothing is perfect. Perfection simply doesn't exist. And at the same time, I 
follow Kim Collins, who beleived in striving for continuous improvement, instead
of perfection. So, while looking for further ways of optimization, my mentor
suggested --squash(ing) images with docker. After reading about this method,
upgrading docker to v1.17 and enabling the tool, after squashing the image size
is reduced from ~609 MB to ~ 510 mB. To read about squashing follow this 
[link](https://blog.docker.com/2017/01/whats-new-in-docker-1-13/)

The stage is set, the image is ready to run inside a container and build mlpack.
While building I faced a large number of linking errors, all of which converge
to a single solution, i.e., to install c++ armadillo library from source instead
of using the package manager. After all this is done, now I am looking to add
some suitable docker plugin on Jenkins server (the masterblaster) to enable me
add build steps with Docker. 

Stay tuned for more updates from coming weeks! Keep coding!
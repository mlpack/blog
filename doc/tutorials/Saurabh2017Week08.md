@brief Build testing with Docker and VMs - Week 8
@author Saurabh Gupta
@page Saurabh2017WeekEight Build testing with Docker and VMs - Week 8
@date 2017-07-25 07:19:00

@section Saurabh2017WeekEight Build testing with Docker and VMs - Week 8


The next steps included running a container using a pre-built image,
building mlpack inside a container using a Jenkins plugin. I am using
[CloudBees Docker Custom Build Environment Plugin](https://wiki.jenkins.io/display/JENKINS/CloudBees+Docker+Custom+Build+Environment+Plugin).

Apart from that, a matrix configuration is to be created to create
images with different configurations and mlpack is to be installed,
run and tested against each image.

Also, I am looking for missing library versions.
Title: Build testing with Docker and VMs
Date: 2016-06-04 12:18:00
Tags: gsoc, docker, mlpack, containerization
Author: Saurabh Gupta

With getting selected in Google Summer of Code 2017 to work for the project mlpack
this is my first major opportunity to contribute to the open source community. 
Getting started with the work I realized how amazing the mentors are in 
this program. I am really thankful for getting an opportunity to work with  
**Ryan Curtin** for this project.

My first task was to run a simple docker container and building it using 
jenkins. The next step involved making a Docker image with all dependencies of
mlpack in order to run a container in which one can build mlpack. This is done
initially taking ubuntu:16.04 as the base image and installing dependencies on 
top of it. Now, as Ernest Hemingway once said "The first draft of everything 
is shit", so as this docker image with no hardening, susceptible to attacks, a
a non-acceptable size (too large ~ 420MB) and not matching the mlpack's coding 
standards. 

The feedback from the mentor is really helpful and certainly improves the 
quality of the end product. Considering the feedback, I started with 
alpine:latest as the base image (initial size ~ 5MB), and tried installing all
mlpack dependencies (boost-math boost-program_options boost-unit_test_framework
boost-serialization arpack txt2man binutils-dev cmake g++ make git openblas 
lapack-dev doxygen) to reduce the size to ~ 200 MB i.e. a 2x optimization in size.
To make the container more secure, instead of root a new user id added to the
container. For hardening, unsetting of all setuid bits is done, [followed this
blog](https://blog.tutum.co/2015/02/03/hardening-containers-disable-suid-programs/)
. And, finally following the coding standards set by mlpack. 

More on alpine based docker image: As we know alpine linux is small with many
packages missing in the package manager. While working with it, I realized that
there is no package for armadillo (c++ linear algebra library) and I have to
build it from scratch. 
After completing building mlpack on this alpine linux based container, while 
running the tests, it stops with errors. It cannot find the libarmadillo.so.x
installed on the system. On further investigation and help from the mentor, 
turns out Alpine ships with uclibc not glibc and this will cause many other issues
and will produce a build environment too far away from what mlpack's users 
typically have. So, now I'll be trying building the image using another minimal 
base image (for eg. busybox with glibc).

Stay tuned for more updates. Coding is fun! so as reading this blog, isn't it? 


Title: Build testing with Docker and VMs Week 7
Date: 2017-07-18 11:22:00
Tags: gsoc, docker
Author: Saurabh Gupta


After resolving a lot of issues with clang and gcc compilers I ,finally,
got them working i.e. installing mlpack successfully and completed 
running the test with no errors detected.

Apart from this, shell scripts are created to generate the Dockerfile
automatically. The advantage of this is, I do not have to create Docker
images of all configurations beforehand. I can run these scripts 
mentioning the desired armadillo, boost and gcc/clang versions and then, 
can create a docker image with the generated Dockerfile. 

Now, I have to make Jenkins build mlpack inside a container. Also,
I need to find and put tar balls of all different desired versions of 
armadillo, boost, gcc/clang on the Apache server.

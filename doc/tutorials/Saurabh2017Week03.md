@brief Build testing with Docker and VMs - Week 3 + 4
@author Saurabh Gupta
@page Saurabh2017WeekThree Build testing with Docker and VMs - Week 3 + 4
@date 2017-06-27 03:00:00

@section Saurabh2017WeekThree Build testing with Docker and VMs - Week 3 + 4


This time, I collected different versions of armadillo and boost libraries.
Installed apache2 on masterblaster to enable the downloading of  tar balls 
of these libraries inside docker container.
Also, I successfully build armadillo and boost libraries inside the container.
Now, since I know the process it will not take long to create a shell script
and replicating the findings to create Dockerfile programmatically. 

Apache2, while downloading the files, gave 403 error. So, I followed this
[blog](https://askubuntu.com/questions/767504/permissions-problems-with-var
-www-html-and-my-own-home-directory-for-a-website) to resolve the issue.
Now, the versions of armadillo and the versions of boost can now be downloaded 
and different dockerfiles can be generated automatically for different versions.

Before creating the final shell script to generate the dockerfile programma-
-tically, I am looking to make clear the process to install all the remaining
iterations (different gcc and clang versions, cmake release modes, architectures)
so that the shell script can be generated in one go. 

Currently, I am trying to install gcc compiler from source. Once this is done,
I am going to do the same for clang.
@brief Build testing with Docker and VMs - Week 5
@author Saurabh Gupta
@page Saurabh2017WeekFive Build testing with Docker and VMs - Week 5
@date 2017-07-03 19:25:00

@section Saurabh2017WeekFive Build testing with Docker and VMs - Week 5


Passed in first evaluations, I am happy to continue the work in this project.
The feedback is really good from the mentor and I'll take care of the points 
mentioned in it. 

With the last PR, the Dockerfile which installs gcc, armadillo and boost from
source is ready. However, there are some changes required for them to be ready
to use. The docker image is tested with building mlpack inside a container run 
using this image. And, not only mlpack installed correctly, there were no errors
while building the test. 

After a lot of efforts and waiting, I was successfully able to create a docker
image with a dockerfile which installs clang, armadillo and boost from source.
clang here is used as an alternative to gcc. (By the way, installing clang takes 
more than 3 hours, that's why the wait). I am currently installing mlpack inside 
the container run using clang based docker image. There were a lot of warnings.
So, I am looking into this only.
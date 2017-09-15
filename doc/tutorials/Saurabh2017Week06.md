@brief Build testing with Docker and VMs - Week 6
@author Saurabh Gupta
@page Saurabh2017WeekSix Build testing with Docker and VMs - Week 6
@date 2017-07-12 10:07:00

@section Saurabh2017WeekSix Build testing with Docker and VMs - Week 6

After building first draft image with clang, there were a lot of problems with
the Dockerfile. I need to install the boost, armadillo, clang into the 
recommended system directory.

So, once these changes were done, there are further errors occured with
armadillo and for the first time with LAPACK.

Looking into those errors now!	

Also, I made the suggested changes in Dockerfile with gcc. That too generated
new errors. Will be looking into that too.
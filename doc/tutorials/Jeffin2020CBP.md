@brief Visualization Tool - Community Bonding Period
@author Jeffin Sam
@page Jeffin2020CBP Visualization Tool - Community Bonding Period
@date 2020-05-28 14:21:28

@section Jeffin2020CommunityBondingPeriod Visualization Tool - Community Bonding Period

Hi eveyone, Glad to tell that I was lucky enough to be accepted second time as gsoc student for the same org :). And this time I would be working to come up with a Visualization tool for mlpack. This time my mentors would be `Ryan Birmingham` know by github handle as `@brim` and Toshal Agarwal known by github handle as `@walragatver`.

During the community Bonding period we had several meetings to discuss about the high level desgin for the tool and we cam up with the following : 

The initial proposal is intended for enabling users to visualize Mlpack data using the TensorFlow's TensorBoard. The plan of this summer is to develop a logging tool for users to log data in the format that the TensorBoard can render in browsers. Thereby leavraging the power of tensorbaord's frontend and just focusing on the loggin part. The typical workflow is as follows :

<p>
<img src = "images/design.png" width = "300" height = "200"/>
</p>

Asynchronized logger : The logger would  be implemented asynchronously so that training of model or any other operation doesn't get effected. 

High Level Design : 

We plan to add  most of the data types that are aldeardy supported in tensorboard : `scaler` , `image`, `audio`, `text`, `histogram`, `embedding` and `pr-curve`.

class `Summary` : This class would be responsible to hold the data such as scaler summary or image summary and convert it to event and then push it the queue through the filewrite class.
class  `FileWriter` : This class is reponsible for writing events into the file through the logger thread.
class `SharebaleQueue` : This class is responsible to maintain a queue which could be thread safe and shared among the main thread (summary class)  and logger thread (filewrite class) 

The way whole workflow works is 

* The user creates a FileWriter object instance by providing the constructor with a path representing the location where data is going to be logged. For example: fw = FileWriter(logdir='./logs')
* Then a user can call the corresponding summary API to push the data to be logged into the event queue. For example, summary.add_scaler('test',1,13, fw). The arguments could be any depending upon the type of scaler along with the filewrite object. This filewriter internally pushes the event into shared queue.
* Parallely `writeEvent()` which is a logger thread access the shared queue and pops out element and then logs it into event file 

<p>
<img src = "images/workflow.png" width = "300" height = "200"/>
</p>

Acknowledgements and References : 
Special thanks to `@RustingSword`, author of `RustingSword/tensorboard_logger`, who provided insightful ideas and hours of discussion to help me understand the backened thoroghly.  Also some of the refrences are taken from the following repos. We would like to thank them for their good work :)

https://github.com/dmlc/tensorboard
https://github.com/TeamHG-Memex/tensorboard_logger
https://github.com/lanpa/tensorboard-pytorch 
https://github.com/reminisce/tensorboard-mxnet-logger


All of the above repos helped us to come up with design and also made it possible to understand how to log exactly independent of TensorFlow. And also gave us enough insights about the internal of tensorboard and tensorflow logging class.
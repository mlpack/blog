@brief Application of ANN Algorithms Implemented in mlpack - Week 4
@author Mehul Kumar Nirala
@page Mehul2019WeekFour Application of ANN Algorithms Implemented in mlpack - Week 4
@date 2019-06-25 10:15:00

@section Mehul2019WeekFour Application of ANN Algorithms Implemented in mlpack - Week 4

### Tasks
* Completed the PR on image saving feature.
* Written tutorials on how to use image utilities for loading and saving images.
* Added global max & mean pooling to VGG19 model.

## Results

Initially VGG19on minist dataset showed divergence,
```
Epoch 0
Loss after cycle 0 -> 310.261
Epoch 1
Loss after cycle 1 -> 223.393
Epoch 2
Loss after cycle 2 -> 2.83091e+10
Epoch 3
Loss after cycle 3 -> 6.03322e+45
```
So, I retuned the hyper parameters involving initialization and step size. I hope that it gives good results.

### Next Week Goals

* Completing the PR on Image Loading in accordance data::Load() and data::Save() API calls.
* Complete the documentation on VGG.
* Revise the tutorials for image loading/saving.

Thanks for reading. Have a nice day :smile:

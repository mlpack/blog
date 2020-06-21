@brief Visualization Tool - Week 03
@author Jeffin Sam
@page Jeffin2020Week03 Visualization Tool - Week 03
@date 2020-06-21 21:11:28

@section Jeffin2020Week03 Visualization Tool - Week 03

Hi, Welcome to the blog for the third week :)

This was one of the toughest week for me since the start of the GSoC program, Since I had to debug some cmake and protobuf issue. After numerous downloads and install of protobuf library, I was finally able to debug it. And hence catch testing has been finally setup up. Now I can focus on writing tests over the next week. Thanks to @shirt and @toshal for the help :).

Also, Support for logging of the image was added in a new [PR#6](https://github.com/mlpack/mlboard/pull/6). So both of the goals were accomplished which were set during the previous blog.

If you want to try the new Image Logging API for `arma::mat` , you can use the following snippet of code. 

Note : Please download the csv from [here](https://www.kaggle.com/c/digit-recognizer/data?select=train.csv)


```
#include <mlboard/mlboard.hpp>
#include <iostream>
#include <chrono> 
#include <ctime> 
#include <future>

using namespace std;
using namespace mlboard;
using namespace arma;
using namespace mlpack;

int main()
{
    GOOGLE_PROTOBUF_VERIFY_VERSION;

    std::chrono::time_point<std::chrono::system_clock> start, end; 
    start = std::chrono::system_clock::now(); 
    FileWriter f1("jeffin");
    mat tempDataset;

    // https://www.kaggle.com/c/digit-recognizer/data?select=train.csv
    data::Load("train.csv", tempDataset, true);

    // Specify the height width and channel.
    data::ImageInfo info(28, 28, 1, 90);


    arma::Mat<unsigned char> dataset = conv_to<  arma::Mat<unsigned char> >::from(tempDataset.submat(1, 1,
        tempDataset.n_rows - 1, 50)); 
    std::cout<<dataset.n_cols<<std::endl;
    std::cout<<dataset.n_rows<<std::endl;
    mlboard::SummaryWriter<mlboard::FileWriter>::Image(
         "Multiple Image", 1, dataset , info, f1, "Sample DIGITS Image",
         "This is a Sample image logged using mlboard ");
    f1.Close(); 

    end = std::chrono::system_clock::now(); 
    std::chrono::duration<double> elapsed_seconds = end - start; 
    std::time_t end_time = std::chrono::system_clock::to_time_t(end); 
    
    std::cout << "finished computation at " << std::ctime(&end_time) 
              << "elapsed time: " << elapsed_seconds.count() << "s\n"; 

    google::protobuf::ShutdownProtobufLibrary();
}

```

The outuput would be

```
50
784
finished computation at Sun Jun 21 20:42:49 2020
elapsed time: 4.10645s
```

It took around 4 sec to log 50 Images, and IMO that is really good. Also, To log 42000 images it took 67.6837s.

The ouput would be similar to

<p>
<img src = "images/mlboard_image.png" width = "600" height = "400"/>
</p>

Next week is the final week before the first phase ends, and therefore I would like to completely get rid of both the PR ( Image support and catch-testing ), and then focus on logging text, audio, histogram during the second phase. Till then Bye :)
#include <stdio.h>
#include <chrono>
#include <vector>
#include <math.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std::chrono;

// #pragma pack(push, 2)
struct BGR
{
    uchar blue;
    uchar green;
    uchar red;
};

int main(int argc, char **argv)
{
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<Mat> mats;
    int _i = 0;
    for (_i = 0; _i < pow(2, 9) * 3; _i++)
    {
        Mat image(256, 256, CV_8U);
        mats.push_back(image);
    }
    std::cout << _i << std::endl;
    // if (!image.data)
    // {
    //     printf("No image data \n");
    //     return -1;
    // }

    for (auto v : mats)
    {
        std::cout << v.rows << " " << v.cols << std::endl;
        for (int y = 0; y < v.rows; y++)
        {
            for (int x = 0; x < v.cols; x++)
            {
                v.at<uchar>(x,y) = 123;
                // v.
                // get pixel
                // Vec3b &color = v.at<Vec3b>(y, x);

                // ... do something to the color ....
                // color[0] = 13;
                // color[1] = 13;
                // color[2] = 13;

                // set pixel
                // v.at<Vec3b>(Point(x,y)) = color;
                //if you copy value
                // BGR* bgr = v->ptr<BGR>(y)[x];
                // bgr->blue = (uchar)13;
            }
        }
    }
    auto end = std::chrono::high_resolution_clock::now();\
    std::cout << "end for algo" << std::endl;
    // pre-show
    std::cout << mats.size() << " " << mats[0].rows << std::endl;
    namedWindow("Display Image", WINDOW_AUTOSIZE);
    imshow("Display Image", mats[0]);
    waitKey(0);
    //=========

    auto duration = duration_cast<milliseconds>(end - start);

    std::cout << "Finished work, time: " << duration.count() << "ms" << std::endl;
    return 0;
}
#include <stdio.h>
#include <chrono>
#include <vector>
#include <math.h>
#include "gl.h"
#include "util.h"
#include <fstream>
#include <boost/filesystem.hpp>
// #include <algorithm>
#include <string>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std::chrono;
using namespace std;

#define TILE_SIZE 256
#define MAX_ZOOM 6

void zoom_iteration(int zoom, const vector<coord> &letter_points)
{
    int scale = pow(2, zoom);
    int size = 3 * scale;

    // Calculate for pixel position
    START_TIMER(pixel_calc);
    vector<coord> pixels;
    for (auto xy : letter_points)
    {
        dot(pixels, xy.x * scale, xy.y * scale, scale);
    }
    END_TIMER(pixel_calc);

    // Making tile objects
    START_TIMER(making_tiles);
    vector<vector<Mat>> tiles;
    for (int i = 0; i < size; i++)
    {
        tiles.emplace_back();
        for (int h = 0; h < size; h++)
        {
            Mat tile = cv::Mat::zeros(cv::Size(256, 256), CV_8U);
            // Mat tile(256, 256, CV_8U);
            tiles[i].push_back(tile);
        }
    }
    END_TIMER(making_tiles);

    // Draw tiles
    draw_tiles(pixels, tiles, TILE_SIZE);

    // Save tiles
    START_TIMER(saving_tiles);

    for (int i = 0; i < tiles.size(); i++)
    {
        for (int h = 0; h < tiles[i].size(); h++)
        {
            boost::system::error_code error;
            boost::filesystem::path path("tiles");
            path /= std::to_string(zoom);
            path /= std::to_string(i);
            boost::filesystem::create_directories(path, error);
            
            string filename = std::to_string(h) + ".png";
            path /= filename;
            imwrite(path.string(), tiles[i][h]);        
            assert(!error);
        }
    }

    // imwrite("test.png", tiles[1][1]);
    END_TIMER(saving_tiles);

    // namedWindow("Display Image", WINDOW_AUTOSIZE);
    // imshow("Display Image", tiles[0][0]);
    // waitKey(0);
}

int main()
{
    //INIT
    vector<coord> letter_coords;
    {
        fstream letter_coords_file("letter_coords.txt", std::ios_base::in);
        float temp_x;
        float temp_y;
        while (letter_coords_file >> temp_x >> temp_y)
        {
            letter_coords.push_back({temp_x, temp_y});
        }
    }
    // ZOOM
    for (int zoom = 0; zoom < MAX_ZOOM; zoom++)
    {
        cout << "Zoom: " << zoom << endl;
        START_TIMER(Zoom);

        zoom_iteration(zoom, letter_coords);

        END_TIMER(Zoom);
    }
}

/*
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
*/
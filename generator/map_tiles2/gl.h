#include <opencv2/opencv.hpp>
#include <vector>
#include "util.h"
using namespace cv;
using namespace std;

struct coord
{
    float x;
    float y;
};

void dot(vector<coord> &pixels, float __x, float __y, int scale)
{
    int _x = __x;
    int _y = __y;
    for (int x = _x; x < _x + scale; x++)
    {
        for (int y = _y; y < _y + scale; y++)
        {
            pixels.push_back({(float)x, (float)y});
        }
    }
}

void draw_tiles(const vector<coord> &pixels, vector<vector<Mat>> &tiles, int tile_size)
{
    START_TIMER(draw_tiles);
    // Drawing
    for (auto xy : pixels)
    {
        tiles[(int)xy.x / tile_size][(int)xy.y / tile_size].at<uchar>((int)xy.x % tile_size, (int)xy.y % tile_size) = 255;
    }
    END_TIMER(draw_tiles);
}
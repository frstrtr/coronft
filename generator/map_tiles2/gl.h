#include <opencv2/opencv.hpp>
#include <vector>
#include "util.h"
using namespace cv;
using namespace std;

struct coord
{
    int x;
    int y;
};

void dot(vector<coord> &pixels, int _x, int _y, int scale)
{
    for (int x = _x; x < _x + scale; x++)
    {
        for (int y = _y; y < _y + scale; y++)
        {
            pixels.push_back({x, y});
        }
    }
}

void draw_tiles(const vector<coord> &pixels, vector<vector<Mat>> &tiles, int tile_size)
{
    START_TIMER(draw_tiles);
    // Drawing
    for (auto xy : pixels)
    {
        tiles[xy.x / tile_size][xy.y / tile_size].at<uchar>(xy.x % tile_size, xy.y % tile_size) = 255;
    }
    END_TIMER(draw_tiles);
}
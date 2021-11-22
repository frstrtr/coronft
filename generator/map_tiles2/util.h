#pragma once

#include <iostream>
#include <chrono>
using namespace std::chrono;

#define START_TIMER(name) \
    auto start_##name = std::chrono::high_resolution_clock::now();

#define END_TIMER(name) \
    auto finish_##name = std::chrono::high_resolution_clock::now();\
    auto duration_##name = std::chrono::duration_cast<milliseconds>(finish_##name - start_##name);\
        cout << "\t" << #name << " for: " << duration_##name.count() << "ms." << endl;


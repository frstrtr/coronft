cmake_minimum_required(VERSION 2.8)
project( GenTiles )
find_package( OpenCV REQUIRED )

find_package(Boost 1.71.0 COMPONENTS filesystem REQUIRED)
if(Boost_FOUND)
	MESSAGE( STATUS "Boost_INCLUDE_DIRS = ${Boost_INCLUDE_DIRS}.")
    MESSAGE( STATUS "Boost_LIBRARIES = ${BOOST_LIBRARYDIR}.")
    MESSAGE( STATUS "Boost_LIB_VERSION = ${Boost_LIB_VERSION}.")
endif()
include_directories(${Boost_INCLUDE_DIRS})


include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( GenTiles gen_tiles.cpp gl.h util.h)
target_compile_features(GenTiles PRIVATE cxx_std_17)
target_link_libraries( GenTiles ${OpenCV_LIBS} Boost::filesystem)
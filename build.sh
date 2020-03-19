#!/bin/bash
git submodule init
git submodule update --remote
cd Physics/
mkdir build
cd build
cmake ..
make
cp ./*.so ../../Simulator

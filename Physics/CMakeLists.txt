cmake_minimum_required(VERSION 3.0.0)
project(Physics VERSION 0.1.0)

set_property(GLOBAL PROPERTY CXX_STANDARD 17)
set(PYBIND11_CPP_STANDARD -std=c++1z)

add_subdirectory(pybind11)


pybind11_add_module(Physics
    src/main.cpp
    src/physics/PhysicsMotor.cpp
    src/physics/PhysicsObject.cpp
    src/utils/PeriodicProcess.cpp)


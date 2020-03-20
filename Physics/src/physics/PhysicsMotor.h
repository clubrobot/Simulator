#ifndef _PHYSICS_MOTOR_H_
#define _PHYSICS_MOTOR_H_


#include "../utils/PhysicsUtils.h"
#include "../utils/PeriodicProcess.h"
#include "PhysicsObject.h"
#include <iostream>
#include <map>
#include <vector>
#include <optional>
#include <pybind11/stl.h>
#include <pybind11/pybind11.h>


#define MAX_OBJECT  64
 	

class PhysicsMotor : public PeriodicProcess
{
public:


    //Constructor
    PhysicsMotor() : PeriodicProcess(10),  m_map({0}) {}


    // Map access
    void setMap(std::vector<std::tuple<float, float>> m){m_map.from_python(m);}
    std::vector<std::tuple<float, float>> getMap(){return m_map.to_python();}


    // Object access
    void addObject(std::string name);
    void removeObject(std::string name);
    std::optional<std::string> getObject(float x,float y,float threshold);
    void enableObject(std::string name);
    void disableObject(std::string name);

    void setShape(std::string name,std::vector<std::tuple<float, float>> poly);
    void setPosition(std::string name,float x,float y);
    void setTheta(std::string name,float t);
    void setWeight(std::string name,float weight);
    void setVelocity(std::string name,float lin,float vel,bool forced = true);
    void setMaxAcceleration(std::string name,float lin,float vel);
    void setMinAcceleration(std::string name,float lin,float vel);


    std::optional<std::vector<std::tuple<float, float>>> getShape(std::string name);
    std::optional<std::tuple<float, float>> getPosition(std::string name);
    float                getTheta(std::string name);
    float                getWeight(std::string name);
    std::optional<std::tuple<float, float>> getVelocity(std::string name);
    std::optional<std::tuple<float, float>> getMaxAcceleration(std::string name);
    std::optional<std::tuple<float, float>> getMinAcceleration(std::string name);
    bool                 isCollided(std::string name);                





protected:
     // Computing method
    virtual void process();
    bool collide(std::string name,PhysicsObject  * main, std::vector<std::string> ban_list);
    void move(PhysicsObject& p);



protected:

private:



    Polygon m_map;
    std::map<std::string,PhysicsObject> m_objects;




};

#endif // _PHYSICS_MOTOR_H_

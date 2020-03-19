#ifndef _PHYSICSUTILS_H_
#define _PHYSICSUTILS_H_

#include <cmath>
#include <vector>
#include <tuple>
#define MAX_POLYGONE_LENGTH 64




typedef struct {
    std::tuple<float, float> to_python(){
        return std::make_tuple(linear,angular);
    };
    

    float linear;
    float angular;
    } Velocity;

typedef Velocity Acceleration;

//struct point;

typedef struct vec{
    float x;
    float y;
    float z;
    float operator*(vec &c)
    {
        return (x*c.x+y*c.y);
    };
    vec operator^(vec &c)
    {
        vec result = {0.,0.,0.};
        result.z = x*c.y-y*c.x;
        result.y = z*c.x-x*c.z;
        result.x = y*c.z-z*c.y;
       return result;
    };
    bool isNULL(){
        return (x==0 && y==0);
    };

    float norm(){
        return (std::sqrt(x*x+y*y+z*z));
    };
} Vector;



typedef struct point{
    std::tuple<float, float> to_python(){
        return(std::make_tuple(x,y));
    };
    void operator+=(Vector const& v){
        x+=v.x;
        y+=v.y;

    };
    void operator-=(Vector const& v){
        x-=v.x;
        y-=v.y;

    };

    float x;
    float y;
    } Point;

typedef struct {
    std::vector<std::tuple<float, float>> to_python(){
        std::vector<std::tuple<float, float>> result;
        int i;
        for(i=0;i<length;i++){
            result.push_back(list[i].to_python());
        }
    return(result);
    };

    void from_python(std::vector<std::tuple<float, float>> poly){
        int i;
        length = poly.size(); 
        for(i = 0;i<length;i++){
            list[i].x = std::get<0>(poly[i]);
            list[i].y = std::get<1>(poly[i]);
        }
    };

    int length;
    Point list[MAX_POLYGONE_LENGTH];
    } Polygon;

#endif //_PhysicsUtils_H_

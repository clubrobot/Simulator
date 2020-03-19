#ifndef _PERIODICPROCESS_H_
#define _PERIODICPROCESS_H_

#include <iostream>
#include <thread>
#include <chrono>
#include <mutex> 

class PeriodicProcess
{
public:
    PeriodicProcess(int t) : m_timestep(t), m_enable(false){}
    PeriodicProcess(const PeriodicProcess& var);
    virtual ~PeriodicProcess(){ stop();}
    static void run(PeriodicProcess * parent);
	int getTimestep() const {return m_timestep;}
    void setTimestep(int timestep){m_timestep = timestep;}
    bool isEnabled() const {return m_enable;}
    void start();
    void stop();

protected:
	virtual void process() = 0;
	virtual void onProcessEnabling(){}
	virtual void onProcessDisabling(){}
    std::mutex m_mtx;
    int m_timestep;

private:

    bool m_enable;
    std::thread *m_soul;
};



#endif //_PERIODICPROCESS_H_

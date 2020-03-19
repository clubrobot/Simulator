#include "PeriodicProcess.h"

//Can"t do proper copy
PeriodicProcess::PeriodicProcess(const PeriodicProcess& var){
    m_timestep = var.m_timestep;
    m_enable   = var.m_enable;
}


void PeriodicProcess::run(PeriodicProcess * parent){
    while(parent->m_enable){
        parent->m_mtx.lock();
        parent->process();
        parent->m_mtx.unlock();
        std::this_thread::sleep_for(std::chrono::milliseconds(parent->m_timestep));
    }
    parent->m_enable=false;
}


void PeriodicProcess::start(){
    onProcessEnabling();
    m_enable = true;
    m_soul   = new std::thread(run, this);
}

void PeriodicProcess::stop(){
    m_enable = false;
    (*m_soul).join();
	delete (m_soul);
    onProcessDisabling();
}

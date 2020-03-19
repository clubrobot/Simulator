#ifndef _FUNCTION_PYTHON_H_
#define _FUNCTION_PYTHON_H_

#include <boost/python.hpp>

class FunctionPython {

public:
    FunctionPython(PyObject *callable) : m_function(callable) {}
    FunctionPython(){}
    void execute();
    void setFunction(PyObject *callable){ m_function=callable;}
    
private:

PyObject  *m_function;

};

#endif // _FUNCTION_PYTHON_H_



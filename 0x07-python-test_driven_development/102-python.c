#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Invalid Python string\n");
        return;
    }

    PyObject *str = PyUnicode_AsUTF8String(p);
    if (str) {
        char *str_data = PyBytes_AsString(str);
        if (str_data) {
            printf("String: %s\n", str_data);
        }
        Py_XDECREF(str);
    }
}

int main(int argc, char *argv[]) {
    // Initialize Python
    Py_Initialize();

    // Create a Python string
    PyObject *python_string = PyUnicode_DecodeUTF8("Hello, Python!", strlen("Hello, Python!"), "strict");

    // Print the Python string
    print_python_string(python_string);

    // Cleanup and finalize Python
    Py_DECREF(python_string);
    Py_Finalize();

    return 0;
}

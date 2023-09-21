#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints info about a Python list object
 * @p: pointer to PyObject
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(P))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	PyObject *allocated = PyObject_GetAttrString(p, "allocated");
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", PyLong_AsLong(allocated));

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

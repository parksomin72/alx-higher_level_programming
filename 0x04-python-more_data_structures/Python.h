#ifndef PYTHON_H
#define PYTHON_H

typedef struct _object {
struct _typeobject *ob_type;
} PyObject;

typedef struct {
PyObject ob_base;
Py_ssize_t ob_size;
char ob_bytes[1];
} PyBytesObject;

typedef struct {
PyObject_VAR_HEAD
PyObject *ob_item[1];
} PyListObject;

typedef struct {
const char *tp_name;
} PyTypeObject;

#define PyBytes_Check(obj)  (Py_TYPE(obj) == &PyBytes_Type)
#define PyList_Check(obj)   (Py_TYPE(obj) == &PyList_Type)

#define Py_TYPE(obj)        (((PyObject*)(obj))->ob_type)
#define PyBytes_Size(obj)   (((PyBytesObject*)(obj))->ob_size)
#define PyBytes_AsString(obj) (((PyBytesObject*)(obj))->ob_bytes)
#define PyList_Size(obj)    (((PyListObject*)(obj))->ob_base.ob_size)
#define PyList_GetItem(obj, index) (((PyListObject*)(obj))->ob_item[index])

extern PyTypeObject PyBytes_Type;
extern PyTypeObject PyList_Type;

#endif /* PYTHON_H */

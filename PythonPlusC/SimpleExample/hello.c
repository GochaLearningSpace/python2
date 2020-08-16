#include <Python.h>

static PyObject* helloworld(PyObject* self) {
	return Py_BuildValue("s", "#Modified Hello , ths is Python extensions written in hello.c i!!");
}

static char helloworld_docs[] =
	"helloworld() : Any message you want to put here !!\n";

static PyMethodDef helloworld_funcs[] = {
	{"helloworld", (PyCFunction)helloworld,
		METH_NOARGS, helloworld_docs}, {NULL}
};

void inithelloworld (void) {
	Py_InitModule3("helloworld" , helloworld_funcs, "Extension module example ! ");
//	Py_InitModule2("helloworld" , helloworld_funcs, "Extension module example ! ");
}


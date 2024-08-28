import CppHeaderParser

from pybind11_autogen.doxygen import wrap_doxygen


def wrap_variable(variable):
    return f'm.attr("{variable["name"]}") = py::cast({variable["name"]});' # , {wrap_doxygen(variable.get("doxygen", ""))}

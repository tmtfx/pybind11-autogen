import CppHeaderParser

from pybind11_autogen.doxygen import wrap_doxygen
from pybind11_autogen.variable import wrap_variable


def wrap_enum(enum):
    try:
        code = [
            f'py::enum_<{enum["name"]}>(m, "{enum["name"]}", {wrap_doxygen(enum.get("doxygen", ""))})']
        for value in enum["values"]:
            code.append(
                f'.value("{value["name"]}", {enum["name"]}::{value["name"]}, {wrap_doxygen(value.get("doxygen", ""))})')
        code.append(".export_values();")
    except KeyError:
        code=[]
        for value in enum["values"]:
            code.append(wrap_variable(value))
    return "\n".join(code)

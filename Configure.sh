
#!/bin/bash

PythonFile_01="./CreateParam.py"
PythonParam_01="Param_01"
PythonParam_02="Param_02"
PythonParam_03="Param_03"
PythonParam_04="Param_04"


PythonFile_02="./CreateFile.py"
PythonParam_11=true

test=python ${PythonFile_01} ${PythonParam_01} ${PythonParam_02} ${PythonParam_03} ${PythonParam_04}

test=python ${PythonFile_02} ${PythonParam_11}

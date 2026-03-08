cmake_minimum_required(VERSION 3.0)
project(PipPrefixWrap LANGUAGES NONE)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

execute_process(
  COMMAND ${Python3_EXECUTABLE} -c "from distutils.sysconfig import get_python_lib; from os.path import relpath; print(relpath(get_python_lib(1,prefix='${CMAKE_INSTALL_PREFIX}'),'${CMAKE_INSTALL_PREFIX}'))"
  OUTPUT_VARIABLE PYTHON3_INSTALL_DIR OUTPUT_STRIP_TRAILING_WHITESPACE
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")

install(DIRECTORY pip DESTINATION ${PYTHON3_INSTALL_DIR})
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/dist-info/METADATA" "${CMAKE_CURRENT_SOURCE_DIR}/dist-info/top_level.txt" DESTINATION ${PYTHON3_INSTALL_DIR}/pip_prefix_wrap.dist-info/)

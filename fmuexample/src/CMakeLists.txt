
set(headers
        cppfmu/cppfmu_cs.hpp
        cppfmu/cppfmu_common.hpp

        fmi/fmi2Functions.h
        fmi/fmi2FunctionTypes.h
        fmi/fmi2TypesPlatform.h

        Modules/DI8.py
        Modules/DO8.py
        Modules/MVKLEDConfig.py
        Modules/QualifierDI8.py
        Modules/QualifierDO8.py
        )

set(sources
        cppfmu/cppfmu_cs.cpp
        cppfmu/fmi_functions.cpp
        Modules/DI8.py
        Modules/DO8.py
        Modules/MVKLEDConfig.py
        Modules/QualifierDI8.py
        Modules/QualifierDO8.py
        )

add_library(fmuexample ${sources} ${headers})
target_compile_features(fmuexample PUBLIC "cxx_std_17")

target_include_directories(fmuexample
        PRIVATE
        "${Python3_INCLUDE_DIRS}"
        "${CMAKE_CURRENT_SOURCE_DIR}"
        )

if (WIN32)
  target_link_libraries(fmuexample PRIVATE ${Python3_LIBRARIES})
elseif (APPLE)
  set_target_properties(fmuexample PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
endif ()
# and on linux, dont link!

if (WIN32)
  set_target_properties(fmuexample
          PROPERTIES
          RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_SOURCE_DIR}/../resources/binaries/${TARGET_PLATFORM}"
          )
else ()
  set_target_properties(fmuexample
          PROPERTIES
          LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/../resources/binaries/${TARGET_PLATFORM}"
          )
endif ()
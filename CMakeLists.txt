cmake_minimum_required(VERSION 2.8.5)
project(blog)

# First, define all the options.
option(MATHJAX
    "Use MathJax for HTML Doxygen output (disabled by default)." OFF)

# Include modules in the CMake directory.
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMake")

# Make a target to generate the documentation.  If Doxygen isn't installed, then
# I guess this option will just be unavailable.
find_package(Doxygen)
if (DOXYGEN_FOUND)
  if (MATHJAX)
    find_package(MathJax)
    if (NOT MATHJAX_FOUND)
      message(STATUS "Using MathJax at the MathJax Content Delivery Network. "
          "Be careful, formulas will not be shown without the internet.")
    endif ()
  endif ()
  # Preprocess the Doxyfile.  This is done before 'make doc'.
  add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/Doxyfile
      PRE_BUILD
      COMMAND ${CMAKE_COMMAND}
          -D DESTDIR="${CMAKE_BINARY_DIR}"
          -D MATHJAX="${MATHJAX}"
          -D MATHJAX_FOUND="${MATHJAX_FOUND}"
          -D MATHJAX_PATH="${MATHJAX_PATH}"
          -P "${CMAKE_CURRENT_SOURCE_DIR}/CMake/GenerateDoxyfile.cmake"
      WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
      DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile"
      COMMENT "Creating Doxyfile to generate Doxygen documentation"
  )

  # Generate documentation.
  add_custom_target(doc
      COMMAND "${DOXYGEN_EXECUTABLE}" "${CMAKE_BINARY_DIR}/Doxyfile"
      DEPENDS "${CMAKE_BINARY_DIR}/Doxyfile"
      WORKING_DIRECTORY "${CMAKE_BINARY_DIR}"
      COMMENT "Generating API documentation with Doxygen"
  )

  install(DIRECTORY ${CMAKE_BINARY_DIR}/doc/html
      DESTINATION share/doc/mlpack
      COMPONENT doc
      OPTIONAL
  )
endif ()

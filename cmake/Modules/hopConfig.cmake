INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_HOP hop)

FIND_PATH(
    HOP_INCLUDE_DIRS
    NAMES hop/api.h
    HINTS $ENV{HOP_DIR}/include
        ${PC_HOP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    HOP_LIBRARIES
    NAMES gnuradio-hop
    HINTS $ENV{HOP_DIR}/lib
        ${PC_HOP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(HOP DEFAULT_MSG HOP_LIBRARIES HOP_INCLUDE_DIRS)
MARK_AS_ADVANCED(HOP_LIBRARIES HOP_INCLUDE_DIRS)


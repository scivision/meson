## CMake Components

CMake `find_package( COMPONENTS ...) is necessary for some packages in CMake, and is
enabled in Meson by `dependency(cmake_components:)`

Some of the same packages require not having Meson prefill the CMake cache, which is
controlled by `dependency(cmake_full_find: true)` to have CMake determine the full cache.
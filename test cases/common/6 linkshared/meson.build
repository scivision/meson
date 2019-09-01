project('shared library linking test', 'c')

if add_languages('cpp', required: false)
  cpp = meson.get_compiler('cpp')
else
  error('MESON_SKIP_TEST: No C++ compiler available.')
endif

lib = shared_library('mylib',
 'libfile.c' # Split to different lines before and after the comma to test parser.
 , install : false) # Don't install libraries in common tests; the path is platform-specific
exe = executable('prog', 'main.c', link_with : lib, install : true)

test('runtest', exe)

cpplib = shared_library('mycpplib', 'cpplib.cpp')
cppexe = executable('cppprog', 'cppmain.cpp', link_with : cpplib)
test('cpptest', cppexe)

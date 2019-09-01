project('C++ and FORTRAN', 'fortran')

if add_languages('cpp', required : false)
  cpp = meson.get_compiler('cpp')
else
  error('MESON_SKIP_TEST: No C++ compiler available.')
endif

fc = meson.get_compiler('fortran')

if cpp.get_id() == 'clang'
  error('MESON_SKIP_TEST Clang C++ does not find -lgfortran for some reason.')
elif build_machine.system() == 'windows' and cpp.get_id() != fc.get_id()
  error('MESON_SKIP_TEST mixing gfortran with non-GNU C++ does not work.')
endif

link_with = []
if fc.get_id() == 'intel'
  link_with += fc.find_library('ifport')
endif

e = executable(
  'cppfort',
  ['main.cpp', 'fortran.f'],
  dependencies : link_with,
)

test('C++ FORTRAN', e)

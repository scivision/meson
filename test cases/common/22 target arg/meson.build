project('local arg test', 'c')

if add_languages('cpp', required: false)
  cpp = meson.get_compiler('cpp')
else
  error('MESON_SKIP_TEST: No C++ compiler available.')
endif

exe1 = executable('prog', 'prog.cc', 'func.c', \
c_args   : '-DCTHING', \
cpp_args : '-DCPPTHING')
exe2 = executable('prog2', 'prog2.cc', 'func2.c')

test('prog1', exe1)
test('prog2', exe2)

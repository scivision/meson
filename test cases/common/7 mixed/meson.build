project('mixed C and C++', 'c')

if add_languages('cpp', required: false)
  cpp = meson.get_compiler('cpp')
else
  error('MESON_SKIP_TEST: No C++ compiler available.')
endif

exe = executable('prog', 'main.cc', 'func.c')
test('mixtest', exe)

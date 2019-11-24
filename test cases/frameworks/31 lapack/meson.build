project('lapack_test', 'c')

cc = meson.get_compiler('c')

# --- C tests
lapack_c = dependency('lapack', language: 'c', required : false)
if not lapack_c.found()
  error('MESON_SKIP_TEST: LAPACK C library not found, skipping tests.')
endif
# FIXME: this is a workaround for Intel Compiler icl bug: https://www.scivision.dev/intel-compiler-windows-bug-workaround
if cc.get_id() == 'intel-cl' and not cc.compiles(files('main.c'), dependencies: lapack_c, name: 'ICL MSVC')
  add_project_arguments('/TP', language: 'c')
  message('applying workaround for Intel ICL bug with MSVC: https://www.scivision.dev/intel-compiler-windows-bug-workaround')
endif
if cc.get_id() == 'msvc' and not cc.links(files('main.c'), dependencies: lapack_c, name: 'MSVC MKL')
  error('MESON_SKIP_TEST: Lapack on MSVC can be done with Intel MKL')
endif
exec = executable('exec', 'main.c', dependencies : lapack_c)

test('LAPACK C', exec, timeout: 10)

# --- Fortran tests
if add_languages('fortran')
  lapack_f = dependency('lapack', language: 'fortran', required : false)
  if not lapack_f.found()
    error('MESON_SKIP_TEST: LAPACK C library not found, skipping tests.')
  endif

  exef = executable('exef', 'main.f90', dependencies : lapack_f)
  test('LAPACK Fortran', exef, timeout: 10)
endif

# Check we can apply a version constraint
if lapack_c.version() != 'unknown'
  dependency('lapack', version: '>=@0@'.format(lapack_c.version()))
endif
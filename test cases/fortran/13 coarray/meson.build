project('Fortran coarray', 'fortran',
  meson_version: '>=0.50')

fc = meson.get_compiler('fortran')

if ['pgi', 'flang'].contains(fc.get_id())
  error('MESON_SKIP_TEST: At least through PGI 19.10 and Flang 7.1 do not support Fortran Coarrays.')
endif

# coarray is required because single-image fallback is an intrinsic feature

foreach depmeth : ['pkg-config', 'cmake']

  coarray = dependency('coarray', method: depmeth, required: false)
  if not coarray.found()
    continue
  endif

  # check coarray, because user might not have all the library stack installed correctly
  # for example, conflicting library/compiler versions on PATH
  # this has to invoke a run of "sync all" to verify the MPI stack is functioning,
  # particularly for dynamic linking

  if fc.run('sync all; end', dependencies: coarray, name: 'Coarray link & run').returncode() != 0
    error(depmeth + ' coarray stack (including MPI) did not link correctly so that a simple test could run.')
  endif

endforeach

if not coarray.found()
  error('did not find coarrays')
endif

exe = executable('hello', 'main.f90',
  dependencies : coarray)

# cafrun is optional but would almost always be used with coarrays
if fc.get_id() == 'gcc'
  cafrun = find_program('cafrun', required: false)
else
  cafrun = disabler()
endif
if cafrun.found()
  # "oversubscribing" is OK for simple test (more processes than CPU cores)
  test('Coarray hello world', cafrun, args: ['-np', '4', exe], timeout: 10)
else
  # intel doesn't need cafrun
  test('Coarray hello world', exe, timeout: 10)
endif

project('global arg test', 'c')

cpp_ok = add_languages('cpp', required: false)
if cpp_ok
  cpp = meson.get_compiler('cpp')
endif

add_global_arguments('-DMYTHING', language : 'c', native : true)
add_global_arguments('-DMYTHING', language : 'c', native : false)
if cpp_ok
  add_global_arguments('-DMYCPPTHING', language : 'cpp', native : true)
  add_global_arguments('-DMYCPPTHING', language : 'cpp', native : false)
endif
add_global_arguments('-DGLOBAL_BUILD', language : 'c', native : true)
add_global_arguments('-DGLOBAL_HOST', language : 'c', native : false)

build_c_args = ['-DARG_BUILD']
c_args = ['-DARG_HOST']

add_global_arguments('-DMYCANDCPPTHING', language: 'c', native: true)
add_global_arguments('-DMYCANDCPPTHING', language: 'c', native: false)
if cpp_ok
  add_global_arguments('-DMYCANDCPPTHING', language: 'cpp', native: true)
  add_global_arguments('-DMYCANDCPPTHING', language: 'cpp', native: false)
endif

exe1 = executable('prog1', 'prog.c', c_args : build_c_args, native : true)
exe2 = executable('prog2', 'prog.c', c_args : c_args, native : false)

test('prog1', exe1)
test('prog2', exe2)

if cpp_ok
  exe3 = executable('prog3', 'prog.cc')
  test('prog3', exe3)
endif
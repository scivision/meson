project('project options tester', 'c',
  version : '2.3.4',
  license : 'mylicense')

cpp_ok = add_languages('cpp', required: false)

add_global_arguments('-DGLOBAL_ARGUMENT', language: 'c')
add_project_arguments('-DPROJECT_OPTION', language: 'c')
if cpp_ok
  add_project_arguments('-DPROJECT_OPTION_CPP', language: 'cpp')
  add_project_arguments('-DPROJECT_OPTION_C_CPP', language: ['c', 'cpp'])
endif

sub = subproject('subexe', version : '1.0.0')

add_project_arguments('-DPROJECT_OPTION_1', language: 'c')

e = executable('exe', 'exe.c')
test('exetest', e)

if cpp_ok
  ep = executable('execpp', 'exe.cpp')
  test('execpptest', ep)
endif
project('add language')

assert(add_languages('c'), 'add_languages() returned false on success')

test('C', executable('cprog', 'prog.c'))

assert(not add_languages('klingon', required : false), 'Add_languages returned true on failure.')

if add_languages('cpp', required: false)
  test('C++', executable('cppprog', 'prog.cc'))
endif
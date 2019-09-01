project('selfbuilt custom')

# Build an exe and use it in a custom target
# whose output is used to build a different exe.

if not add_languages('cpp', required: false)
  error('MESON_SKIP_TEST: C++ compiler not available')
endif

tool = executable('tool', 'tool.cpp', native : true)

hfile = custom_target('datah',
  output : 'data.h',
  input : 'data.dat',
  command : [tool, '@INPUT@', '@OUTPUT@'],
)

main = executable('mainprog', 'mainprog.cpp', hfile)

test('maintest', main)

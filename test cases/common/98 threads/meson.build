project('threads', 'c',
  default_options : ['cpp_std=c++11'])

threaddep = dependency('threads')

if add_languages('cpp', required: false)
  test('cppthreadtest',
    executable('cppthreadprog', 'threadprog.cpp',
      dependencies : threaddep
    )
  )
endif

test('cthreadtest',
  executable('cthreadprog', 'threadprog.c',
    dependencies : threaddep
  )
)

project('has type', 'c')

compilers = [meson.get_compiler('c')]

if add_languages('cpp', required: false)
  compilers += meson.get_compiler('cpp')
endif

foreach cc : compilers
  if not cc.has_type('time_t', prefix : '#include<time.h>')
    error('Did not detect type that exists.')
  endif

  if cc.has_type('no_time_t', prefix : '#include<time.h>')
    error('Not existing type found.')
  endif
endforeach

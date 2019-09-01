# Must have two languages here to exercise linker language
# selection bug
project('all sources generated', 'c')

if not add_languages('cpp', required: false)
  error('MESON_SKIP_TEST: C++ compiler not available')
endif

comp = find_program('converter.py')

g = generator(comp,
  output : '@BASENAME@',
  arguments : ['@INPUT@', '@OUTPUT@'])

c = g.process('foobar.cpp.in')

prog = executable('genexe', c)

c2 = custom_target('c2gen',
  output : '@BASENAME@',
  input : 'foobar.cpp.in',
  command : [comp, '@INPUT@', '@OUTPUT@'])

prog2 = executable('genexe2', c2)

project('stringdef', 'c')


if host_machine.system() == 'windows' and meson.get_compiler('c').get_id() == 'pgi'
  error('MESON_SKIP_TEST: PGI does not have this character set')
endif

test('stringdef', executable('stringdef', 'stringdef.c', c_args : '-DFOO="bar"'))

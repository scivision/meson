project('pch test', 'c',
  meson_version: '>= 0.46.0')

if add_languages('cpp', required: false)
  cpp = meson.get_compiler('cpp')
else
  error('MESON_SKIP_TEST: No C++ compiler available.')
endif

cc = meson.get_compiler('c')
cc_id = cc.get_id()

if cc_id == 'pgi'
  error('MESON_SKIP_TEST: PGI compiler does support PCH, however, PGI cannot tolerate spaces in the --pch_dir path and Meson run_project_tests.py uses spaces in temporary build path names. If this test is run individually with no spaces in build path, it will pass.')
endif

subdir('c')
subdir('cpp')
subdir('generated')
subdir('userDefined')
subdir('withIncludeDirectories')

if meson.backend() == 'xcode'
  warning('Xcode backend only supports one precompiled header per target. Skipping "mixed" which has various precompiled headers.')
else
  subdir('mixed')
endif

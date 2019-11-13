# Copyright 2019 The meson development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Abstractions for the PGI family of compilers."""

import typing
import os
from pathlib import Path

from ..compilers import clike_debug_args, Compiler

if typing.TYPE_CHECKING:
    from ..fortran import FortranCompiler
    _Base1 = FortranCompiler
    _Base2 = Compiler
else:
    _Base1 = _Base2 = object

clike_optimization_args = {'0': [],
                           'g': [],
                           '1': ['-O1'],
                           '2': ['-O2'],
                           '3': ['-O3'],
                           's': ['-Os'],
                           }  # typing.Dict[typing.List[str]]

pgi_buildtype_args = {
    'plain': [],
    'debug': [],
    'debugoptimized': [],
    'release': [],
    'minsize': [],
    'custom': [],
}  # type: typing.Dict[str, typing.List[str]]


class PGICompiler(_Base1, _Base2):
    def __init__(self):
        self.base_options = ['b_pch']
        self.id = 'pgi'

        default_warn_args = ['-Minform=inform']
        self.warn_args = {'0': [],
                          '1': default_warn_args,
                          '2': default_warn_args,
                          '3': default_warn_args}

    def get_module_incdir_args(self) -> typing.Tuple[str]:
        return ('-module', )

    def get_no_warn_args(self) -> typing.List[str]:
        return ['-silent']

    def gen_import_library_args(self, implibname: str) -> typing.List[str]:
        return []

    def get_pic_args(self) -> typing.List[str]:
        # PGI -fPIC is Linux only.
        if self.info.is_linux():
            return ['-fPIC']
        return []

    def openmp_flags(self) -> typing.List[str]:
        return ['-mp']

    def get_buildtype_args(self, buildtype: str) -> typing.List[str]:
        return pgi_buildtype_args[buildtype]

    @staticmethod
    def get_optimization_args(optimization_level: str) -> typing.List[str]:
        args: typing.List[str] = clike_optimization_args[optimization_level]
        return args

    @staticmethod
    def get_debug_args(is_debug: bool) -> typing.List[str]:
        return clike_debug_args[is_debug]

    def compute_parameters_with_absolute_paths(self, parameter_list: typing.List[str], build_dir: str) -> typing.List[str]:
        for idx, i in enumerate(parameter_list):
            if i[:2] == '-I' or i[:2] == '-L':
                parameter_list[idx] = i[:2] + os.path.normpath(os.path.join(build_dir, i[2:]))
        return parameter_list

    def get_dependency_gen_args(self, outtarget: str, outfile: str) -> typing.List[str]:
        return []

    def get_always_args(self) -> typing.List[str]:
        return []

    def get_pch_suffix(self) -> str:
        # PGI defaults to .pch suffix for PCH on Linux and Windows with --pch option
        return 'pch'

    def get_pch_use_args(self, pch_dir: str, header: str) -> typing.List[str]:
        # PGI supports PCH for C++ only.
        hdr = Path(pch_dir).resolve().parent / header
        if self.language == 'cpp':
            return ['--pch',
                    '--pch_dir', str(hdr.parent),
                    '-I{}'.format(hdr.parent)]
        else:
            return []

    def thread_flags(self, env):
        # PGI cannot accept -pthread, it's already threaded
        return []

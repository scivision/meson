# Copyright 2013-2019 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
import os

from .base import (CMakeDependency, ExternalDependency, PkgConfigDependency)


class LapackDependency(ExternalDependency):

    def __init__(self, environment, kwargs):
        language = kwargs.get('language', 'c')
        super().__init__('lapack', environment, language, kwargs)
        kwargs['required'] = False
        kwargs['silent'] = True
        self.is_found = False
        self.static = kwargs.get('static', False)

        # 1. try pkg-config
        mklroot = None
        is_gcc = None
        if language == 'fortran':
            is_gcc = environment.detect_fortran_compiler(self.for_machine).get_id() == 'gcc'
        elif language == 'c':
            is_gcc = environment.detect_c_compiler(self.for_machine).get_id() == 'gcc'
        elif language == 'cpp':
            is_gcc = environment.detect_cpp_compiler(self.for_machine).get_id() == 'gcc'
        # Intel MKL works with non-Intel compilers too
        if 'MKLROOT' in os.environ:
            try:
                mklroot = Path(os.environ['MKLROOT']).resolve()
            except Exception:
                pass
            # MKL pkg-config is a start, but you have to add / change stuff
            # https://software.intel.com/en-us/articles/intel-math-kernel-library-intel-mkl-and-pkg-config-tool
            pkgconfig_files = ['mkl-static-lp64-iomp'] if self.static else ['mkl-dynamic-lp64-iomp']
        if mklroot is None:
            if language in (('cpp', 'c')):
                pkgconfig_files = ['lapacke']
            else:
                pkgconfig_files = ['lapack']

        # some pkg-config e.g. ubuntu don't chain up correctly, so append args
        for pkg in pkgconfig_files:
            pkgdep = PkgConfigDependency(pkg, environment, kwargs, language=self.language)
            if pkgdep.found():
                self.compile_args = pkgdep.get_compile_args()
                self.link_args = pkgdep.get_link_args()
                if mklroot is not None:
                    if is_gcc:
                        for i, a in enumerate(self.link_args):
                            if 'mkl_intel_lp64' in a:
                                self.link_args[i] = a.replace('intel', 'gf')
                                break

                self.version = pkgdep.get_version()
                if self.version == 'unknown' and mklroot is not None:
                    try:
                        v = (
                            mklroot.as_posix()
                            .split('compilers_and_libraries_')[1]
                            .split('/', 1)[0]
                        )
                        if v:
                            self.version = v
                    except IndexError:
                        pass
                self.is_found = True
                self.pcdep = pkgdep
                return

        # 2. try CMake
        cmakedep = CMakeDependency('Lapack', environment, kwargs)
        if cmakedep.found():
            self.compile_args = cmakedep.get_compile_args()
            self.link_args = cmakedep.get_link_args()
            self.version = cmakedep.get_version()
            self.is_found = True
            return

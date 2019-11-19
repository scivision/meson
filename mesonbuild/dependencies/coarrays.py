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

import functools

from .base import CMakeDependency, DependencyMethods, ExternalDependency, PkgConfigDependency


class CoarrayDependency(ExternalDependency):
    """
    Coarrays are a Fortran 2008 feature.

    Coarrays are sometimes implemented via external library (GCC+OpenCoarrays),
    while other compilers just build in support (Cray, IBM, Intel).
    Coarrays may be thought of as a high-level language abstraction of
    low-level MPI calls.
    """
    def __init__(self, environment, kwargs: dict):
        super().__init__('coarray', environment, 'fortran', kwargs)

    @classmethod
    def _factory(cls, environment, kwargs):
        methods = cls._process_method_kw(kwargs)
        candidates = []

        cid = environment.coredata.compilers.host['fortran'].id
        if cid == 'gcc':
            """ OpenCoarrays is the most commonly used method for Fortran Coarray with GCC """
            if DependencyMethods.PKGCONFIG in methods:
                candidates.append(functools.partial(PkgConfigDependency, 'caf-openmpi', environment, kwargs))
                candidates.append(functools.partial(PkgConfigDependency, 'caf', environment, kwargs))
            if DependencyMethods.CMAKE in methods:
                kwargs['modules'] = 'OpenCoarrays::caf_mpi'
                candidates.append(functools.partial(CMakeDependency, 'OpenCoarrays', environment, kwargs))
        else:
            kwargs['cid'] = cid
            candidates.append(functools.partial(CoarrayFlags, environment, kwargs))
        return candidates

    @staticmethod
    def get_methods():
        return [DependencyMethods.PKGCONFIG, DependencyMethods.CMAKE]


class CoarrayFlags(ExternalDependency):
    """ for compilers with intrinsic Coarray support, only flags or nothing needed """

    def __init__(self, environment, kwargs: dict):
        super().__init__('coarray', environment, 'fortran', kwargs)

        self.is_found = False
        cid = kwargs['cid']

        if cid == 'intel':
            """ Coarrays are built into Intel compilers, no external library needed """
            self.link_args = ['-coarray=shared']
            self.compile_args = self.link_args
            self.is_found = True
        elif cid == 'intel-cl':
            """ Coarrays are built into Intel compilers, no external library needed """
            self.compile_args = ['/Qcoarray:shared']
            self.is_found = True

    @staticmethod
    def get_methods():
        return [DependencyMethods.PKGCONFIG, DependencyMethods.CMAKE]

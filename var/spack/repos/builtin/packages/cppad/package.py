##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Cppad(CMakePackage):
    """A Package for Differentiation of C++ Algorithms."""

    homepage = "https://www.coin-or.org/CppAD/"
    url      = "http://www.coin-or.org/download/source/CppAD/cppad-20170114.gpl.tgz"

    version('20170114', '565a534dc813fa1289764222cd8c11ea')
    version('develop', git='https://github.com/coin-or/CppAD.git')

    def cmake_args(self):
        # This package does not obey CMAKE_INSTALL_PREFIX
        args = [
            "-Dcppad_prefix=%s" % (self.prefix),
            "-Dcmake_install_docdir=share/cppad/doc"
        ]
        return args

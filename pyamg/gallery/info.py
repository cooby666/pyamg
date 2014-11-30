"""Matrix Gallery for Multigrid Solvers

Functions
=========
    - poisson() : Poisson problem using Finite Differences
    - linear_elasticity() : Linear Elasticity using Finite Elements
    - stencil_grid() : General stencil generation from 1D, 2D, and 3D
    - diffusion_stencil_2d() : 2D rotated anisotropic FE/FD stencil
"""
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

postpone_import = 1

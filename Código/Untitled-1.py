"""
Rod phototransduction (rod disk) — reaction–diffusion model in radial 2D symmetry.

Equations (per area densities):
    ∂t G* = Dg ∇_r^2 G*  - kG G* + S(t) δ(r)                # transducin (active)
    ∂t E* = De ∇_r^2 E*  + k2 G* - kE (E* - E_basal)        # PDE (active)
    ∂t  C  = Dc ∇_r^2  C + α - β E* C                       # cGMP
    Boundary conditions:
    Neumann (no-flux) at r = R; symmetry at r = 0.
"""


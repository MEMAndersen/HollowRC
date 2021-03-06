# -*- coding: utf-8 -*-
"""
Class definition of a container for sectional forces

History log:
Version 0.1 - first working build

Author: Kenneth C. Kleissl
"""

class SectionForces:
    """
    A container for sectional forces by Kenneth C. Kleissl.

    Attributes:
        N:  Normal force (neg. = compression)
        My: Bending moment about the y-axis
        Mz: Bending moment about the z-axis
        Vy: Shear force in the y-axis
        Vz: Shear force in the z-axis
        T:  Torsional moment
    """
    # Class variables
    count = 0
    load_factor = 1.0
    fac_bending = load_factor
    fac_shear = load_factor

    def __init__(self, N, My, Mz, Vy=None, Vz=None, T=None):
        # Instance variables
        self.N = N * self.fac_bending
        self.My = My * self.fac_bending
        self.Mz = Mz * self.fac_bending

        if Vy:
            self.Vy = Vy * self.fac_shear
        else:
            self.Vy = Vy

        if Vz:
            self.Vz = Vz * self.fac_shear
        else:
            self.Vz = Vz

        if T:
            self.T = T * self.fac_shear
        else:
            self.T = T

        SectionForces.count += 1

    def set_load_factor(self, fac):
        self.load_factor = fac

    def print_str(self):
        string = 'N=' + str(self.N) + ', My=' + str(self.My) + ', Mz=' + str(self.Mz) \
                 + ', Vy=' + str(self.Vy) + ', Vz=' + str(self.Vz) + ', T=' + str(self.T)
        return string


# For when this script is excetuted on its own
if __name__ == '__main__':
    N = -20000
    My = 60000
    Mz = -10000
    Vy = 0
    Vz = 2000
    T = 0
    SF = SectionForces(N, My, Mz, Vy, Vz, T)
    print(SF.My)


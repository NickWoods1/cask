"""
Defines parameters class. Reads from parameters file, otherwise
specifies the default.
"""

class parameters(object):
        def __init__(self,*args,**kwargs):

            # Basis set
            self.cut_off_energy = kwargs.pop('cut_off_energy',300)

            # Exchange / Correlation
            self.xc_functional = kwargs.pop('xc_functional','lda')

            # Electronic minimisation
            self.scf_method  = kwargs.pop('mixing_method','pulay')
            self.scf_max_iter = kwargs.pop('scf_max_iter',100)
            self.scf_damping = kwargs.pop('scf_damping',0.8)
            self.scf_kerker = kwargs.pop('scf_kerker',1.5)
            self.scf_history_size = kwargs.pop('scf_history_size',10)

            # Cell
            self.cell = kwargs.pop('cell',[[3.0,0,0],[0,3.0,0],[0,0,3.0]])

            # Atomic species

            # Atomic positions

            # k-point spacing


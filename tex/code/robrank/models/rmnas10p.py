from . import rres18


class Model(rres18.Model):
    BACKBONE = 'rmnas10'
    is_advtrain_pnp = True

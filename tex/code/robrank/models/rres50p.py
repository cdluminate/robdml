from . import rres18


class Model(rres18.Model):
    BACKBONE = 'rres50'
    is_advtrain_pnp = True

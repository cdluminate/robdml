from . import rc2f2


class Model(rc2f2.Model):
    BACKBONE = 'rlenet'
    is_advtrain = True

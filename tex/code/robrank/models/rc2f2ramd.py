from . import rc2f2
from .. import utils


class Model(rc2f2.Model):
    is_advtrain_ramd = True

    def post_init_hook(self):
        utils.warn('reducing advtrain_pgditer to 7 or it will collapse')
        utils.warn('this warning is irrelevant to attack')
        self.config.advtrain_pgditer = 7

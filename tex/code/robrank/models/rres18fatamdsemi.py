from . import rres18
from ..defenses import freeat_common_post_init_hook


class Model(rres18.Model):
    is_freeat_amdsemi = True

    def post_init_hook(self):
        freeat_common_post_init_hook(self)

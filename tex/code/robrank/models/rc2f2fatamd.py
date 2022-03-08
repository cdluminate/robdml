from . import rc2f2
from ..defenses import freeat_common_post_init_hook


class Model(rc2f2.Model):
    is_freeat_amd = True

    def post_init_hook(self):
        freeat_common_post_init_hook(self)

from .template_rank import MetricTemplate28


class Model(MetricTemplate28):
    is_advtrain = False
    do_svd = False
    BACKBONE = 'rc2f2'

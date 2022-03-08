from .template_rank import MetricTemplate224


class Model(MetricTemplate224):
    BACKBONE = 'rres18'
    is_advtrain = False
    do_svd = False

from .template_rank import MetricTemplate224


class Model(MetricTemplate224):
    BACKBONE = 'ribn'
    is_inceptionbn = True
    is_advtrain = False
    do_svd = False

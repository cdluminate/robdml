from .template_rank import MetricTemplate224


class Model(MetricTemplate224):
    BACKBONE = 'ribn'
    is_inceptionbn = True
    is_advtrain_est = True
    do_svd = False

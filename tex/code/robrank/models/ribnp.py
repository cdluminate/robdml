from .template_rank import MetricTemplate224


class Model(MetricTemplate224):
    BACKBONE = 'ribn'
    is_inceptionbn = True
    is_advtrain_pnp = True
    do_svd = False

from .template_rank import MetricTemplate224


class Model(MetricTemplate224):
    BACKBONE = 'reffb0'
    is_advtrain_pnp = True

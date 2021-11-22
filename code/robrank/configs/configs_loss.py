
from dataclasses import dataclass

#########################
# Loss Function Configs #
#########################


@dataclass
class contrastive:
    margin_cosine: float = 1.0
    margin_euclidean: float = 1.0


@dataclass
class triplet:
    '''
    Setting margin_cosine: float = 0.8 can further improve the model
    robustness with EST or ACT defense. But here we don't enable that
    by default. Note, we also use margin_cosine for euclidean distance
    on (unit) hypersphere, which is symbolized as the "N" metric.
    '''
    margin_cosine: float = 0.2
    margin_euclidean: float = 1.0


@dataclass
class quadruplet:
    margin2_cosine: float = 0.1
    margin2_euclidean: float = 0.5


@dataclass
class glift:
    margin_cosine: float = 0.2
    margin_euclidean: float = 1.0
    l2_weight: float = 5e-3


@dataclass
class npair:
    l2_weight: float = 5e-3


@dataclass
class margin:
    beta: float = 0.6  # [locked, ICML20]
    lr_beta: float = 5e-4  # [locked, ICML20]
    margin: float = 0.2


@dataclass
class multisim:
    pos_weight: float = 2  # [locked, ICML20]
    neg_weight: float = 40  # [locked]
    margin: float = 0.1  # [locked]
    threshold: float = 0.5  # [locked]


@dataclass
class snr:
    margin: float = 0.2  # [locked, ICML20]
    reg_lambda: float = 0.005  # [locked, ICML20]

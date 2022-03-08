
# pylint: disable=unused-argument,useless-super-delegation
from dataclasses import dataclass
import multiprocessing as mp
import re


#################
# Model Configs #
#################


@dataclass
class __hybrid:
    allowed_losses: tuple = (
        'contrast',  # default setting of contrastive loss
        'contrastiveC', 'contrastiveE',
        'pcontrastC', 'pcontrastE', 'pcontrastN',
        'pdcontrastN', 'pDcontrastN',
        'ctripletC', 'ctripletE', 'ctripletN',
        'ptripletC', 'ptripletE', 'ptripletN',
        'pmtripletC', 'pmtripletE', 'pmtripletN',
        'phtripletC', 'phtripletE', 'phtripletN',
        'pstripletC', 'pstripletE', 'pstripletN',
        'pdtripletN', 'pDtripletN',
        'ttripletC', 'ttripletE', 'ttripletN',
        'pgliftE',  # only E makes sense for pglift
        'pmarginC', 'pmarginE', 'pmarginN',
        'pdmarginN', 'pDmarginN',
        'pnpairE',  # only E makes sense for pnpair, presumably
        'pquadC', 'pquadE', 'pquadN', 'pdquadN',
        'prhomC', 'prhomE', 'prhomN', 'pdrhomN',
        'pmsC', 'pmsN',
        # extra.py: borrowed functions
        'pstripN',
        'pangularN',
        'pcontN',
        'pncaN',
    )


@dataclass
class __hybrid_model_28x28(__hybrid):
    allowed_datasets: tuple = ('mnist', 'fashion')
    advtrain_eps: float = 0.3


@dataclass
class __hybrid_model_224x224(__hybrid):
    allowed_datasets: tuple = ('sop', 'cub', 'cars')
    advtrain_eps: float = 16. / 255.

    def __init__(self, dataset, loss):
        if dataset == 'cub':
            self.num_class = 100
        elif dataset == 'cars':
            self.num_class = 98
        elif dataset == 'sop':
            self.num_class = 11316


@dataclass
class __hybrid_model_224x224_icml(__hybrid_model_224x224):
    def __init__(self, dataset, loss):
        super().__init__(dataset, loss)
        if dataset == 'sop':
            self.maxepoch = 100
        self.validate_every = {'sop': 5, 'cub': 5, 'cars': 5}[dataset]
        if re.match(r'c.+', loss):
            self.batchsize = 112  # [lock]
        elif re.match(r'p.+', loss):
            self.batchsize = 56  # [lock]
            self.maxepoch //= 2
        elif re.match(r't.+', loss):
            self.batchsize = 37  # [lock]
            self.maxepoch //= 3


@dataclass
class hc2f2(__hybrid_model_28x28):
    maxepoch: int = 16  # eph-with-cls-batch, equals 2 * eph-with-spc2-batch
    loader_num_workers: int = min(8, mp.cpu_count())
    batchsize: int = 128
    lr: float = 1e-3
    weight_decay: float = 1e-7
    validate_every: int = 1
    valbatchsize: int = 128
    num_class: int = 10

    def __init__(self, dataset, loss):
        if re.match(r'p.+', loss):
            self.maxepoch //= 2
        if re.match(r't.+', loss):
            self.maxepoch //= 3


@dataclass
class hres18(__hybrid_model_224x224_icml):
    maxepoch: int = 150
    loader_num_workers: int = min(8, mp.cpu_count())
    lr: float = 1e-5  # [lock]
    weight_decay: float = 4e-4  # [lock] 2002.08473
    embedding_dim: int = 512
    freeze_bn: bool = True
    valbatchsize: int = 112

    def __init__(self, dataset, loss):
        super().__init__(dataset, loss)


@dataclass
class hres50(__hybrid_model_224x224_icml):
    maxepoch: int = 150
    loader_num_workers: int = min(8, mp.cpu_count())
    lr: float = 1e-5  # [lock]
    weight_decay: float = 4e-4  # [lock] 2002.08473
    embedding_dim: int = 512
    freeze_bn: bool = True
    valbatchsize: int = 112

    def __init__(self, dataset, loss):
        super().__init__(dataset, loss)


@dataclass
class hmnas(__hybrid_model_224x224_icml):
    maxepoch: int = 150
    loader_num_workers: int = min(8, mp.cpu_count())
    lr: float = 1e-5  # [lock]
    weight_decay: float = 4e-4  # [lock] 2002.08473
    embedding_dim: int = 512
    freeze_bn: bool = True
    valbatchsize: int = 112

    def __init__(self, dataset, loss):
        super().__init__(dataset, loss)

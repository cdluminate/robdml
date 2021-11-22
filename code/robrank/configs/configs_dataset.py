
import os
from dataclasses import dataclass

###################
# Dataset Configs #
###################


@dataclass
class mnist:
    path: str = os.path.expanduser('~/.torch')
    num_class: int = 10


@dataclass
class fashion:
    path: str = os.path.expanduser('~/.torch')
    num_class: int = 10


@dataclass
class cifar10:
    path: str = os.path.expanduser('~/.torch/cifar-10-batches-py')
    num_class: int = 10


@dataclass
class cifar100:
    path: str = os.path.expanduser('~/.torch/cifar-100-python')
    num_class: int = 100


@dataclass
class sop:
    path: str = os.path.expanduser('/dev/shm/Stanford_Online_Products/') if \
        os.path.exists(os.path.expanduser('/dev/shm/Stanford_Online_Products/')) \
        else os.path.expanduser('~/.torch/Stanford_Online_Products/')
    list_train: str = 'Ebay_train.txt'
    list_test: str = 'Ebay_test.txt'
    num_class_val: int = 11316
    num_class: int = 22634


@dataclass
class cub:
    path: str = os.path.expanduser('/dev/shm/CUB_200_2011/') if \
        os.path.exists(os.path.expanduser('/dev/shm/CUB_200_2011/')) else \
        os.path.expanduser('~/.torch/CUB_200_2011/')
    list_images: str = 'images.txt'
    list_split: str = 'train_test_split.txt'
    num_class_val: int = 100
    num_class: int = 200


@dataclass
class cars:
    path: str = os.path.expanduser('/dev/shm/cars/') if \
        os.path.exists('/dev/shm/cars') else \
        os.path.expanduser('~/.torch/cars/')
    num_class_val: int = 98
    num_class: int = 196


@dataclass
class ilsvrc:
    path: str = os.path.expanduser('~/.torch/ILSVRC/Data/CLS-LOC')
    num_class: int = 1000

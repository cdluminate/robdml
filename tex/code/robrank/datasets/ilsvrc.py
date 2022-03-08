
# pylint: disable=too-many-function-args
import os
import numpy as np
import pickle
from PIL import Image
import torchvision as V
from .. import configs


def getDataset(kind: str = 'classification'):
    if kind == 'classification':
        return __get_classification_dataset()
    else:
        raise NotImplementedError


def __get_classification_dataset():
    '''
    https://github.com/pytorch/examples/blob/master/imagenet/main.py
    '''
    normalize = V.transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])
    train = V.datasets.ImageFolder(
        os.path.join(configs.ilsvrc.path, 'train'),
        V.transforms.Compose([
            V.transforms.RandomResizedCrop(224),
            V.transforms.RandomHorizontalFlip(),
            V.transforms.ToTensor(),
            normalize,
        ]))
    test = V.datasets.ImageFolder(
        os.path.join(configs.ilsvrc.path, 'val-symlink'),
        V.transforms.Compose([
            V.transforms.Resize(256),
            V.transforms.CenterCrop(224),
            V.transforms.ToTensor(),
            normalize,
        ]))
    return (train, None, test)

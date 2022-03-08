import torch as th
import pytorch_lightning as thl
from .. import datasets
from .. import configs
from .template_classify import ClassifierTemplate


class SLP(th.nn.Module):
    '''
    Single-Layer Perceptron (SLP)
    '''

    def __init__(self, output_size: int = 10):
        super(SLP, self).__init__()
        self.fc1 = th.nn.Linear(28 * 28, output_size)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = self.fc1(x)
        return x


class Model(ClassifierTemplate, thl.LightningModule):
    BACKBONE = 'cslp'

    def __init__(self, *, dataset: str, loss: str):
        super().__init__()
        # dataset setup
        assert(dataset in configs.cslp.allowed_datasets)
        assert(loss in configs.cslp.allowed_losses)
        # config
        self.dataset = dataset
        self.loss = loss
        self.config = getattr(configs, self.BACKBONE)(dataset, loss)
        # backbone
        self.backbone = SLP(output_size=getattr(configs, dataset).num_class)

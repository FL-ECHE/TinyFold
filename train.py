import torch as t
import torch_geometric as tg
from Dataloader import TUDataset
#look at examples of how it is instantiated

#first import proteins, with sequence and coordinates
Prot_data = TUDataset()
#bqsed on InMemoryDataset so need to implement Dataloader


import torch
import torch_geometric
from torch import nn


#create CNN for sequence distance map
class DistNN(nn.Module):
	def __init__(self):
		self.nlayers = 0
		self.input_size = 500 #num of residues max, w/ padding
		mlpList = [nn.Linear(self.input_size,deeper)] #as encoder-decoder, need depper and smaller width, kernels?   
	def forward(self):
				


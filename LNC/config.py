import numpy as np
import torch
import random
import os


# non-linear functions
eta = [2.1493e-03, 1.0022e+00, 2.3549e-03, 1.2297e+01]
inv = [2.1493e-03, 1.0022e+00, 2.3549e-03, 1.2297e+01]
rt_ = [-0.6686,  0.2794,  6.9068,  0.2375, -0.9061,  0.9282,  1.6092]

# hardware-related parameters
gmin = 0.01
gmax = 10
m = 0.3
T = 0.1

# hyperparameter for training
lr_theta = 0.1
lr_lnc   = 0.001
lr_rt    = 0.005

# variation-aware
N = 20
N_test = 100

def SetSeed(seed=0):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True 
    random.seed(seed)
    np.random.seed(seed)
    g = torch.Generator()
    g.manual_seed(seed)                  
    torch.backends.cudnn.benchmark = False
    os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
    
def Normalization(data, MIN, MAX, inverse=False):
    if not inverse:
        data_N = (data - MIN) / (MAX - MIN)
        return data_N
    else:
        data_D = data * (MAX - MIN) + MIN
        return data_D
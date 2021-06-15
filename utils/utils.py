from sklearn import preprocessing
import torch
import torchvision
import matplotlib.pyplot as plt

def label_encoder(labels):
    "Convert list of string labels to tensors"

    le = preprocessing.LabelEncoder()
    targets = le.fit_transform(labels)
                  
    return torch.as_tensor(targets)

def tensor2numpy(data):
    """Send to CPU. If computational graph is connected then detach it as well."""
    if data.requires_grad:
        return data.detach().cpu().numpy()
    else:
        return data.cpu().numpy()
    
def label2rgb(labels):
    return torch.nn.functional.one_hot(labels)
    
def normalize(x):
    """ Min-max normalization (0-1):
    
    Args:
        * x - Union[Tensor,np.ndarray]
    
    Return:
        * Union[Tensor,np.ndarray] - Return same type as input but scaled between 0 - 1
    """
    return (x - x.min())/(x.max()-x.min())
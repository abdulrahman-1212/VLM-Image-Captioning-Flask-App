import torch
import torchvision
from torch import nn


class Encoder(nn.Module):
    """Encoder Model

    Args:
        nn (_type_): _description_
    """
    def __init__(self,
                img_size: int=14):
        super(Encoder, self).__init__()
        
        self.resnet = torchvision.models.resnet34(pretrained=True)
        modules = list(self.resnet.children())[:-2]
        self.resnet = nn.Sequential(*modules)
        
        self.adaptive_pool = nn.AdaptiveAvgPool2d((img_size, img_size))
        
        
    def forward(self, images):
        """Forward Pass

        Args:
            images (Tensor): (Batch size, num_channels, height, width)

        Returns:
            Output (Tensor): (Batch size, num_channels, height, width)

        """
        output = self.resnet(images)
        output = self.adaptive_pool(output)
        output = output.permute(0, 2, 3, 1)
        return output

    def finetune(self, finetune=True):
        for p in self.resnet.parameters():
            p.requires_grad = False
        
        # Fine tune only Conv Layers
        for c in list(self.resnet.children())[5:]:
            for p in c.parameters():
                p.requires_grad = finetune
        
class Attention(nn.Module):
    """_summary_

    Args:
        nn (_type_): _description_
    """
    def __init__(self):
        super(Attention, self).__init__()
    
    
class ImageCaptioningModel(nn.Module):
    """Attention Based Image Captioning Model

    Args:
        nn (_type_): _description_
    """
    def __init__(self):
        super().__init__()
    
    
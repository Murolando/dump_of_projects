import torch.nn as nn
import torch
import numpy as np

class Generator(nn.Module):
    def __init__(self):
        super(Generator,self).__init__()

        self.main = nn.Sequential(
            # 1 => 4
            nn.ConvTranspose2d(100,  512, 4, 1, 0, bias=True),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=False),
            # 4 => 8
            nn.ConvTranspose2d(512, 256, 4, 2, 1, bias=True),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=False),
            # 8 => 16
            nn.ConvTranspose2d( 256, 128, 4, 2, 1, bias=True),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=False),
            # 16 => 32
            nn.ConvTranspose2d(128, 64, 4, 2, 1, bias=True),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=False),
            # 32 => 100
            nn.ConvTranspose2d( 64, 3, 7, 3, 0, bias=True),
            nn.Tanh()
        )

    def forward(self, x):
        return self.main(x)
        # return self.oleg(x)

def neural_net(noise) :
    generator = torch.load('NarutoGanUpdate.pt', map_location=torch.device('cpu'))
    generator.eval()
    result = generator.forward(noise)
    return result

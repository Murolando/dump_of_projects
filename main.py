from flask import Flask, render_template, url_for
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
app = Flask(__name__)
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

def neural_net(noise) :
    try:
        generator = torch.load('NarutoGanUpdate.pt', map_location=torch.device('cpu'))
        generator.eval()

        result = generator.forward(noise)
        result = np.array(result.detach())
        result = result.squeeze(0)
        result = np.rollaxis(result, 0, 3)
        result = result*255
        result = np.array(result, np.int8)

        # result = json.dumps(result)
        img = Image.fromarray(result, mode="RGB")
        img.save('static/image.png')
    except:
        print("GG")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/neural',methods=['POST'])
def neural():
    noise = torch.randn((1, 100, 1, 1))
    neural_net(noise)
    return render_template('photo.html')

if __name__ == '__main__':
    app.run(debug = True)



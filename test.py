import torch
from torch import nn


class net(nn.Module):

    def __init__(self):
        super().__init__()
        self.cov = nn.Conv2d(3, 5, (3, 3), 1, 1)

    def forward(self, input):
        output = self.cov(input)
        return output


network = net()
img = torch.randn(1, 3, 256, 256)
pred_logit = network(img)

gt = torch.LongTensor(1, 256, 256).random_(0, 6)
gt.unique()
criterion = nn.CrossEntropyLoss(ignore_index=5)
loss = criterion(pred_logit,gt)
loss.backward()
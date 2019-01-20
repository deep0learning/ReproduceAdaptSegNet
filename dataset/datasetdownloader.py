import os
import wget
from multiprocessing.dummy import Pool

## download GT5 dataset
# outdir = 'GTA5'
img_ulr = lambda d: f'https://download.visinf.tu-darmstadt.de/data/from_games/data/%.2d_images.zip' % d
gt_ulr = lambda d: f'https://download.visinf.tu-darmstadt.de/data/from_games/data/%.2d_labels.zip' % d


def get_file(id):
    wget.download(img_ulr(id))
    wget.download(gt_ulr(id))


if __name__ == '__main__':
    p = Pool(10)
    p.map(get_file, range(1, 11))

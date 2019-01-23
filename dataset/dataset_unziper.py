import os
import argparse
from multiprocessing import Pool
from pathlib import Path
import zipfile
from functools import partial

def get_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='GTA-5 dataset unziper')
    parser.add_argument('--dataset_dir', type=str, required=True)
    parser.add_argument('--out_dir', type=str, required=True, help='output dir for unziped files')
    parser.add_argument('--n', type=int, default=20, help='cpu_power to unzip')
    args = parser.parse_args()
    print(args)
    return args


def unzip(zip_path: Path, out_dir: Path) -> None:
    assert zip_path.exists()
    out_dir.mkdir(exist_ok=True, parents=True)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(out_dir)


def main(args: argparse.Namespace) -> None:
    dataset_dir: Path = Path(args.dataset_dir)
    assert dataset_dir.exists()
    out_dir: Path = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    imgzip_names = dataset_dir.glob('*images.zip')
    labzip_names = dataset_dir.glob('*labels.zip')
    P = Pool(processes=args.n)
    unzip_ = partial(unzip,out_dir=out_dir)

    P.map(unzip_, [*imgzip_names,*labzip_names])

if __name__ == '__main__':
    main(get_args())

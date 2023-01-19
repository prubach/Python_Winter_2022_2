from concurrent.futures import ProcessPoolExecutor
from functools import partial

from knotprot_download import *
from multiprocessing.pool import Pool

def download_sequentially(my_dir):
    proteins = get_proteins()
    print(proteins)
    print(len(proteins))
    for p in proteins:
        download_link(my_dir, p)


def download_multiprocessing(my_dir):
    proteins = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(12) as pl:
        pl.map(download, proteins)


def create_thumbs_seq():
    for image_path in Path('images').iterdir():
        create_thumbnail((64, 64), image_path)


def create_thumbs_paral():
    create_thumbs = partial(create_thumbnail, (64, 64))
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(create_thumbs, Path('images').iterdir())

if __name__=='__main__':
    #setup_download_dir()
    #time_it(download_sequentially, 'images')
    #time_it(download_multiprocessing, 'images')
    #time_it(create_thumbs_seq)
    time_it(create_thumbs_paral)
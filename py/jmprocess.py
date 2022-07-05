# multiprocessing boilerplate
from tqdm.contrib.concurrent import process_map
import multiprocessing as mp
from functools import partial
import pickle

def _runWorker(result, inp):
    output = None
    result.append(output)

if __name__ == '__main__':
    with mp.Manager() as manager:
        result = manager.list()
        # result = manager.dict()
        iterator_object = None
        process_map(partial(_runWorker, result), iterator_object, max_workers=4, chunksize=2)
        with open('./result.pkl', 'wb') as f: 
            pickle.dump(list(result), f)

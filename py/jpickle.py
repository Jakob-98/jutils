import pickle

def jdump(filepath, obj):
    with open(filepath, 'wb') as f: 
        pickle.dump(list(obj), f)

def jload(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(filepath)
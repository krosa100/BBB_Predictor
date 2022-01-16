import pickle

def from_disk(dir):
    '''
    return pickle at dir as obj
    '''
    return pickle.load(open(dir, 'rb'))


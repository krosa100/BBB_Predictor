import pickle

def mp(f,a):
    r = []
    for v in a:
        r.append(f(v))
    return r

def to_disk(obj, dir):
    '''
    save obj to dir as pickle
    '''
    pickle.dump(obj, open(dir, 'wb'))

def from_disk(dir):
    '''
    return pickle at dir as obj
    '''
    return pickle.load(open(dir, 'rb'))


def sf(s, *a):
    return s.format(*a)


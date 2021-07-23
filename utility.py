import sys
import json
import pickle
from multiprocessing.pool import ThreadPool
from urllib.request import urlopen
import pandas as pd
from copy import deepcopy
import numpy as np

def mp(f,a):
    r = []
    for v in a:
        r.append(f(v))
    return r

def select(f,a):
    r = []
    for v in a:
        if f(v):
            r.append(v)
    return r

def sort_by(f, a):
    return sorted(a, key=f)

def max_by(f, a):
    return a[np.argmax(mp(f, a))]

def flatten(a):
    return [item for sublist in a for item in sublist]

def write_txt(fn, s):
    f = open(fn, "w")
    f.write(s)
    f.close()

def read_txt(fn):
    f = open(fn, "r")
    s = f.read()
    f.close()
    return s

def irange(a, b):
    if b >= a:
        return range(a, b + 1)
    else:
        return range(a, b - 1, - 1)

def dict_to_json_file(d, dir):
    f = open(dir, 'w')
    json.dump(d, f)
    f.close()

def json_file_to_dict(dir):
    f = open(dir)
    d =  json.load(f)
    f.close()
    return d

def json_string_to_dict(s):
    return json.loads(s.decode())

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

def get_urls(urls):
    def fetch_url(url):
        try:
            response = urlopen(url)
            return url, response.read(), None
        except Exception as e:
            return url, None, e

    results = ThreadPool(100).imap(fetch_url, urls)
    return mp(lambda r : r[1], results)

def process_urls(f, urls):
    def fetch_url(url):
        try:
            response = urlopen(url)
            content = response.read()
            f(content)
        except:
            pass

    ThreadPool(100).map(fetch_url, urls)

def sf(s, *a):
    return s.format(*a)

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
hdr = {'User-Agent': user_agent} 
def get_json(site):
    req = urllib.request.Request(site, headers=hdr)
    page = urllib.request.urlopen(req)
    data = json.loads(page.read().decode())
    return data

pd.set_option('display.max_rows', 50)
def p_table(a):
    return pd.DataFrame(a[0:50])
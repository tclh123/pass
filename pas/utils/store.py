# coding=utf-8

import os
import cPickle


def get_store_path():
    from pas import BASE_PATH
    STORE_PATH = 'databases/pkl/'
    return os.path.join(BASE_PATH, STORE_PATH)


def make_path(key):
    store_path = get_store_path()
    key = key.strip('/')
    to_dir = '/'.join([store_path] + key.split('/')[:-1])
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
    path = os.path.join(store_path, key)
    return path


def set(key, value):
    path = make_path(key)
    with open(path, 'wb') as f:
        cPickle.dump(value, f)


def get(key, default):
    path = make_path(key)
    try:
        with open(path, 'rb') as f:
            return cPickle.load(f)
    except Exception:
        return default

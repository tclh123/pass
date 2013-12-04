# coding=utf-8

from pas.utils import store


class Platform(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    @classmethod
    def db_key(cls):
        return '/pass/platform'

    @classmethod
    def gets(cls):
        return store.get(cls.db_key())

    @classmethod
    def add(cls, name, url):
        platforms = cls.gets()
        p = cls(name, url)
        platforms.append(p)
        store.set(cls.db_key(), platforms)
        return p

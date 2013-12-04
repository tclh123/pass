# coding=utf-8

from pas.utils import store


class Platform(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return '%s => %s' % (self.name, self.url)

    def __repr__(self):
        return ('<Platform(name=%s, url=%s)>'
                % (self.name, self.url))

    @classmethod
    def db_key(cls):
        return '/pass/platform'

    @classmethod
    def _gets(cls):
        return store.get(cls.db_key(), {})

    @classmethod
    def gets(cls):
        return cls._gets().values()

    @classmethod
    def get(cls, name):
        return cls._gets().get('name', None)

    @classmethod
    def rm(cls, name):
        ps = cls._gets()
        if name in ps:
            del ps[name]
            return True
        else:
            return False

    @classmethod
    def add(cls, name, url):
        ps = cls._gets()
        p = cls(name, url)
        ps[p.name] = p
        store.set(cls.db_key(), ps)
        return p

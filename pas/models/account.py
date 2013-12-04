# coding=utf-8

from pas.utils import store
from pas.utils.passwd import mask_pwd


class Account(object):
    def __init__(self, uid, passwd, plat_name,
                 name=None, email='', phone=''):
        self.uid = uid
        self.passwd = passwd
        self.plat_name = plat_name
        self.name = name or uid
        self.email = email or ''
        self.phone = phone or ''

    def __str__(self):
        return ('{name}({uid}), {plat_name}, email: {email}, pwd: {masked_pwd}'
                .format(uid=self.uid,
                        name=self.name,
                        email=self.email,
                        plat_name=self.plat_name,
                        masked_pwd=self.masked_pwd))

    def __repr__(self):
        return ('<Account(uid=%s, name=%s, email=%s, passwd=%s, plat_name=%s)>'
                % (self.uid, self.name, self.email,
                   self.masked_pwd, self.plat_name))

    @property
    def unique_key(self):
        return (self.uid, self.plat_name)

    @property
    def masked_pwd(self):
        return mask_pwd(self.passwd)

    @classmethod
    def db_key(cls):
        return '/pass/account'

    @classmethod
    def _gets(cls):
        return store.get(cls.db_key(), {})

    @classmethod
    def gets(cls):
        return cls._gets().values()

    @classmethod
    def get(cls, uid, plat_name):
        return cls._gets().get((uid, plat_name), None)

    @classmethod
    def rm(cls, uid, plat_name):
        accs = cls._gets()
        if (uid, plat_name) in accs:
            del accs[(uid, plat_name)]
            store.set(cls.db_key(), accs)
            return True
        else:
            return False

    @classmethod
    def add(cls, uid, passwd, plat_name,
            name=None, email='', phone=''):
        if not (uid and passwd and plat_name):
            return None
        accs = cls._gets()
        a = cls(uid, passwd, plat_name, name, email, phone)
        accs[a.unique_key] = a
        store.set(cls.db_key(), accs)
        return a

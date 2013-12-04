# coding=utf-8


def mask_pwd(pwd):
    if not pwd:
        return ''
    n = len(pwd)
    prefix = suffix = ''
    if n > 2:
        n -= 2
        prefix = pwd[0]
        suffix = pwd[-1]
    masked = prefix + n * '*' + suffix
    return masked

def increase(num, tax):
    inc = num + (num * tax/100)
    return inc


def decrease(num, tax):
    dec = num - (num * tax/100)
    return dec


def double(num):
    dbl = num * 2
    return dbl


def half(num):
    half = num / 2
    return half


def currency(func):
    return f'${func:.2f}'
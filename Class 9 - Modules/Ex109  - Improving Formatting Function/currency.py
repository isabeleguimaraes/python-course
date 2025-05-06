def currency(value):
    return f'${value:.2f}'


def increase(num, tax, form=False):
    inc = num + (num * tax/100)
    return currency(inc) if form else inc


def decrease(num, tax, form=False):
    dec = num - (num * tax/100)
    return dec


def double(num, form=False):
    dbl = num * 2
    return dbl


def half(num, format=False):
    half = num / 2
    return half



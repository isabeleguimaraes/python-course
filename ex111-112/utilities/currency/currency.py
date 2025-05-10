def currency(value):
    return f'${value:.2f}'


def increase(num, tax, form=False):
    inc = num + (num * tax/100)
    return currency(inc) if form else inc


def decrease(num, tax, form=False):
    dec = num - (num * tax/100)
    return currency(dec) if form else dec


def double(num, form=False):
    dbl = num * 2
    return currency(dbl) if form else dbl


def half(num, form=False):
    half = num / 2
    return currency(half) if form else half

def summary(price, tax=0):
    print(f'The original price is {currency(price)}')
    print(f'The increased price is {increase(price,tax,True)}')
    print(f'The decreased price is {decrease(price, tax, True)}')
    print(f'The doubled price is {double(price, True)}')
    print(f'The half price is {half(price, True)}')



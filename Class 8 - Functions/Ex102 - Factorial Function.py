def factorial(number, show=False):
    """
    -> Calculating a number's factorial.
    :param number: the number to be factored.
    :return: factorial result.
    """
    f = 1
    for c in range(number, 0, -1):
        f = f * c
        if show==True:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f

print(factorial(6,show=True))



def maior(*valor):
    print(max(valor))


def bigger(*value):
    big = value[0]
    for i in value:
        if i > big:
            big = i
    print(big)

bigger(1)



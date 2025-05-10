def readvalue():
    while True:
        answer = str(input('Type a price: ')).strip()
        if answer.isnumeric():
            return float(answer)
        else:
            print(f'Your answer \"{answer}\" is invalid. Please type a valid price number.')





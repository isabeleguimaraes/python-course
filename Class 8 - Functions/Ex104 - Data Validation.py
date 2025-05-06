def readInt(string):
    while True:
        result = str(input(string)).strip()
        if result.isnumeric():
            return int(result)
        else:
            print(f'Error! Type a valid number.')

# Main Program
number = readInt('Type a number')
print(f'You typed the number {number}')

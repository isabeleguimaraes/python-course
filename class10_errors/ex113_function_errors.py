def readInt(string):
    while True:
        try:
            result = int(input(string))

        except (ValueError):
            print('\033[32mError: type a valid number\033[m')

        else:
            return result

# Main Program
number = readInt('Type a number')
print(f'You typed the number {number}')

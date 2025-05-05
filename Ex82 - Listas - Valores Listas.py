numbers = []
odd = []
even = []
while True:
    number = int(input('Type a number: '))
    numbers.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    while True:
        answer = str(input('Would you like to continue? (Y/N)')).upper().strip()[0]
        if answer in 'YN':
            break
    if answer == 'N':
        break
print(f'The major list is {numbers}, the odd number list is: {odd}, and the even numbers list is: {even}')

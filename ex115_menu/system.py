from ex115_menu.lib.interface import *
from ex115_menu.lib.archive import *
file = 'registration.txt'
if not file_exists(file):
    create_file(file)
title('Welcome to the System 115')
while True:
    title('Menu')
    opt = menu(['Registered People List', 'Register Someone', 'Exit the System'])
    if opt == 1:
        print('Registered People List')
        read_file(file)
    elif opt == 2:
        title('Register Someone')
        name = str(input('Name: '))
        age = readint('Age: ')
        register(file,name,age)

    elif opt == 3:
        title('Bye bye')
        break
    else:
        print('Try again')





from ex115_menu.lib.interface import *

title('Welcome to the System 115')
while True:
    title('Menu')
    opt = menu(['Option1', 'Option2', 'Option3'])
    if opt == 1:
        print('Option 1')
    elif opt == 2:
        print('Option 2')
    elif opt == 3:
        title('Bye bye')
        break
    else:
        print('Try again')




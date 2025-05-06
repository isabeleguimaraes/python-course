def intHelp():
    """
    Interactive help system with the user
    :return: None
    """
    while True:
        print('Interactive Help System')
        answer = str(input('Type a function or library')).strip()
        if answer.upper() == 'END':
            print('See you soon!')
            break
        else:
            help(answer)


intHelp()


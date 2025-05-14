def title(content=''):
    print('-' *30)
    print(content.center(30))
    print('-' *30)


def menu(list):
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c+=1
    option = readint('Choose an Option: ')
    return option


def readint(question):
    while True:
        try:
            answer = int(input(question))
        except:
            print('Error. Try again')
            continue
        else:
            return answer





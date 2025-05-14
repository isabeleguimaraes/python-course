def file_exists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error while creating the file')
    else:
        print(f'File {name} created successfully')


def read_file(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error reading the document')
    else:
        for line in a:
            list = line.split(';')
            list[1] = list[1].replace('\n', '')
            print(f'{list[0]:<20}{list[1]:>3}')
    finally:
        a.close()


def register(file, name, age):
    try:
        a = open(file, 'at')
    except:
        print('Error')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Error')
        else:
            print('New registration completed.')
            a.close()

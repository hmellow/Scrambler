def write(mode = 'user', *args):
    if mode == 'user':
        i = input('Please enter what you wish to put in the file:')
        with open('.env', mode='w+') as f:
            f.write(i)
        print('File sucessfully written')
    elif mode == 'called':
        with open('.env', mode='w+') as f:
            f.write(args)
        return

write('user')

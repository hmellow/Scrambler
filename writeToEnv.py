def write(mode = 'user', *args):
    if mode == 'user':
        i = input('write to env:')
        with open('.env', mode='w+') as f:
            f.write(i)
        print('File sucessfully written')
    elif mode == 'called':
        with open('.env', mode='w+') as f:
            f.write(args)
        return

write('user')

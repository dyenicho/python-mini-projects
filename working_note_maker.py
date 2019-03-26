import os.path

def dataHandler():
    global username
    global password
    username = input('Enter nickname: ')
    password = input('Enter password: ')
    return username, password


def noteMaker():
    userLocation = os.path.join(notesLocation, username + '\\')
    if os.path.exists(notesLocation + username + '\\') == False:
        os.makedirs(userLocation)
    note_name = input('Enter note\'s name: ') + '.txt'
    title = 'title:' + input('Enter a title: ') + '\n'
    with open(os.path.join(userLocation, note_name), 'w+') as note:
        note.write(title)
        note.write('------------note--------------\n')
        some_text = input('note: ')
        note.write(some_text)
        note.write('\n------------------------------')


def noteHandler():
    print('Hello, %s! choose option:\n1 view notes list\n2 make a note' % username)
    choice = input()
    if choice == '2':
        noteMaker()
    elif choice == '1':
        dir_list = os.listdir(notesLocation + username)
        for i in dir_list:
            print(i)


def signUp_menu():
    print('[1] Sign up')
    print('[2] Sign in')


def menu():
    while True:
        print(20 * '-')
        print('Hi, %s!\n' % username)
        print('[1] Make a note')
        print('[2] View list of notes\n')
        print('[0] Log out')
        print(20 * '-')
        choice = input('> ')
        if choice == '1':
            noteMaker()
        elif choice == '2':
            dir_list = os.listdir(notesLocation + username)
            for i in dir_list:
                print(i)
        elif choice == '0':
            break

notesLocation = os.path.expanduser('~') + '\Desktop\\my python notebook\\'
#os.makedirs(notesLocation)

database = {}
username = None
tries = 4

while tries != 0:
    signUp_menu()
    choice = input('> ')
    if choice == '1':
        dataHandler()
        database.update({username: password})
        menu()
    if choice == '2':
        while tries != 0:
            dataHandler()
            for usr, psw in database.items():
                if usr != username or psw != password:
                    tries -= 1
                    print('Invalid data, please, try again.', tries, ' more tries left')
                    if tries == 0:
                        print('You\'re blocked')
                else:
                    tries = 4
                    menu()
            break
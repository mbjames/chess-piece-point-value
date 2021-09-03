import menu


def start():
    menu.main_menu()

    answer = input('\n > ').lower()

    if answer == 'q':
        exit()

    elif answer == '1':
        print('\n Pawn = 1')

        start()

    elif answer == '2':
        print('\n Bishop = 3')

        start()

    elif answer == '3':
        print('\n Knight = 3')

        start()

    elif answer == '4':
        print('\n Rook = 5')

        start()

    elif answer == '5':
        print('\n Queen = 9')

        start()

    elif answer == '6':
        print('\n King = Infinite')

        start()

    else:
        print('INVALID SELECTION!!!')

        start()


start()

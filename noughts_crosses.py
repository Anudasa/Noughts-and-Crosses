def display_board(gameboard):
    for x in range(len(gameboard)):
        print(gameboard[x][0], gameboard[x][1], gameboard[x][2])

def registration(player_base):
    for i in player_base:
        print('\n ', "Игрок за ", i, ": ")
        player_base[i] = input()

def check_draw(gameboard):
    if all(all(cell != ' ' for cell in row) for row in gameboard):
        return True
    return False

def check_winner(gameboard, turn):
    for i in range(3):
        if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] == turn or \
           gameboard[0][i] == gameboard[1][i] == gameboard[2][i] == turn:
            return True

    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == turn or \
       gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == turn:
        return True

    return False

def play_game():          
    gameboard = [[' '] * 3 for _ in range(3)]
    player_base = {"X": "", "O": ""}
    running = True

    registration(player_base)

    while running:
        for turn in player_base:
            print("\n", "Ходит:", player_base[turn])
            display_board(gameboard)

            while True:
                square = int(input("Введите номер клетки (1-9): "))
                row = (square - 1) // 3
                column = (square - 1) % 3

                if gameboard[row][column] == ' ':
                    gameboard[row][column] = turn
                    break
                else:
                    print('Это поле уже занято. Попробуйте еще раз.')

            if check_winner(gameboard, turn):
                display_board(gameboard)
                print(player_base[turn], "Победил!")
                running = False
                break

            if check_draw(gameboard):
                display_board(gameboard)
                print("Ничья!")
                running = False
                break

while True:
    play_game()
    print("Хочешь сыграть еще раз: Y / N")
    decision = input()
    if decision.capitalize == 'Y':
        continue
    elif decision.capitalize == 'N':
        break
    else:
        break
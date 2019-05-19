import itertools


def game_board(curr_game, player=0, row=0, column=0, just_display=False):
    try:
        if curr_game[row][column] != 0 and player != 0:
            print("This space is occupied try another")
            return False

        if not just_display:
            curr_game[row][column] = player

        print("   0  1  2")
        for count, row in enumerate(curr_game):
            print(count, row)
        return curr_game
    except IndexError:
        print("You played row column outside the range")
        return False
    except Exception as e:
        print(str(e))
        return False


def winner(curr_game):

    def all_same(l):
        if(l.count(l[0]) == len(l) and l[0] != 0):
            return True
        else:
            return False

    # Horizontal
    for row in curr_game:
        if all_same(row):
            print(f"Player {row[0]} has won Horizontally")
            return True

    # Vertical
    for col in range(len(curr_game[0])):
        check = []
        for row in curr_game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} has won Vertically")
            return True

    # Diagonal
    dia = []
    for idx in range(len(curr_game)):
        dia.append(curr_game[idx][idx])

    if all_same(dia):
        print(f"Player {dia[0]} has won Dialgonally")
        return True

    dia = []
    for idx, reverse_idx in enumerate(reversed(range(len(curr_game)))):
        dia.append(curr_game[idx][reverse_idx])

    if all_same(dia):
        print(f"Player {dia[0]} has won rev Dialgonally")
        return True

    return False


play = True
players = [1, 2]
while play:
    game = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    game_won = False
    palyer_cycle = itertools.cycle([1, 2])
    game_board(curr_game=game, just_display=True)
    while not game_won:
        current_player = next(palyer_cycle)
        played = False
        while not played:
            print(f"Player: {current_player}")
            row_choice = int(input("Which row? "))
            col_choice = int(input("Which column? "))

            played = game_board(game, player=current_player,
                            row=row_choice, column=col_choice)

        if(winner(game)):
            game_won = True
            again = input("Do you want to play more?(y/n)")

            if(again.lower() == "y"):
                print("Restarting the game.....")
                play = True
            elif(again.lower() == "n"):
                print("Bye....")
                play = False
            else:
                print("Wrong option. Bye....")
                play = False

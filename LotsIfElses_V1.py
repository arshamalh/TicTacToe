# Dead version
from itertools import cycle

class GameBoard:

    sign = 'X'
    matrix = []

    def __init__(self, row, column):
        self.size = [row, column]
        self.shape = ''
        self.matrix = [['-' for _ in range(self.size[1])] for _ in range(self.size[0])]

    def drawer(self):
        self.shape = ''
        for i in range(self.size[0]):
            self.shape += ' ---' * self.size[1] + '\n'
            for j in range(self.size[1]):
                self.shape += f'| {self.matrix[i][j]} '
            self.shape += '|' + '\n'
        self.shape += ' ---' * self.size[1] + '\n'
        return self.shape

    def filler(self, player, choice):
        if self.matrix[choice[0] - 1][choice[1] - 1] == '-':
            if player == 1:
                self.sign = 'X'
            elif player == 2:
                self.sign = 'O'
            else:
                print('I have some problems with Player number!')
            self.matrix[choice[0] - 1][choice[1] - 1] = self.sign
            return True
        else:
            return False

    def checker(self):
        winner = ''
        xPlayer = "X"
        oPlayer = "O"
        winnerX = False
        winnerO = False
        for i in self.matrix:
            if i[0] == i[1] == i[2] == xPlayer: # like ---
                winner = xPlayer
                break
            elif i[0] == i[1] == i[2] == oPlayer:
                winner = oPlayer
                break

            # winnerX = i[0] == i[1] == i[2] == xPlayer

            else:
                for i in range(3):
                    if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == xPlayer: # like |
                        winner = xPlayer
                        break
                    elif self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == oPlayer:
                        winner = oPlayer
                        break
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == xPlayer: # like this: \
            winner = xPlayer
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == xPlayer: # like this /
            winner = xPlayer
        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == oPlayer:
            winner = oPlayer
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == oPlayer: 
            winner = oPlayer
        
        if winner == xPlayer:
            return True, 'Player 1 is winner'
        elif winner == oPlayer:
            return True, 'Player 2 is winner'

        return True, "No Winner!"

board = GameBoard(3, 3)
player_cyc = cycle([1, 2])
place_filled = 0
while True:
    pl = next(player_cyc)
    list_of_choices = []
    while True:
        if len(list_of_choices) != 2:
            position = input(f'player {pl} please enter your position: '
                    ).replace(',', "").replace('.', "").replace('/', "").replace('-', "").replace(' ', "")
            list_of_choices = [int(ch) for ch in position if ch.isnumeric()]

        else:
            break
    while True:
        if not board.filler(pl, list_of_choices):
            print('that place is filled, please select somewhere else')
            position = input(f'player {pl} please enter your position: ').split(',')
            list_of_choices = [int(ch) for ch in position if ch.isnumeric()]
        else:
            break
    print(board.drawer())
    place_filled += 1
    print(f'{place_filled} place is filled')
    if place_filled > 4:
        checked, pl_winner = board.checker()
        if checked:
            print(f'{pl_winner}')
            break
    if place_filled == 9:
        print('No player won, play again!')


# TODO: can it be a package? so make it simpler to understand and documented
# TODO: make everything happened in class an while loop in play method
# TODO: don't repeat, line 75 and 89 are same (position input)
# TODO: it has to work for bigger GameBords (the problem is with cheker)
# TODO: make a toturial how did you do this

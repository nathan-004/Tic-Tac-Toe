from copy import deepcopy

class Board():
    def __init__(self, board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]):
        self.board = board
        self.count = 0

    def print(self, board=None):
        if board is None:
            board = self.board
        row = []
        print(" 0   1   2  ")
        for ind, i in enumerate(board):
            for index, j in enumerate(i):
                if index != 2:
                    row.append(" " + j + " |")
                else:
                    row.append(" " + j + " |")
            print("".join(row) + " " + str(ind) + " ")
            row = []
        print(" ")

    def player(self, board):
        count = 0
        for i in board:
            for j in i:
                if j != " " and j != "":
                    count += 1
        if count % 2 == 0:
            return "X"
        return "O"

    def move(self, move):
        print(move)
        if self.board[move[0]][move[1]] == " ":
            self.board[move[0]][move[1]] = self.player(self.board)
            self.count += 1

    def reset(self):
        self.__init__([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])

    def isWinner(self, board):
        for row in board:
            if all(cell == 'X' for cell in row):
                return 'X'
            if all(cell == 'O' for cell in row):
                return 'O'

        for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)):
                return 'X'
            if all(board[row][col] == 'O' for row in range(3)):
                return 'O'

        if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
            return 'X'
        if all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
            return 'O'

        return None

    def isEnded(self, board):
        if self.isWinner(board) is not None:
            return True
        count = 0
        for i in board:
            count += i.count(" ")
        if count == 0:
            return True
        return False

    def getActions(self, board):
        actions = []
        for ind, i in enumerate(board):
            for index, j in enumerate(i):
                if j == " ":
                    actions.append((ind, index))
        return actions

    def getValue(self, board):
        if self.isEnded(board):
            if self.isWinner(board) is not None:
                if self.isWinner(board) == "O":
                    return -1
                else:
                    return 1
            else:
                return 2008
        return 0

    def getResult(self, board, move, player_=None):
        y, x = move
        new_board = deepcopy(board)
        if self.player(board) == "O":
            player = "X"
        else:
            player = "O"

        if player_ is not None:
            player = player_
        new_board[y][x] = player
        return new_board


from game import Board
from random import choice
import time
import random

class Node():
    def __init__(self, player:str, board: Board, move, depth: int):
        """
        Init a Node instance

        Inputs
        -------
        player:str
            Either X or O, define the player that plays the current move
        board:Board
            Board object to access the board functions and the current board
        move:tuple
            tuple of the last move played (y, x)
        depth:int
            the depth of the board in the tree
        """

        self.player = player
        self.board_ = board
        self.board = board.board
        self.move = move
        self.depth = depth

    def get_best_move(self):
        """
        Returns the best move of the possible moves

        Returns
        -------
        tuple
            (value, (best move possible))

        * Use of an other function to get max/min to not rewrite all this function
        """
        if self.board_.isEnded(self.board): # If the game ended, return the value
            value = self.board_.getValue(self.board)
            if value == 2008: # Check if tie
                return (0, self.move)
            elif value < 0:
                value = value * 10 + self.depth
            elif value > 0:
                value = value * 10 - self.depth
            return (value, self.move)

        if self.player == "X": # Define the children player
            player = "O"
            best_val = -10
        else:
            player = "X"
            best_val = 10

        best_move = None

        # Loop all over the children Nodes
        for move in self.board_.getActions(self.board):
            #  Get their best move
            value= Node(player, Board(self.board_.getResult(self.board, move, self.player)), move, self.depth + 1).get_best_move()[0]
            #  value <- the best
            new = self.best_between_two(best_val, value)

            # Implement alpha beta -> to do

            best_val = new[0]
            if new[1] == 1:
                best_move = move

        return (best_val, best_move)

    def best_between_two(self, val1, val2):
        """
        Returns max(val1, val2) or min(val1, val2) depending on the player.

        Inputs
        -------
        val1:int
            First number or the best_val
        val2:int
            Second number or the val

        Returns
        -------
        list
            First element is the max or the min of the given value depending on the player and the second is 0 or 1 corresponding to the best move
        """

        if self.player == "X":
            if val1 == val2:
                return [val1, random.randint(0, 1)] # Add randomness
            m = max(val1, val2)
            return [m, val2==m]
        else:
            if val1 == val2:
                return [val1, random.randint(0, 1)] # Add randomness
            m = min(val1, val2)
            return [m, val2==m]


class Bot():
    def __init__(self, player: str, board: Board) -> None:
        """
        Init a Bot instance

        Inputs
        -------
        player : str
            Either O or X -> define the player than the bot plays
        board: Board
            Board object that give access to the basic functions
        """

        self.player = player
        self.board = board

    def play(self):
        """
        Returns the Bot move

        Returns
        -------
        tuple
            Move that the bot plays (x, y)
        """

        start = time.time()
        root = Node(self.player, self.board, None, 0) # Define the root Node of the tree
        move = root.get_best_move()
        end = time.time()
        print(end-start)
        return move[1]

#https://medium.com/@alialaa/tic-tac-toe-with-javascript-es2015-ai-player-with-minimax-algorithm-59f069f46efa
#https://fr.wikipedia.org/wiki/%C3%89lagage_alpha-b%C3%AAta#:~:text=En%20informatique,%20plus%20pr%C3%A9cis%C3%A9ment%20en%20intelligence%20artificielle%20et

import tkinter as tk
from tkinter import ttk
from random import choice, randint

from game import Board
from bot import Bot

class Game():

    def __init__(self) -> None:
        self.board = Board([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
        self.board.reset()
        self.bot = Bot(" ", Board([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]))

    def home(self):
        print("  _______                  ______                       ______         ")
        print(" /_  __(_)____            /_  __/___ ______            /_  __/___  ___ ")
        print("  / / / / ___/  ______     / / / __ `/ ___/  ______     / / / __ \/ _ \ ")
        print(" / / / / /__   /_____/    / / / /_/ / /__   /_____/    / / / /_/ /  __/")
        print("/_/ /_/\___/             /_/  \__,_/\___/             /_/  \____/\___/ ")
        print(" ")
        while True:
            self.player = input("X ou O : ")
            if self.player == "quit":
                raise SystemExit("Quiting...")
            if self.player.lower() == "x" or self.player.lower() == "o":
                break
        if self.player.lower() == "x":
            self.botP = "O"
        else:
            self.botP = "X"
        self.play()

    def play(self):
        if self.board.player(self.board.board) == self.player.upper(): # If it's the player turn
            self.board.move(self.playP()) # Make the player move
        else:
            self.board.move(self.playB()) # Makes the bot move
        if self.board.isEnded(self.board.board): # If the game is ended
            self.board.print() # print the board
            if self.board.isWinner(self.board.board) is not None: # If there is a winner
                print("Victoire de " + self.board.isWinner(self.board.board))
            else:
                print("Egalité")
            self.__init__()
        self.play() # Call the play function

    def play_botvsbot(self, n):
        """Make two bots play"""
        score = {"X": 0, "O": 0, "Tie": 0}
        for game in range(n):
            self.board.move((randint(0, 2), randint(0, 2)))

            while not self.board.isEnded(self.board.board):
                self.botP = self.board.player(self.board.board)
                self.board.move(self.playB())
                self.board.print()
            if self.board.isWinner(self.board.board) is not None:
                winner = self.board.isWinner(self.board.board)
                print("Victoire de " + winner)
                score[winner] += 1
            else:
                print("Egalité")
                score["Tie"] += 1
            print(score)
            self.__init__()

    def playP(self):
        self.board.print()
        move = input("Quel coup " + self.player + " : ")
        print(" ")
        if move == "quit":
            raise SystemExit("Quiting...")
        elif move == "":
            return self.playB(self.board.player(self.board.board))
        if not move.isnumeric() or len(move) != 2:
            self.playP()
        x, y = int(move[0]), int(move[1])
        return (y, x)

    def playB(self, botP=None):
        if botP is None:
            botP = self.botP
        self.bot.__init__(botP, Board(self.board.board))
        move = self.bot.play()
        return move

class Window():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Morpion")

        window = (1300, 800)
        screen = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())

        self.root.geometry(str(window[0]) + "x" + str(window[1]) + "+" + str(int((screen[0]/2 - window[0] / 2))) + "+" + str(int((screen[1]/2 - window[1] / 2)))) # ("widthxheight+x+y")
        self.root.resizable(False, False) # Empeche de bouger la fenetre

        # root.iconbitmap('./assets/pythontutorial.ico') MODIFIER L'ICONE

        # Menubutton variables
        self.player = None
        self.selected_player = tk.StringVar()
        self.selected_player.trace("w", self.get_player)

    def __home__(self):
        """
        Launch the home menu
        """

        # Display the title
        title = ttk.Label(
            self.root,
            text = "Morpion",
            font = ("Helvetica", 60)
        )

        title.pack(ipadx=10, ipady=10)


        # Display the button to choose between X and O
        player = ttk.Menubutton(
            self.root,
            text="Sélectionne un joueur"
        )

        menu = tk.Menu(player, tearoff=0)

        menu.add_radiobutton(
            label="X",
            value="X",
            variable=self.selected_player)

        menu.add_radiobutton(
            label="O",
            value="O",
            variable=self.selected_player)

        player["menu"] = menu

        player.pack(ipadx=10, ipady=10, expand=True)


        # Creates the button to launch a game
        button = ttk.Button(
            self.root,
            text="Jouer",
            command=self.__play__
        )

        button.pack(ipadx=10, ipady=10, expand=True)

        self.root.mainloop()

    def get_player(self, *args):
        """
        Get the value from the player menu button
        Put the value in the self.player variable
        """
        self.player = self.selected_player.get()

    def __play__(self):
        """
        Makes the Interface to play the game
        """

        if self.player is None:
            self.root.destroy()
            self.__home__()

        print(self.player)

root = Window()
root.__home__()

# https://www.pythontutorial.net/tkinter/tkinter-ttk/

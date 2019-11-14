from os import name, system

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class Tictactoe():
    win_patterns = ([1,2,3],[1,5,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9])
    def __init__(self):
        self.cells = {1:"_", 2:"_", 3:"_",\
                      4:"_", 5:"_", 6:"_",\
                      7:"_", 8:"_", 9:"_"}
        self.currentPlayer = 1
        self.player_marks = {1: "O", 2:"X"}
        self.ended = False
        self.show()

    def show(self):
        clear()
        print("")
        for i, v in self.cells.items():
            print("|", end=v)
            if i%3 == 0:
                print("|")
        print("Player: {}".format(self.currentPlayer))
        print("Please select cell: ")


    def move(self, cell):
        self.cells[cell] = self.player_marks[self.currentPlayer]
        self.show()

    def checkboard(self):
        for L in self.win_patterns:
            if len([x for x in L if self.cells[x] == self.player_marks[self.currentPlayer]]) == 3:
                print("Player {} won!!".format(self.currentPlayer))
                self.ended = True
                return

        if not ("_" in self.cells.values()):
            print("It's a draw.")
            self.ended = True
            return

    def change_player(self):
        self.currentPlayer = self.currentPlayer%2 +1

    def validate_cell(self,cell):
        if self.cells[cell]=="_":
            return True

        print("The cell is already taken.")
        print("Try another cell")
        return False

    def isended(self):
        return self.ended


def start_game():
    print("Tictactoe\n")
    tictac = Tictactoe()

    while not tictac.isended():
        try:
            c = int(input())
        except ValueError as e:
            print("Wrong input. Please input from 1 to 9.")
        else:
            if c < 1 or c > 9:
                print("Wrong input. Please input from 1 to 9.")
                continue
            if not tictac.validate_cell(c):
                continue

            tictac.move(c)
            tictac.checkboard()
            tictac.change_player()


if __name__ == "__main__":
    ans = True
    while ans:
        start_game()
        a = input("Continue? (Y/N)")
        if a == "y" or "Y":
            continue
        else:
            ans = False
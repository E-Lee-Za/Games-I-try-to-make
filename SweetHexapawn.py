#MODULES USED
from random import *

#BASIC HEXAPAWN
pwins = 0
cwins = 0
#ALL POSSIBLE PLAYER'S BOARDS AS ARRAY HERE
#TThe moves from the board images are left to right
class Board:
  def __init__(self, board, moves):
      self.board = board
      self.moves = moves

boards1 = ["# O O\nO # #\nX X X", "O # O\n# O #\nX X X", "O O #\n# # O\nX X X"] #move1 boards

b1 = Board("# # O\nO # #\nX # X", 1)
b2 = Board("# # O\nX O #\nX # X", randint(1,5))
b3 = Board("# O #\nX # O\nX # X", randint(1,3))
b4 = Board("# O #\nO O #\nX X #", randint(1,4))
b5 = Board("# # O\nO O X\nX X #", randint(1,3))
b6 = Board("# # O\nO # O\nX X #", randint(1,4))
b7 = Board("O # #\nX O O\n# X X", randint(1,3))
b8 = Board("# # O\n# O #\n# X X", randint(1,5))
b9 = Board("O # #\n# O #\n# X X", randint(1,3))
b10 = Board("O # #\n# O #\n# X X", randint(1,3))
b11 = Board("O # #\n# X O\n# X X", randint(1,4))
boards2 = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11] #move2 boards

c1 = Board("# # #\nO O O\nX # #", 1)
c2 = Board("# # #\nX O #\n# # X", randint(1,4))
c3 = Board("# # #\nX X O\n# # X", randint(1,3))
c4 = Board("# # #\nX O #\nX # #", randint(1,3))
c5 = Board("# # #\nX X O\nX # #", randint(1,3))
c6 = Board("# # #\nO O X\n# X #", randint(1,3))
c7 = Board("# # #\nX O O\n# X #", randint(1,3))
c8 = Board("# # #\n# X O\n# X #", randint(1,3))
c9 = Board("# # #\nO X #\n# X #", randint(1,3))
c10 = Board("# # #\nO X X\n# # X", randint(1,3))
c11 = Board("# # #\n# O X\n# # X", randint(1,3))

boards3 = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]#move3 boards

#START GAME - 1st move
print("You play as O, computer is X")
currentboard = "O O O\n# # #\nX X X"
print(currentboard)

#PLAYER MOVE 1
print("\n0 \n" + boards1[0])
print("\n1 \n" + boards1[1])
print("2 \n" + boards1[2])

pmove = int(input("Which move will you make? Type 0/1/2 >>> "))
currentboard = boards1[pmove];

#COMPUTER MOVE 1
if currentboard == boards1[0]:
    cmove = randint(1, 3)
    if cmove == 1:
        currentboard = "# O O\nX # #\nX # X"
    elif cmove == 2:
        currentboard = "# O O\nO X #\nX # X"
    else:
        currentboard = "# O O\nO # X\nX X #"

if currentboard == boards1[1]:
    cmove = randint(1, 3)
    if cmove == 1:
        currentboard = "O # O\nX O #\n# X X"
    else:
        currentboard = "O # O\n# X #\n# X X"

if currentboard == boards1[2]:
    cmove = randint(1, 4)
    if cmove == 1:
        currentboard = "O O #\n# # X\nX # X"
    elif cmove == 2:
        currentboard = "O O #\n# X O\nX # X"
    else:
        currentboard = "O O #\nX # O\nX # X"

print("Computer has moved")

#MOVE 2
print(currentboard)
#PLAYER'S MOVE
print("Your turn: your possible moves:")
#ALL POSSIBLE MOVES AS ARRAY HERE
pboards2 = [Board("# O O\nO X #\nX # X", ["# O #\nO O #\nX # X", "# O #\nO X O\nX # X"]),
            Board("# O O\nX # #\nX # X", ["# # O\nO # #\nX # X", "# # O\nX O #\nX # X", "# O #\nX # O\nX # X"]),
            Board("# O O\nO # X\nX X #", ["# # O\nO O X\nX X #", "# # O\nO # O\nX X #", "# O O\n# # X\nX O #"]),
            Board("O O #\n# # X\nX # X", ["# O #\nO # X\nX X #", "O # #\n# O X\nX X #", "O # #\n# # O\nX X #"]),
            Board("O O #\n# X O\nX # X", "# O #\n# O O\nX # X"),
            Board("O O #\nX # O\nX # X", ["O # #\nO # O\nX # X", "O # #\nX O O\nX # X"]),
            Board("O # O\nX O #\n# X X", "O # #\nX O O\n# X X"),
            Board("O # O\n# X #\n# X X",["# # O\nO X #\n# X X", "# # O\n# O #\n# X X", "O # #\n# X O\n# X X", "O # #\n# O #\n# X X"])]

possiblemovesP = []

#FIND CURRENT BOARD AND GET ALL POSSIBLE MOVES
for i in range (0, len(pboards2)):
    if currentboard == pboards2[i].board:
        possiblemovesP = pboards2[i].moves
        break    
for x in range(0, len(possiblemovesP)):
    print(x)
    print(str(possiblemovesP[x]))

#CHOOSE WHICH MOVE TO PLAY
pmove = int(input("Which move will you make? >>> "))
currentboard = pboards2[i].moves[pmove]
#COMPUTER'S TURN
#GET CURRENT BOARD
possiblemovesC = []
moveTaken = 0
for y in range(1, len(boards2)):
    if currentboard == boards2[y].board:
        moveTaken = boards2[y].moves
# RANDOMLY CHOOSE WHAT MOVE TO MAKE, MAKE MOVE, STORE WHAT MOVE IT WAS IN A VARIABLE

cmove = possiblemovesC[moveTaken]
currentboard = cmove
print("Computer moved")
print(currentboard)

#THE REST HASN'T BEEN MADE YET.

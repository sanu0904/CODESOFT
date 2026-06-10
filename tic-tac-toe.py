# Simple Tic Tac Toe with AI

board = [" "] * 9


# Print board
def show():

    for i in range(0, 9, 3):

        print(board[i], "|", board[i+1], "|", board[i+2])

        if i < 6:
            print("--+---+--")

    print()


# Check winner
def winner(p):

    wins = [

        [0,1,2], [3,4,5], [6,7,8],

        [0,3,6], [1,4,7], [2,5,8],

        [0,4,8], [2,4,6]
    ]

    for w in wins:

        if (
            board[w[0]] == p and
            board[w[1]] == p and
            board[w[2]] == p
        ):

            return True

    return False


# Check draw
def draw():

    return " " not in board


# AI move
def ai():

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"
            return


# Position guide
print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")


# Main game
while True:

    show()

    move = int(input("Enter position: "))

    if board[move] != " ":

        print("Already taken!")
        continue

    # Player move
    board[move] = "X"

    if winner("X"):

        show()
        print("You Win!")
        break

    if draw():

        show()
        print("Draw!")
        break

    # AI move
    ai()

    if winner("O"):

        show()
        print("AI Wins!")
        break

    if draw():

        show()
        print("Draw!")
        break

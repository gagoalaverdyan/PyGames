def print_board(b):
    print("-------------")
    print(f"| {b[0][0]} | {b[0][1]} | {b[0][2]} |")
    print(f"| {b[1][0]} | {b[1][1]} | {b[1][2]} |")
    print(f"| {b[2][0]} | {b[2][1]} | {b[2][2]} |")
    print("-------------")


def checkWin(b, z):
    variants = [
        b[0][0] == b[0][1] == b[0][2] == z,
        b[1][0] == b[1][1] == b[1][2] == z,
        b[2][0] == b[2][1] == b[2][2] == z,
        b[0][0] == b[1][0] == b[2][0] == z,
        b[0][1] == b[1][1] == b[2][1] == z,
        b[0][2] == b[1][2] == b[2][2] == z,
        b[0][0] == b[1][1] == b[2][2] == z,
        b[2][0] == b[1][1] == b[0][2] == z,
    ]
    if any(variants):
        return True


def playerInput(znak, num):
    if num < 4:
        board[0][num - 1] = znak
    elif 3 < num < 7:
        board[1][num - 4] = znak
    elif 6 < num < 10:
        board[2][num - 7] = znak


board = [["*", "*", "*"] for _ in range(3)]
variants = [int(i) for i in range(1, 10)]
winner = False

print_board(board)
while True:
    try:
        if variants:
            p1 = int(input("X player, enter a number (1-9):\n"))
            playerInput("X", p1)
            print_board(board)
            variants.pop(variants.index(p1))
            if checkWin(board, "X"):
                print("X Won!")
                winner = True
                break
        if variants:
            p2 = int(input("O player, enter a number (1-9):\n"))
            playerInput("O", p2)
            print_board(board)
            variants.pop(variants.index(p2))
            if checkWin(board, "O"):
                print("O Won!")
                winner = True
                break
        else:
            break
    except:
        print("Wrong cell! Try again.")
        continue

if not winner:
    print("It's a tie!")

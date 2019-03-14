import queue
from datetime import datetime

starttime = datetime.now()


def createMaze():
    maze = []
    print("Where do you want your start node?")
    user_input = int(input("Pick a number between 1-5: "))
    print("Where do you want your end node?")
    user_input2 = int(input("Enter a number between 1-5: "))

    # for the first position

    if user_input == 1 and user_input2 == 1:
        maze.append(["#", "O", "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 1 and user_input2 == 2:
        maze.append(["#", "O", "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 1 and user_input2 == 3:
        maze.append(["#", "O", "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 1 and user_input2 == 4:
        maze.append(["#", "O", "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 1 and user_input2 == 5:
        maze.append(["#", "O", "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the second position

    elif user_input == 2 and user_input2 == 1:
        maze.append(["#", "#", "O", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 2 and user_input2 == 2:
        maze.append(["#", "#", "O", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 2 and user_input2 == 3:
        maze.append(["#", "#", "O", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 2 and user_input2 == 4:
        maze.append(["#", "#", "O", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 2 and user_input2 == 5:
        maze.append(["#", "#", "O", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the third position

    elif user_input == 3 and user_input2 == 1:
        maze.append(["#", "#", "#", "O", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 3 and user_input2 == 2:
        maze.append(["#", "#", "#", "O", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 3 and user_input2 == 3:
        maze.append(["#", "#", "#", "O", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 3 and user_input2 == 4:
        maze.append(["#", "#", "#", "O", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 3 and user_input2 == 5:
        maze.append(["#", "#", "#", "O", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the forth position

    elif user_input == 4 and user_input2 == 1:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 4 and user_input2 == 2:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 4 and user_input2 == 3:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 4 and user_input2 == 4:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 4 and user_input2 == 5:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the fifth position

    elif user_input == 5 and user_input2 == 1:
        maze.append(["#", "#", "#", "#", "#", "O", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 5 and user_input2 == 2:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 5 and user_input2 == 3:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 5 and user_input2 == 4:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 5 and user_input2 == 5:
        maze.append(["#", "#", "#", "#", "O", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

    else:
        print("Invalid number input")
        return False

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif maze[j][i] == "#":
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze()

while not findEnd(maze, add):
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)

print("Run in  ", datetime.now() - starttime)
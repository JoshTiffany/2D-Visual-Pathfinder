import queue
from datetime import datetime
import termcolor


starttime = datetime.now()


def createMaze():
    maze = []
    print(termcolor.colored("Where do you want your start node?", 'blue'))
    user_input = int(input(termcolor.colored("Pick a number between 1-5: ", "red")))
    print(termcolor.colored("Where do you want your end node?", "blue"))
    user_input2 = int(input(termcolor.colored("Enter a number between 1-5: ", "red")))

    # for the first position

    if user_input == 1 and user_input2 == 1:
        maze.append(["#", termcolor.colored("O", "red"), "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 1 and user_input2 == 2:
        maze.append(["#", termcolor.colored("O", "red"), "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 1 and user_input2 == 3:
        maze.append(["#", termcolor.colored("O", "red"), "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 1 and user_input2 == 4:
        maze.append(["#", termcolor.colored("O", "red"), "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 1 and user_input2 == 5:
        maze.append(["#", termcolor.colored("O", "red"), "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the second position

    elif user_input == 2 and user_input2 == 1:
        maze.append(["#", "#", termcolor.colored("O", "red"), "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 2 and user_input2 == 2:
        maze.append(["#", "#", termcolor.colored("O", "red"), "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 2 and user_input2 == 3:
        maze.append(["#", "#", termcolor.colored("O", "red"), "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 2 and user_input2 == 4:
        maze.append(["#", "#", termcolor.colored("O", "red"), "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 2 and user_input2 == 5:
        maze.append(["#", "#", termcolor.colored("O", "red"), "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the third position

    elif user_input == 3 and user_input2 == 1:
        maze.append(["#", "#", "#", termcolor.colored("O", "red"), "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 3 and user_input2 == 2:
        maze.append(["#", "#", "#", termcolor.colored("O", "red"), "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 3 and user_input2 == 3:
        maze.append(["#", "#", "#", termcolor.colored("O", "red"), "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 3 and user_input2 == 4:
        maze.append(["#", "#", "#", termcolor.colored("O", "red"), "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 3 and user_input2 == 5:
        maze.append(["#", "#", "#", termcolor.colored("O", "red"), "#", "#", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the forth position

    elif user_input == 4 and user_input2 == 1:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 4 and user_input2 == 2:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 4 and user_input2 == 3:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 4 and user_input2 == 4:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 4 and user_input2 == 5:
        maze.append(["#", "#", "#", "#",termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "X", "#"])

        # for the fifth position

    elif user_input == 5 and user_input2 == 1:
        maze.append(["#", "#", "#", "#", "#", termcolor.colored("O", "red"), "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "X", "#", "#", "#", "#", "#"])

    elif user_input == 5 and user_input2 == 2:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "X", "#", "#", "#", "#"])

    elif user_input == 5 and user_input2 == 3:
        maze.append(["#", "#", "#", "#",termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#", "#", "#", "X", "#", "#", "#"])

    elif user_input == 5 and user_input2 == 4:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#", " ", "#", " ", " ", " ", "#"])
        maze.append(["#", " ", "#", "#", "#", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "X", "#", "#"])

    elif user_input == 5 and user_input2 == 5:
        maze.append(["#", "#", "#", "#", termcolor.colored("O", "red"), "#", "#"])
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
        if pos == termcolor.colored("O", "red"):
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
                print(termcolor.colored("+ ", "blue"), end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == termcolor.colored("O", "red"):
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
        if pos == termcolor.colored("O", "red"):
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
        print(termcolor.colored("Found: ", "yellow") + termcolor.colored(moves, "green"))
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

print(termcolor.colored("Run in: ", "yellow"), termcolor.colored( datetime.now() - starttime, "green"))

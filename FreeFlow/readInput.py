#In this file write functions relating to File i/o
import glob
import copy

def get_list_of_test_files():
    return glob.glob("./Inputs/Test/*")

def get_list_of_smaller_files():
    return glob.glob("./Inputs/Smaller/*")

def get_list_of_smaller_files():
    return glob.glob("./Inputs/Bigger/*")

def get_list_of_solved_files():
    return glob.glob("./Inputs/Solved/*")

def input_to_array(file):
    lines = []
    for line in open(file):
        appendable = list(line.rstrip('\n'))
        lines.append(appendable)
    return lines

def get_name(file):
    names = file.split('/')
    name = names[3]
    name, trash = name.split('.')
    return name[5:]

def puzzleDetails(lines):
    height = 0
    width = 0
    for line in lines:
        height += 1
        width = len(lines)
    return height, width

def generateColorSet_Dict(lines):
    colorSet = []
    colorDict = {}
    for line in lines:
        for character in line:
            if character != '_':
                colorSet.append(character)
    colorSet = set(colorSet)

    for line in lines:
        for character in line:
            if character in colorSet:
                colorDict[lines.index(line), line.index(character)] = character
    return colorSet, colorDict

def print_free_flow(solved_maze,height,width):
    # (row,column)
    out=[]
    outline = []
    for i in range(0,width):
        outline.append('_')
    for i in range(0,height):
        out.append(outline[:])

    for key in solved_maze.keys():
        row=key[0]
        col=key[1]
        out[row][col]=solved_maze[key]
    for line in out:
        print(line)


def print_free_flow_file(width, height, solvedMaze, filename):
    output_maze = open(filename, 'w')
    printlist = []
    for x in range(width):
        for y in range(height):
            if (x, y) not in solvedMaze:
                printlist.append('_')
            else:
                printlist.append(solvedMaze[(x, y)])
    return output_maze.write(str(printlist))



if __name__ == "__main__":
    games = get_list_of_solved_files()
    for gameboard in games:
        name = get_name(gameboard)
        print(name)
        useful_array_board = input_to_array(gameboard)
        print('\n')
        height, width = puzzleDetails(useful_array_board)
        colorSet, colorDict = generateColorSet_Dict(useful_array_board)
        filename = 'Outputs/%s.txt' %name
        solvedMaze = print_free_flow_file(width, height, colorDict, filename)
        print("SolvedMaze:", solvedMaze)

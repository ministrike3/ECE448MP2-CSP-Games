#In this file write functions relating to File i/o
import glob

def get_list_of_test_files():
    return glob.glob("./Inputs/Test/*")

def get_list_of_smaller_files():
    return glob.glob("./Inputs/Smaller/*")

def get_list_of_smaller_files():
    return glob.glob("./Inputs/Bigger/*")

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

if __name__ == "__main__":
    games = get_list_of_test_files()
    for gameboard in games:
        name = get_name(gameboard)
        print(name)
        useful_array_board = input_to_array(gameboard)
        print(useful_array_board)
        print('\n')
        height, width = puzzleDetails(useful_array_board)
        print("height:", height, "width:", width)
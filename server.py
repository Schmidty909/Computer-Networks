import random

# Server side code for Admiral Acknownledgement
# To do:
# 1.) Rewrite code in C++
# 2.) Create board for both players.
# 3.) Receive player movement
#       b.) Verify player input is correct
# 4.) Receive player's torpedo

gridWidth = 10
gridLength = 10
gridOutline = 25

game_grid = []


def build_game_grid(array):
    for x in range(gridWidth):
        y_grid = []
        for y in range(gridLength):
            value = '0'
            if random.randrange(1, 11) == 10:
                value = '#'
            y_grid.append(value)
        array.append(y_grid)

    return array


def print_game_grid(array):
    for x in range(gridWidth):
        for y in range(gridLength):
            print(array[x][y], end="  ")
        print()


def main():
    build_game_grid(game_grid)
    print_game_grid(game_grid)


if __name__ == '__main__':
    main()

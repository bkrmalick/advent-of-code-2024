CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]


UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"
BLOCK = "#"

visited = {}


def _walk_until_blocked(grid: list) -> tuple[list, int]:
    print("BEFORE\n", "\n".join(["".join(row) for row in grid]))

    dimension = len(grid)
    
    new_grid = grid.copy()
    steps_taken = 0

    pos_x = None
    pos_y = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # print(cell)
            # import pdb;pdb.set_trace()
            if cell in [UP, RIGHT, DOWN, LEFT]:
                pos_x = x
                pos_y = y
                break
    
    try: 
        assert pos_x is not None and pos_y is not None, "No position found"
    except AssertionError as e:
        # print grid
        # print("\n".join(["".join(row) for row in grid]))
        raise

    # if (
    #     pos_x == 0
    #     or pos_x == dimension - 1
    #     or pos_y == 0
    #     or pos_y == dimension - 1
    # ):  
    #     print("FINAL POS", pos_x, pos_y)
    #     return new_grid, steps_taken

    if grid[pos_y][pos_x] == UP:
        print("UP")
        # print("BUP\n", "\n".join(["".join(row) for row in new_grid]))
        start = pos_y
        while True:

            start = start - 1

            if start < 0:
                new_grid[pos_y][pos_x] = "."

                new_grid[start + 1][pos_x] = UP
                return new_grid, 0
            elif grid[start][pos_x] == BLOCK:
                steps_taken = pos_y - start
                new_grid[pos_y][pos_x] = "."
                
                new_grid[start + 1][pos_x] = RIGHT
                # print("AUP\n", "\n".join(["".join(row) for row in new_grid]))
                break
            else:
                visited.update({(start, pos_x): True})

    elif grid[pos_y][pos_x] == DOWN:
        print("DOWN")
        start = pos_y
        while True:
            start = start + 1
            if start == dimension:
                new_grid[pos_y][pos_x] = "."

                new_grid[start - 1][pos_x] = DOWN
                return new_grid, 0
            elif grid[start][pos_x] == BLOCK:
                steps_taken = start - pos_y
                new_grid[pos_y][pos_x] = "."

                new_grid[start - 1][pos_x] = LEFT
                break
            else:
                visited.update({(start, pos_x): True})

    elif grid[pos_y][pos_x] == RIGHT:
        print("RIGHT")
        start = pos_x
        while True:
            start = start + 1
            if start == dimension:
                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start - 1] = RIGHT
                return new_grid, 0
            elif grid[pos_y][start] == BLOCK:
                steps_taken = start - pos_x

                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start - 1] = DOWN
                break
            else:
                visited.update({(pos_y, start): True})

    elif grid[pos_y][pos_x] == LEFT:
        print("LEFT")
        # print("BLEFT\n", "\n".join(["".join(row) for row in new_grid]))

        start = pos_x
        while True:
            start = start - 1
            if start < 0:
                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start + 1] = LEFT
                return new_grid, 0
            elif grid[pos_y][start] == BLOCK:
                steps_taken = pos_x - start
                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start + 1] = UP
                # print("ALEFT\n", "\n".join(["".join(row) for row in new_grid]))

                break
            else:
                visited.update({(pos_y, start): True})
    else:
        raise Exception("invalid char")

    print("AFTER1\n", "\n".join(["".join(row) for row in new_grid]))


    # if steps_taken != 0:
    #     new_grid[pos_y][pos_x] = "."

    print("AFTER2\n", "\n".join(["".join(row) for row in new_grid]))

    return new_grid, steps_taken


if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f'{CURRENT_FILE_NAME.replace("a", "").replace("b", "")}.txt', "r") as f:
        inp = f.readlines()

    grid = []
    for line in inp:
        grid.append([char for char in line if char != "\n"])

    total_steps = 0
    steps_taken = 0

    while True:
        print(total_steps)

        grid, steps_taken = _walk_until_blocked(grid)
        total_steps += steps_taken+1
        if steps_taken == 0:
            break

    # print(total_steps)

    
    # print X wherever visited
    for key in visited.keys():
        if grid[key[0]][key[1]] not in [UP, RIGHT, DOWN, LEFT]:
            grid[key[0]][key[1]] = "X"

    print("\n".join(["".join(row) for row in grid]))

    print(
    "Total visited unique cells: ",
    len(visited))

    

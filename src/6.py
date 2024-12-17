CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]


UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"
BLOCK = "#"

visited = {}


def _walk_until_blocked(grid: list) -> tuple[list, int, bool]:
    print("BEFORE")
    str_repr = "\n".join(["".join(row) for row in grid])
    print(str_repr)

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
                visited.update({(y, x): True})
                break

    assert pos_x is not None and pos_y is not None, "No position found"

    reached_edge = False

    if grid[pos_y][pos_x] == UP:
        print("UP")
        # print("BUP\n", "\n".join(["".join(row) for row in new_grid]))
        start = pos_y
        while True:

            start = start - 1

            if start < 0:
                steps_taken = pos_y - start

                new_grid[pos_y][pos_x] = "."

                new_grid[start + 1][pos_x] = UP

                reached_edge = True

                break
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
                steps_taken = start - pos_y

                new_grid[pos_y][pos_x] = "."

                new_grid[start - 1][pos_x] = DOWN
                reached_edge = True

                break
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
                steps_taken = start - pos_x

                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start - 1] = RIGHT
                reached_edge = True

                break
            elif grid[pos_y][start] == BLOCK:
                steps_taken = start - pos_x

                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start - 1] = DOWN
                break
            else:
                visited.update({(pos_y, start): True})

    elif grid[pos_y][pos_x] == LEFT:
        print("LEFT")
        start = pos_x
        while True:
            start = start - 1
            if start < 0:
                steps_taken = pos_x - start

                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start + 1] = LEFT
                reached_edge = True

                break
            elif grid[pos_y][start] == BLOCK:
                steps_taken = pos_x - start
                new_grid[pos_y][pos_x] = "."

                new_grid[pos_y][start + 1] = UP

                break
            else:
                visited.update({(pos_y, start): True})
    else:
        raise Exception("invalid char")

    str_repr = "\n".join(["".join(row) for row in new_grid])
    print(str_repr)

    return new_grid, steps_taken, reached_edge


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

        grid, steps_taken, end = _walk_until_blocked(grid)
        total_steps += steps_taken + 1
        if end:
            break

    # print X wherever visited
    for key in visited.keys():
        if grid[key[0]][key[1]] not in [UP, RIGHT, DOWN, LEFT]:
            grid[key[0]][key[1]] = "X"

    print("\n\n")
    print("\n".join(["".join(row) for row in grid]))

    print("Total visited unique cells: ", len(visited))

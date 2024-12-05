CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f"{CURRENT_FILE_NAME}.txt", "r") as f:
        inp = f.readlines()

    arr = []
    for line in inp:
        arr.append([c for c in line if c != "\n"])

    print(arr)

    def _safe_get(x, y):

        if x<0 or y<0:
            return ""

        try:
            return arr[x][y]
        except:
            return ""

    itt = lambda: range(1, 4)
    to_check = "MAS"

    def _check_horizontal(x, y, plus):
        str = ""
        for i in itt():
            str += _safe_get(x + i if plus else x - i, y)

        print(str)
        if str == to_check:
            return True
        return False

    def _check_vertical(x, y, plus):
        str = ""
        for i in itt():
            str += _safe_get(x, y + i if plus else y - i)

        if str == to_check:
            return True
        return False

    def _check_diagonal(x, y, plus, plus2):
        str = ""
        for i in itt():
            str += _safe_get(x + i if plus else x - i, y + i if plus2 else y - i)

        if str == to_check:
            return True
        return False

    times_found = 0
    import copy

    new_arr = copy.deepcopy(arr)
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            prev_times_found = times_found
            if _safe_get(x, y) == "X":
                if _check_horizontal(x, y, True):
                    times_found += 1
                if _check_horizontal(x, y, False):
                    times_found += 1
                if _check_vertical(x, y, True):
                    times_found += 1
                if _check_vertical(x, y, False):
                    times_found += 1
                if _check_diagonal(x, y, True, True):
                    times_found += 1
                if _check_diagonal(x, y, True, False):
                    times_found += 1
                if _check_diagonal(x, y, False, True):
                    times_found += 1
                if _check_diagonal(x, y, False, False):
                    times_found += 1

            if prev_times_found == times_found:
                new_arr[x][y] = "."
            else:
                new_arr[x][y] = str(times_found - prev_times_found)

    for x in new_arr:
        print(x)
    print(times_found)

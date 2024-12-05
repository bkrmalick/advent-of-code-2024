CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f'{CURRENT_FILE_NAME.replace("a", "").replace("b", "")}.txt', "r") as f:
        inp = f.readlines()

    arr = []
    for line in inp:
        arr.append([c for c in line if c != "\n"])

    print(arr)

    def _safe_get(x, y):

        if x < 0 or y < 0:
            return ""

        try:
            return arr[x][y]
        except:
            return ""


    times_found = 0
    import copy

    new_arr = copy.deepcopy(arr)
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            prev_times_found = times_found
            if _safe_get(x, y) == "A":
                ls = []
                ls.append(_safe_get(x - 1, y - 1))
                ls.append(_safe_get(x - 1, y + 1))
                ls.append(_safe_get(x + 1, y - 1))
                ls.append(_safe_get(x + 1, y + 1))


                if (
                    ls.count("M") == 2
                    and ls.count("S") == 2

                ):
                    gh= "".join(ls)

                    if gh not in [
                        "MSSM",
                        "SMMS",
                    ]:
                        print (gh)
                        times_found += 1

            if prev_times_found == times_found:
                new_arr[x][y] = "."
            else:
                new_arr[x][y] = str(times_found - prev_times_found)

    # for x in new_arr:
    #     print(x)
    print(times_found)

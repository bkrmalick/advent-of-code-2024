CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f"{CURRENT_FILE_NAME}.txt", "r") as f:
        inp = f.readlines()

    safe_counter = 0
    for line in inp:
        diffs = []
        prev = None
        mode = None

        is_safe = None

        for idx, c in enumerate(line.split()):
            if idx != 0:
                diffs.append(int(c) - prev)
            prev = int(c)

        is_safe = len([d for d in diffs if d in [1, 2, 3]]) == len(diffs) or len(
            [d for d in diffs if -1 * d in [1, 2, 3]]
        ) == len(diffs)

        if is_safe:
            print(diffs)
            safe_counter += 1

    print(safe_counter)

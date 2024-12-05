CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f'{CURRENT_FILE_NAME.replace("a", "").replace("b", "")}.txt', "r") as f:
        inp = f.readlines()

    rules = []
    pages = []

    def _is_safe(nums: list[int]):
        diffs = []
        prev = None

        for idx, c in enumerate(nums):
            if idx != 0:
                diffs.append(c - prev)
            prev = c

        all_positive = all([d > 0 for d in diffs])
        all_negative = all([d < 0 for d in diffs])

        if all_positive or all_negative:
            # print("maybe safe", nums, diffs)
            return all([abs(d) <= 3 for d in diffs])
        else:
            # print("unsafe", nums, diffs)
            return False

    c = 0
    for line in inp:
        nums = [int(x) for x in line.split()]

        if _is_safe(nums):
            c += 1
        else:
            for idx in range(len(nums)):
                new_nums = nums.copy()

                new_nums.pop(idx)
                if _is_safe(new_nums):
                    c += 1
                    break

    print(c)

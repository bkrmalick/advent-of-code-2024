CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f"{CURRENT_FILE_NAME}.txt", "r") as f:
        inp = f.readlines()

    concat_lines = "".join(inp)

    so_far = ""
    wait_for = None
    substr = ""
    val = 0
    enabled = True
    for idx, chara in enumerate(concat_lines):
        if so_far.endswith("do()"):
            enabled = True
        elif so_far.endswith("don't()"):
            enabled = False

        if wait_for is None and so_far.endswith("mul"):
            wait_for = ")"  
        elif wait_for:
            if chara == ")":
                parts = substr.split(",")
                if len(parts) > 1:
                    x = parts[0]
                    y = parts[1]

                    # print("x", x)
                    # print("y", y)
                    if enabled:
                        val += int(x) * int(y)

                wait_for = None

                substr = ""
            elif chara == "," or chara.isdigit():
                substr += chara
            else:
                substr = ""
                wait_for = None

        so_far += chara

    print(val)

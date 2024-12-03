
CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f"{CURRENT_FILE_NAME}.txt", "r") as f:
        inp = f.readlines()

    for line in inp:
        vals = line.split("   ")
        ls_1.append(vals[0])
        ls_2.append(vals[1])
    
    sum = 0
    for x,y in zip(sorted(ls_1), sorted(ls_2)):
        sum += abs(int(x) - int(y))
    
    print(sum)

    sim = 0
    for x in ls_1:
        # print(x)
        c = len([y for y in ls_2 if int(y) == int(x)])
        # print(c)
        sim = sim + (int(x)*c)

    print(sim)

    
    
CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

def most_common(lst):
    return max(set(lst), key=lst.count)

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f"{CURRENT_FILE_NAME}.txt", "r") as f:
        inp = f.readlines()

    safe_counter = 0
    safe_counter_damp = 0
    for line in inp:
        diffs = []
        prev = None
        mode = None

        for idx, c in enumerate(line.split()):
            if idx != 0:
                diffs.append(int(c) - prev)
            prev = int(c)

        is_safe = len([d for d in diffs if d in [1, 2, 3]]) == len(diffs) or len(
            [d for d in diffs if -1 * d in [1, 2, 3]]
        ) == len(diffs)

        is_safe_damp = (
            len(diffs) - len([d for d in diffs if d in [1, 2, 3]])
        ) <= 1 or (len(diffs) - len([d for d in diffs if -1 * d in [1, 2, 3]]) <= 1)

        if is_safe:
            # print(diffs)
            safe_counter += 1
        
        if is_safe_damp:
            ls =[int(x) for x in line.split()]
            new_ls = []
            mode = "inc" if diffs[0] > 0 else "dec" if diffs[0] < 0 else ""


            if diffs[0] == 0:
                mode = ""
            else:
                mode = most_common([x>0 for x in diffs])
                mode = "inc" if mode else "dec"
                

            for idx, x in enumerate(ls):
                if idx == 0 and mode == "":
                    new_ls.extend(ls[idx+1:])
                    break

                if idx != 0:
                    diff = x - ls[idx-1] 

                    if mode == "inc" and diff <=0:
                        new_ls.extend(ls[idx+1:])
                        break
                    
                    elif mode == "dec" and diff >=0:
                        new_ls.extend(ls[idx+1:])
                        break

                    elif abs(diff) not in [1,2,3]:
                        new_ls.extend(ls[idx+1:])
                        break

                new_ls.append(x)
            



            # assert len(new_ls) == len(ls) -1, f"{new_ls} - {ls} - {diffs} - {mode}"

            # still_safe = len(new_ls) == len(ls) -1
            diff = None
            still_safe = True
            
            if ( len(ls) - len(new_ls) ) == 1:
                for idx, x in enumerate(new_ls):

                    if idx != 0:
                        diff = x - new_ls[idx-1] 

                        if mode == "inc" and diff <=0:
                            still_safe = False
                            break
                        
                        if mode == "dec" and diff >=0:
                            still_safe = False
                            break

                        if abs(diff) not in [1,2,3]:
                            still_safe = False
                            break
                
            print(f"{ls} - {mode} - {new_ls} - {still_safe}")           
            if still_safe:
                safe_counter_damp += 1

    print(safe_counter)
    print(safe_counter_damp)

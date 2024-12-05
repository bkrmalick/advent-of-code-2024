CURRENT_FILE_NAME = __file__.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    ls_1 = []
    ls_2 = []

    with open(f'{CURRENT_FILE_NAME.replace("a", "").replace("b", "")}.txt', "r") as f:
        inp = f.readlines()

    rules = []
    pages = []

    break_found = False
    for line in inp:
        if line == "\n":
            break_found = True
            continue
        
        if break_found:
            pages.append(line.strip())   
        else:
            rules.append(line.strip())

    print(rules)
    print("----------------------")
    print(pages)
    print("----------------------")


    def _validate_rule(rule, page_nums):
        x, y = rule.split("|")  
        x= int(x)
        y = int(y)


       
        
        try:
            x_ind = page_nums.index(x)
            y_ind = page_nums.index(y)
        except ValueError:
            return True

        return x_ind < y_ind
    

    def _fix_page(rule, page_nums):
        x, y = rule.split("|")  
        x= int(x)
        y = int(y)


       
        
        try:
            x_ind = page_nums.index(x)
            y_ind = page_nums.index(y)
        except ValueError:
            return page_nums, False
        
        if x_ind < y_ind:
            return page_nums, False
        else:
            tmp = page_nums[x_ind]
            page_nums[x_ind] = page_nums[y_ind]
            page_nums[y_ind] = tmp
            return page_nums, True

    
    valid_total = 0
    invalid_total = 0
    for p in pages:
        page_nums = [int(num) for num in p.split(",")]

        is_valid = True
        for rule in rules:
            if not _validate_rule(rule, page_nums):
                is_valid = False
                break
        
        mid_index = len(page_nums) // 2

        if is_valid:
            print("valid page", page_nums)
            valid_total += page_nums[mid_index]
        else:
            print("invalid page", page_nums)
            new_page = page_nums.copy()

            prev_page = None
            updated = True
            while updated:
                updated = False

                for rule in rules:

                    new_page, updated=  _fix_page(
                        rule,
                        new_page
                    )
                    assert _validate_rule(rule, new_page)

                    if updated:
                        break

            mid_val = new_page[mid_index]
            print("mid val", mid_val)

            invalid_total += mid_val
            

    print(valid_total)
    print(invalid_total)    
    

            


    

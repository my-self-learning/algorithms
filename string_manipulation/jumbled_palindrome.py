# itinn


def palin_check(str_lst):
    count = 0
    str_len = len(str_lst)
    pointer, temp, last_index = 0, str_len-1, str_len-1
    while(temp > pointer):
        cur_chr = str_lst[pointer]
        if (temp - pointer == 1):
            str_lst[pointer], str_lst[temp] = str_lst[temp], str_lst[pointer]
            count += 1
            temp = last_index
            continue
        if (str_lst[temp] == cur_chr):
            str_lst[temp], str_lst[last_index] = str_lst[last_index], str_lst[temp]
            count += 1
            pointer += 1
            last_index -= 1
            temp = last_index
        else:
            temp -= 1
    print("".join(str_lst))
    print(count)

palin_check(list('itntntssi'))
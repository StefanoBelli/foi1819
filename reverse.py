def reverse(lst):
    new_lst = list()
    lstlen = len(lst) - 1

    for idx in range(lstlen):
        new_lst.append(lst[lstlen - idx])

    return new_lst

more_things = [1,2,3,4]

print(reverse(more_things))

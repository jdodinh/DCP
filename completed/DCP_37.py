"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

#####################################################


def find_power_set(lst):
    new_set = []
    if len(lst) == 1:
        new_set.append(lst)                     # If list length is 1, we return the list in a list
        return new_set                              
    for i in range(len(lst)):                   # for all elements in that list, we find powersets of
        lst_cpy = lst.copy()                    # the list with the element removed, and then add it
        el = lst[i]                             # to the powerset, along with each element combined with
        lst_cpy.remove(el)                      # the element that has been removed.
        pw_sub_st = find_power_set(lst_cpy)
        for e in pw_sub_st:
            exp = e + [el]
            exp.sort()
            e.sort()
            if e not in new_set:
                new_set.append(e)
            if exp not in new_set:
                new_set.append(exp)
    return new_set


def main():
    main_set = {1, 2, 3}
    main_set = list(main_set)
    print(main_set)
    pwst = find_power_set(main_set)             # recursive function call to find power set of given set
    pwst.append([])                             # add the empty set
    pwst.sort(key=len)                          # sort based on subset length
    print(pwst)


if __name__ == '__main__':
    main()

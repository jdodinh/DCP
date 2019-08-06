"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the
list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

    2
    1.5
    2
    3.5
    2
    2
    2

"""


og_list = [2, 1, 5, 7, 2, 0, 5]                                 # example list


def median(lst):                                                # function that finds median of a given list.
    length = len(lst)
    lst.sort()
    if length % 2 == 0:                                 
        return (lst[int(length/2)] + lst[int(length/2) - 1])/2  # return average of middle two elements, is list length is even
    else:
        return lst[int(length/2)]                               # return middle element is list length is odd


def main():
    for i in range(1, len(og_list)+1):                          # print out the medians of the slices of the original list, as the
        print(median(og_list[:i]))                              # length increases


if __name__ == "__main__":
    main()

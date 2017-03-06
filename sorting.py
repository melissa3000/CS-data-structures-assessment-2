#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    result_lst = []
    list1_index = 0
    list2_index = 0
    result_index = 0

#Neither of these worked without throwing an index out of order range and I ran
# out of time to figure it out

    # while list1_index < len(list1) and list2_index < len(list2):
    #     if list1[list1_index] < list2[list2_index]:
    #         result_lst[result_index] = list1[list1_index]
    #         list1_index += 1
    #     else:
    #         result_lst[result_index] = list2[list2_index]
    #         list2_index += 1
    #     result_index += 1


    # while len(list1) > 0 or len(list2) > 0:
        # if list1 == []:
        #     result_lst.append(list2.pop(0))
        # if list2 == []:
        #     result_lst.append(list1.pop(0))
        # if list1[0] < list2[0]:
        #     result_lst.append(list1.pop(0))
        # else:
        #     result_lst.append(list2.pop(0))

    print result_lst


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    # pivot = len(lst) / 2
    # list1 = lst[:pivot]
    # list2 = lst[pivot:]

    # # base case = []

    # merge_sort(list1)
    # merge_sort(list2)

    # Although I understood this in lecture and study hall,
    # I discovered I don't understand this well enough to reproduce it.
    # I know I could copy the code from the demo, but don't want to do that.
    # I ran out of time before the deadline to figure it out, but will spend the
    # evenings this week going through the code and the further study resources
    # until I can recreate this on my own.

    pass

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

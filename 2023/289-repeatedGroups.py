def repeatedGroups(lst):
    """Given a list of numbers, return all groups
    of repeating consecutive numbers.


    The function works by iterating over the input
    list, keeping track of the current group of
    consecutive numbers. If the current number is
    the same as the previous number, it is added to
    the current group. If the current number is
    different from the previous number, the current
    group is finished and added to the list of groups,
    and a new current group is started with the current
    number.

    Finally, if there is a current group when the
    iteration is finished, it is also added to the list
    of groups.
    """
    groups = []
    current_group = []

    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i - 1]:
            if len(current_group) > 1:
                groups.append(current_group)
            current_group = [lst[i]]
        else:
            current_group.append(lst[i])

    if len(current_group) > 1:
        groups.append(current_group)

    return groups


if __name__ == "__main__":
    nums = [1, 2, 2, 4, 5]
    # [[2, 2]]
    print(repeatedGroups(nums))
    nums2 = [1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9]
    print(repeatedGroups(nums2))
    # [[1, 1], [0, 0], [4, 4, 4], [9, 9]]

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

    Time complexity: O(n)
    Space complexity: O(n)
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


def repeatedGroups_two_pointers(nums):
    """Given a list of numbers, return all groups
    of repeating consecutive numbers.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    result = []
    pointer_l = pointer_r = 0

    while pointer_l < len(nums) - 1:
        if nums[pointer_l] == nums[pointer_l + 1]:
            aux = []
            aux.append(nums[pointer_l])
            pointer_r = pointer_l + 1
            while nums[pointer_l] == nums[pointer_r]:
                pointer_r += 1
                aux.append(nums[pointer_l])
                if pointer_r == len(nums):
                    break
            pointer_l = pointer_r
            result.append(aux)
        else:
            pointer_l += 1
    return result


def repeatedGroups_recursion(nums):
    """Given a list of numbers, return all groups
    of repeating consecutive numbers.

    Using recursion to solve this problem.
    """
    # base case
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return []
    elif len(nums) == 2:
        if nums[0] == nums[1]:
            return [[nums[0], nums[1]]]
        else:
            return []

    # recursive case
    else:
        if nums[0] == nums[1]:
            current_group = []
            current_group.append(nums[0])
            pointer_r = 1
            while nums[0] == nums[pointer_r]:
                pointer_r += 1
                current_group.append(nums[0])
                if pointer_r == len(nums) - 1:
                    break
            return [current_group] + repeatedGroups_recursion(nums[pointer_r:])
        else:
            return repeatedGroups_recursion(nums[1:])


if __name__ == "__main__":
    nums = [1, 2, 2, 4, 5]
    # [[2, 2]]
    print(repeatedGroups_recursion(nums))
    nums2 = [1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9]
    print(repeatedGroups_recursion(nums2))
    # [[1, 1], [0, 0], [4, 4, 4], [9, 9]]

# Name: Raul Preciado
# OSU Email: preciadr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1 - Python Fundamentals Review
# Due Date: 10/23/2023
# Description: This program contains a total of 10 different functions all with the purpose of writing algorithms that
#  work on Static Arrays and are efficient - O(n) with the exception of count_sort which is O(n + k).


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    Takes a StaticArray as a parameter and outputs a tuple with the min as
     the first value and max as the second value
    """
    max = arr.get(0)
    min = max

    for i in range(arr.length()):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

    return min, max


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Takes a StaticArray as a parameter and returns a second StaticArray object in which the string 'fizz'
    replaces all numbers divisible by 3, 'buzz' replaces all numbers divisible by 5 and 'fizzbuzz' replaces
    all numbers divisible by 3 and 5.
    """
    new_arr = StaticArray(arr.length())

    for i in range(arr.length()):

        num = arr.get(i)

        if (num % 3 == 0) and (num % 5 == 0):
            new_arr.set(i, 'fizzbuzz')

        elif (num % 3 == 0) and (num % 5 != 0):
            new_arr.set(i, 'fizz')

        elif (num % 5 == 0) and (num % 3 != 0):
            new_arr.set(i, 'buzz')

        elif (num % 3 != 0) and (num % 5 != 0):
            new_arr.set(i, num)

    return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Takes a StaticArray object as a parameter and reverses the order of the original StaticArray
    """
    counter = 0
    length = arr.length()

    # The while loop only needs to iterate through the first half of the array since it is swapping
    # the values that are equidistant from the center at each iteration

    while counter < length // 2:
        temp = arr.get(counter)
        arr.set(counter, arr.get(length - 1 - counter))
        arr.set(length - 1 - counter, temp)
        counter += 1


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Takes a StaticArray object and an integer as parameters and returns a new array with each value's index shifted
    right or left depending on the integer representing steps.
    """
    new_arr = StaticArray(arr.length())
    length = arr.length()

    # Takes the absolute value of the steps and if it is greater than the length of the array, it reduces it
    # to a lower number but equivalent in terms of the wrap around effect
    if ((steps ** 2) ** 0.5) >= length:
        steps = steps % length

    for i in range(length):
        # the variable 'assigned' acts as an indicator that the index in question has been assigned a place
        # in the new array. This is a workaround for using continue.
        assigned = False

        if assigned is False and i + steps > length - 1:
            new_i = i + steps - length
            new_arr.set(new_i, arr[i])
            assigned = True

            # after a condition is met to assign another value in the array, we change the assigned value to True to
            # maintain a single assignment per i

        if assigned is False and i + steps < 0:
            new_i = length + (i + steps)
            new_arr.set(new_i, arr[i])
            assigned = True

        if assigned is False:
            new_arr.set(i + steps, arr[i])

    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Takes two integers as parameters and returns a StaticArray with all integers between and including
    start and stop.
    """
    temp_start = start
    arr_size = 1

    if start == end:
        arr = StaticArray(1)
        arr.set(0, start)
        return arr

    while temp_start != end:
        if temp_start < end:
            arr_size += 1
            temp_start += 1
        if temp_start > end:
            arr_size += 1
            temp_start -= 1

    arr = StaticArray(arr_size)
    temp_start = start

    for i in range(arr_size):
        if start < end:
            arr.set(i, temp_start)
            temp_start += 1

        if start > end:
            arr.set(i, temp_start)
            temp_start -= 1

    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
def is_sorted(arr: StaticArray) -> int:
    """
    Takes a StaticArray object as a parameter and returns a value describing how the array is sorted.
    1 : the array is sorted in strictly ascending order
    -1: the array is sorted in strictly descending order
    0: otherwise (not strictly sorted in any direction)
    """
    length = arr.length()

    if length == 1:
        return 1

    val = arr.get(0)

    # once the ascend/descend boolean expressions are set, they must remain unchanged and True or else a 0 will return
    if val > arr[1]:
        descend = True
        ascend = False

    if val < arr[1]:
        ascend = True
        descend = False

    for i in range(1, length):
        next_val = arr[i]

        if val == next_val:
            return 0
        # each comparison checks to see if the ascend/descend values are consistent with the comparison
        if val > next_val:
            if descend is False:
                return 0
            val = arr[i]
            ascend = False

        if val < next_val:
            if ascend is False:
                return 0
            val = arr[i]
            descend = False

    if ascend and not descend:
        return 1
    if descend and not ascend:
        return -1

    return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Takes a sorted array as a parameter and returns a tuple consisting of the mode of the array as the first value
    and the number of times that element appears within the array. It is not restricted to integers.
    """
    # Since the array is sorted, it is possible to traverse through the array keeping track of the item and count
    # and comparing it to each new value and count. When a new high count is reached, the second value and count are
    # zeroed out.
    length = arr.length()
    temp_a = arr[0]
    temp_b = temp_a
    temp_a_count = 0
    temp_b_count = 0

    for i in range(length):
        temp_val = arr[i]

        if temp_a == temp_val:
            temp_a_count += 1

        if temp_a != temp_val and temp_b == temp_val:
            temp_b_count += 1

        if temp_a != temp_val and temp_b != temp_val:
            temp_b = temp_val
            temp_b_count = 0
            temp_b_count += 1

        if temp_b_count > temp_a_count:
            temp_a = temp_b
            temp_a_count = temp_b_count

    return temp_a, temp_a_count


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Takes a sorted Array and returns a new array that is sorted in the same way and
    with all the duplicates removed.
    """
    length = arr.length()
    last_val = arr[0]
    duplicates = 0

    # the for loop below iterates once through the array to count how many duplicates exist in the array
    for i in range(1, length):
        curr_val = arr[i]
        if curr_val == last_val:
            duplicates += 1
        last_val = curr_val

    new_length = length - duplicates
    new_arr = StaticArray(new_length)
    new_arr[0] = arr[0]
    last_val = arr[0]
    new_index = 1
    for i in range(1, length):
        # the expression ' arr[i] != last_val is responsible for ensuring duplicates are left out
        if new_index < new_length and arr[i] != last_val:
            current_val = arr[i]
            new_arr[new_index] = current_val
            last_val = current_val
            new_index += 1

    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Takes a StaticArray object as a parameter and
    """
    length = arr.length()
    minmax = min_max(arr)
    abs_min = abs(minmax[0])
    # helper_range helps get the length of the range of values
    helper_range = sa_range(minmax[0], minmax[1])
    # each index in count_range corresponds to its value in the array. The value that each index accumulates corresponds
    # to the number of times that number appears in the array.
    count_range = StaticArray(helper_range.length() + 1)
    count_range_length = count_range.length()
    result = StaticArray(length)

    # the for loop below accounts for how negative values are handled in the count_range array since negative indexes
    # don't exist in the StaticArray objects
    for i in range(length):
        value = arr[i]
        if minmax[0] < 0:
            index = value + abs_min
        if minmax[0] > 0:
            index = value - abs_min

        if count_range[index] is None:
            count_range[index] = 0
        count_range[index] += 1

    # real_index is the starting index for populating the new Array
    real_index = length - 1

    for i in range(count_range_length - 1):
        # A None value indicates that the number didn't occur at all in the array, so we skip it.
        if count_range[i] is None:
            continue

        freq = count_range[i]
        if minmax[0] < 0:
            value = i - abs_min
        if minmax[0] > 0:
            value = i + abs_min

        # this while loop adds the value at hand to the new array for as many times as was listed in the count_range val
        while freq > 0:
            result[real_index] = value
            real_index -= 1
            freq -= 1

    return result


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def min_max_helper(arr: StaticArray) -> tuple[int, int]:
    """
    Takes a StaticArray as a parameter and outputs a tuple with the absolute min as the first value,
    the absolute max as the second value and the index of the absolute min as the third value
    """
    max = arr.get(0)
    min = max
    min_ind = 0

    for i in range(arr.length()):
        if abs(arr[i]) > abs(max):
            max = arr[i]
        if abs(arr[i]) < abs(min):
            min = arr[i]
            min_ind = i

    return min, max, int(min_ind)

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Takes a sorted array as a parameter and returns a new array with the sorted values of the squares
    of the original array
    """
    length = arr.length()
    new_array = StaticArray(length)
    min_max_help = min_max_helper(arr)
    min_index = min_max_help[2]
    working_array = StaticArray(length)

    for i in range(length):
        working_array[i] = arr[i]

    if min_index == length - 1:
        reverse(working_array)
        min_max_help = min_max_helper(working_array)
        min_index = min_max_help[2]

    if min_index == 0:
        for i in range(length):
            new_array[i] = working_array[i] ** 2
        return new_array
    # left will be the index for the value to the left of the starting point
    # right will be the index for the right value
    left = min_index - 1
    right = min_index + 1
    # count will serve as the next index in the new array that needs to be filled.
    count = 0
    new_array[count] = working_array[min_index] ** 2
    count += 1

    # This algorithm works by starting from the index of the smallest absolute value and comparing the numbers to left
    # and the right to see which number gets inserted next.

    while left >= 0 and right <= length - 1:
        right_val = working_array[right]
        left_val = working_array[left]

        if abs(left_val) <= abs(right_val):
            new_array[count] = left_val ** 2
            left -= 1
            count += 1
        if abs(left_val) > abs(right_val):
            new_array[count] = right_val ** 2
            right += 1
            count += 1
    # if we reach the end point of the array on the right side
    while left >= 0 and right > length - 1:
        left_val = working_array[left]
        new_array[count] = left_val ** 2
        left -= 1
        count += 1
    # if we reach the end point of the array on the left side
    while left <= 0 and right < length - 1:
        right_val = working_array[right]
        new_array[count] = right_val ** 2
        count += 1
        right += 1
    # if for some reason the last index doesn't get filled
    if new_array[length - 1] is None:
        new_array[count] = min_max_help[1] ** 2

    return new_array

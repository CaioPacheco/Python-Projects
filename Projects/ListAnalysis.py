#Functions for a basic analysis of a list of numbers, probably not the best ways to do it but it works.

import random
import time

def generate_random_list(n=10, min=1, max=100):
    # Generates a list of n random integers between 1 and 100.
    try:
        random_list = []
        for i in range(n):
            random_list.append(random.randint(min, max))
        return random_list
    except ValueError as e:
        print(f"An error occurred: {e}")


def find_max(lst):
    # Returns the maximum value in a list.
    try:
        max_val = lst[0]
        for val in lst:
            if val > max_val:
                max_val = val
        return max_val
    except IndexError as e:
        print(f"An error occurred: {e}")


def find_min(lst):
    # Returns the minimum value in a list.
    try:
        min_val = lst[0]
        for val in lst:
            if val < min_val:
                min_val = val
        return min_val
    except IndexError as e:
        print(f"An error occurred: {e}")


def find_average(lst):
    # Returns the average value of a list.
    try:
        total = 0
        for val in lst:
            total += val
        return total / len(lst)
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")


def find_median(lst):
    # Returns the median value of a list.
    try:
        lst.sort()
        if len(lst) % 2 == 0:
            return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
        else:
            return lst[len(lst) // 2]
    except IndexError as e:
        print(f"An error occurred: {e}")


def find_mode(lst):
    # Returns the mode value of a list.
    try:
        count_dict = {}
        for val in lst:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1
        max_val = max(count_dict.values())
        modes = []
        for key, val in count_dict.items():
            if val == max_val:
                modes.append(key)
        return modes
    except ValueError as e:
        print(f"An error occurred: {e}")


def find_range(lst):
    # Returns the range of a list.
    try:
        return find_max(lst) - find_min(lst)
    except TypeError as e:
        print(f"An error occurred: {e}")


def analyze_list(lst):
    # Prints various statistics of a list.
    try:
        start_time = time.time()
        print("Maximum value:", find_max(lst))
        print("Minimum value:", find_min(lst))
        print("Average value:", find_average(lst))
        print("Median value:", find_median(lst))
        print("Mode value:", find_mode(lst))
        print("Range:", find_range(lst))
        end_time = time.time()
        print("Time taken to process:", end_time - start_time, "seconds")
    except Exception as e:
        print(f"An error occurred: {e}")
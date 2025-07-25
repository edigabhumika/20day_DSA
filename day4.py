"""
Day 4 – Python DSA Practice

Topics:
1. Count digits using recursion
2. Sum of digits using recursion
3. Find min and max in a list using recursion
"""

def count_digits(n):
    """Counts the number of digits in an integer using recursion."""
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def sum_digits(n):
    """Returns the sum of digits in an integer using recursion."""
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

def find_min(lst):
    """Finds the minimum value in a list using recursion."""
    if len(lst) == 1:
        return lst[0]
    rest_min = find_min(lst[1:])
    return lst[0] if lst[0] < rest_min else rest_min

def find_min_max(lst):
    """Finds both the minimum and maximum values in a list using recursion."""
    def rec(nums, i):
        if i == len(nums) - 1:
            return nums[i], nums[i]
        curr_min, curr_max = rec(nums, i + 1)
        curr_min = curr_min if curr_min < nums[i] else nums[i]
        curr_max = curr_max if curr_max > nums[i] else nums[i]
        return curr_min, curr_max
    return rec(lst, 0)

# Example usage
if __name__ == "__main__":
    print("Count digits in 123:", count_digits(123))
    print("Sum of digits in 123:", sum_digits(123))

    numbers = [5, 2, 9, 1, 7, 0]
    print("Minimum value:", find_min(numbers))

    nums = [5, 32, 1, 9, 2]
    min_val, max_val = find_min_max(nums)
    print("Min and Max:", min_val, max_val)

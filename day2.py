"""
Day 2 – Python DSA Practice

Topics:
1. Find missing number using sum formula
2. Recursive Fibonacci sequence
3. Find missing numbers in a sequence
4. Move all zeros to the end of a list (recursive and iterative)
5. Rearrange list to move even numbers to the end
"""

def find_missing_number(nums):
    """Find a single missing number from a list containing 1 to n."""
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def fibonacci(n):
    """Return nth Fibonacci number using recursion."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def find_all_missing_numbers(seq):
    """Prints all missing numbers between the first and last elements."""
    missing = [i for i in range(seq[0], seq[-1]) if i not in seq]
    print("Missing numbers:", missing)

def move_zeros_recursive(nums):
    """Moves all zeros to the end using recursion."""
    if not nums:
        return []
    if nums[0] == 0:
        return move_zeros_recursive(nums[1:]) + [0]
    return [nums[0]] + move_zeros_recursive(nums[1:])

def move_zeros_iterative(nums):
    """Moves all zeros to the end using iterative approach."""
    result = [i for i in nums if i != 0]
    zero_count = nums.count(0)
    result.extend([0] * zero_count)
    return result

def move_evens_to_end(lst):
    """
    Moves all even numbers to the end of the list.
    Uses in-place mutation via pop and append.
    """
    i = 0
    count = len(lst)
    for _ in range(count):
        if lst[i] % 2 == 0:
            lst.append(lst.pop(i))
        else:
            i += 1
    return lst

# Example calls for testing
if __name__ == "__main__":
    print("Missing number (sum formula):", find_missing_number([1, 2, 3, 5, 6]))
    print("5th Fibonacci number:", fibonacci(5))

    print("Finding all missing in [1,2,3,6]:")
    find_all_missing_numbers([1, 2, 3, 6])

    print("Move zeros recursively:", move_zeros_recursive([2, 0, 5, 0, 7, 0, 3]))
    print("Move zeros iteratively:", move_zeros_iterative([2, 0, 5, 0, 7, 0, 3]))

    print("Move evens to end:", move_evens_to_end([1, 3, 6, 4, 5, 8]))

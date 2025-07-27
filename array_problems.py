"""
Array Problems – Multiple Approaches

Includes:
1. Two Sum – Brute Force, Hash Map, Two Pointers
2. Three Sum – Brute Force, Hashing, Two Pointers
3. Majority Element – More than n/2 and n/3
"""

# -------------------------------
# TWO SUM METHODS
# -------------------------------

def two_sum_brute_force(nums, target):
    """O(N^2) brute force approach."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def two_sum_hash_map(nums, target):
    """O(N) using hash map."""
    d = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [i, d[diff]]
        d[num] = i
    return None

def two_sum_two_pointers(nums, target):
    """O(N) using two pointers (for sorted array)."""
    nums.sort()
    low, high = 0, len(nums) - 1
    while low < high:
        total = nums[low] + nums[high]
        if total == target:
            return [nums[low], nums[high]]
        elif total < target:
            low += 1
        else:
            high -= 1
    return None

# -------------------------------
# THREE SUM METHODS
# -------------------------------

def three_sum_brute_force(nums):
    """O(N^3) approach to find triplets with sum 0."""
    n = len(nums)
    triplets = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    return [list(t) for t in triplets]

def three_sum_hashing(nums):
    """O(N^2) approach using hashing."""
    n = len(nums)
    triplets = set()
    for i in range(n - 1):
        seen = set()
        for j in range(i + 1, n):
            complement = -(nums[i] + nums[j])
            if complement in seen:
                triplet = tuple(sorted([nums[i], nums[j], complement]))
                triplets.add(triplet)
            seen.add(nums[j])
    return [list(t) for t in triplets]

def three_sum_two_pointers(nums):
    """O(N^2) optimized approach for sorted array."""
    nums.sort()
    n = len(nums)
    triplets = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return triplets

# -------------------------------
# MAJORITY ELEMENT
# -------------------------------

def majority_element_n_by_2(nums):
    """Finds element appearing more than n/2 times."""
    freq = {}
    n = len(nums)
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for key, val in freq.items():
        if val > n // 2:
            return key
    return None

def majority_element_n_by_3(nums):
    """Finds all elements appearing more than n/3 times."""
    freq = {}
    n = len(nums)
    result = []
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for key, val in freq.items():
        if val > n // 3:
            result.append(key)
    return result

# -------------------------------
# MAIN TEST CASES
# -------------------------------

if __name__ == "__main__":
    nums = [1, 2, 3, 0, 0]
    target = 5
    print("Two Sum (Brute):", two_sum_brute_force(nums, target))
    print("Two Sum (Hash Map):", two_sum_hash_map(nums, target))
    print("Two Sum (Two Pointers):", two_sum_two_pointers(nums, target))

    nums_3sum = [-1, 0, 1, 2, -1, -4]
    print("Three Sum (Brute):", three_sum_brute_force(nums_3sum))
    print("Three Sum (Hashing):", three_sum_hashing(nums_3sum))
    print("Three Sum (Two Pointers):", three_sum_two_pointers(nums_3sum))

    majority = [1, 1, 3, 4, 4, 4, 4, 4]
    print("Majority Element > n/2:", majority_element_n_by_2(majority))
    print("Majority Elements > n/3:", majority_element_n_by_3(majority))

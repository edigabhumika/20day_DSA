# day7.py

# ------------------------
# Bubble Sort (bubblesort.py)
# ------------------------
def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
print("Bubble Sort:")
arr = list(map(int, input("Enter numbers for bubble sort: ").split()))
print("Sorted:", bubble_sort(arr))


# ------------------------
# Merge Sort (mergesort.py)
# ------------------------
def mergesort(arr, n):
    def ms(arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        ms(arr, low, mid)
        ms(arr, mid + 1, high)
        merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        i = low
        j = mid + 1
        k = []

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                k.append(arr[i])
                i += 1
            else:
                k.append(arr[j])
                j += 1

        while i <= mid:
            k.append(arr[i])
            i += 1

        while j <= high:
            k.append(arr[j])
            j += 1

        for ind, val in enumerate(k):
            arr[low + ind] = val

    low = 0
    high = n - 1
    ms(arr, low, high)
    return arr

# Example usage:
print("\nMerge Sort:")
arr = list(map(int, input("Enter numbers for merge sort: ").split()))
n = len(arr)
print("Sorted:", mergesort(arr, n))


# ------------------------
# Merging Two Sorted Arrays (sort.py)
# ------------------------
print("\nMerge Two Sorted Arrays:")
nums1 = list(map(int, input("Enter sorted list 1: ").split()))
nums2 = list(map(int, input("Enter sorted list 2: ").split()))
i = 0
j = 0
result = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        result.append(nums1[i])
        i += 1
    else:
        result.append(nums2[j])
        j += 1
while i < len(nums1):
    result.append(nums1[i])
    i += 1
while j < len(nums2):
    result.append(nums2[j])
    j += 1
print("Merged Result:", result)

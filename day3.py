"""
Day 3 – Python DSA Practice

Topics:
1. Binary to Decimal Conversion
2. Bit Manipulation:
   - Count of set bits
   - Count of unset bits
   - Count of trailing set bits
   - Set a bit at a specific position
   - Check if a bit is set
"""

def binary_to_decimal(binary_str):
    """Converts a binary string to decimal."""
    num = 0
    power = 0
    for digit in reversed(binary_str):
        num += int(digit) * (2 ** power)
        power += 1
    return num

def count_set_bits(n):
    """Counts number of 1s in the binary representation of n."""
    count = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count

def count_unset_bits(n):
    """Counts number of 0s in the binary representation of n until all bits are shifted out."""
    count = 0
    while n:
        if not (n & 1):
            count += 1
        n >>= 1
    return count

def count_trailing_set_bits(n):
    """Counts number of trailing 1s in the binary representation."""
    count = 0
    while n & 1:
        count += 1
        n >>= 1
    return count

def set_bit(n, i):
    """Sets the ith bit of number n."""
    mask = 1 << i
    return n | mask

def is_bit_set(n, i):
    """Checks if the ith bit is set in number n."""
    mask = 1 << i
    return (n & mask) > 0

# Example calls for testing
if __name__ == "__main__":
    print("Binary to Decimal (101):", binary_to_decimal("101"))
    print("Set bits in 9:", count_set_bits(9))
    print("Unset bits in 8:", count_unset_bits(8))
    print("Trailing set bits in 3:", count_trailing_set_bits(3))
    print("Set 2nd bit in 8:", set_bit(8, 2))
    print("Is 2nd bit set in 8:", is_bit_set(8, 2))

"""
Day 1 – Python DSA Practice

Topics:
1. Unique number in a list
2. Prime number check
3. Vowel count
4. Sum of character positions (A=1, B=2, ...)
5. Vowel capitalization
6. Toggle case of string
7. Interleave two strings with uppercased remainder
8. Check if one string is a rotation of another
9. Pattern string expansion: e.g., "3a4b" → "aaabbbb"
"""

def unique_numbers(lst):
    """Prints numbers that appear only once in the list."""
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count == 1:
            print(num)

def is_prime(n):
    """Checks if a number is prime."""
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def count_vowels(s):
    """Counts vowels in a string."""
    return sum(1 for ch in s if ch in 'aeiou')

def alphabet_position_sum(s):
    """Returns the sum of positions of uppercase letters (A=1 to Z=26)."""
    return sum(1 + ord(ch) - 65 for ch in s if 'A' <= ch <= 'Z')

def capitalize_vowels(s):
    """Capitalizes all vowels in the string."""
    return ''.join(chr(ord(ch) - 32) if ch in 'aeiou' else ch for ch in s)

def toggle_case(s):
    """Toggles the case of all letters."""
    return ''.join(
        chr(ord(ch) + 32) if 'A' <= ch <= 'Z' else chr(ord(ch) - 32)
        for ch in s if ch.isalpha()
    )

def interleave_strings(s1, s2):
    """Zips two strings and uppercases the leftover characters from the longer one."""
    result = ''.join(a + b for a, b in zip(s1, s2))
    remainder = s1[len(s2):] if len(s1) > len(s2) else s2[len(s1):]
    return result + remainder.upper()

def is_rotation(a, b):
    """Checks if b is a rotation of a."""
    return b in (a + a)

def expand_pattern(s):
    """Expands compressed pattern strings like '3a4b' → 'aaabbbb'."""
    result = ""
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if i < len(s):
            char = s[i]
            i += 1
            result += char * int(count_str)
    return result

def expand_alpha_block(s):
    """Handles patterns like '31abc4b5c' → 'abc...abc' * 31 + 'b'*4 + 'c'*5"""
    result, num, alpha = "", "", ""
    i = 0
    while i < len(s):
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        while i < len(s) and s[i].isalpha():
            alpha += s[i]
            i += 1
        if num and alpha:
            result += int(num) * alpha
        num = alpha = ""
    return result

# Example calls (can be removed/commented when importing as module)
if __name__ == "__main__":
    unique_numbers([1, 2, 1, 2, 3])
    print(is_prime(33))
    print(count_vowels("kavya"))
    print(alphabet_position_sum("ABCD"))
    print(capitalize_vowels("abceik"))
    print(toggle_case("AbCdEG"))
    print(interleave_strings("ajik", "kanis"))
    print(is_rotation("abc", "cab"))
    print(expand_pattern("3a4d5c"))
    print(expand_alpha_block("31abc4b5c"))

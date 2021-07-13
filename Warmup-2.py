'''Given a string and a non-negative int n, return a larger string that is n copies of the original string.'''


def string_times(str, n):
    return str*n


'''Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
   or whatever is there if the string is less than length 3. Return n copies of the front;'''


def front_times(str, n):
    if len(str) < 3:
        return str*n
    else:
        return str[:3]*n


'''Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".'''


def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


'''Given a non-empty string like "Code" return a string like "CCoCodCode".'''


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return result


'''Given a string, return the count of the number of times that a substring length 2 appears in the string and
   also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).'''


def last2(str):
    if len(str) < 2:
        return 0

    last2 = str[len(str)-2:]
    count = 0

    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count = count + 1

    return count


'''Given an array of ints, return the number of 9's in the array.'''


def array_count9(nums):
    result = 0
    for i in nums:
        if i == 9:
            result += 1
    return result


'''Given an array of ints, return True if one of the first 4 elements in the array is a 9.
   The array length may be less than 4.'''


def array_front9(nums):
    if len(nums) < 4:
        for i in nums:
            if i == 9:
                return True
        else:
            return False

    elif len(nums) >= 4:
        for i in nums[0:4]:
            if i == 9:
                return True
        else:
            return False

# Another Solution


def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):
        if nums[i] == 9:
            return True
    return False


'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.'''


def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    else:
        return False


'''Given 2 strings, a and b, return the number of the positions where they contain the same
   length 2 substring.So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
   appear in the same place in both strings.'''


def string_match(a, b):
    small_str = min(len(a), len(b))
    count = 0
    for i in range(small_str-1):
        part_a = a[i:i+2]
        part_b = b[i:i+2]
        if part_a == part_b:
            count += 1
    return count

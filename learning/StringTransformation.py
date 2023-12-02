def cyclic_increment(char, count):
    char_code = ord(char) - ord('a')
    new_char_code = (char_code + count) % 26
    return chr(new_char_code + ord('a'))

def string_transformation(N, s):
    q = ''
    occurrences = {}

    for i in range(N):
        char = s[i]
        count = occurrences.get(char, 0)
        q += cyclic_increment(char, count)
        occurrences[char] = count + 1

    return q

# Input reading and processing
T = int(input("Enter the number of test cases: "))
for _ in range(T):
    N = int(input())
    s = input().strip()
    result = string_transformation(N, s)
    print(result)

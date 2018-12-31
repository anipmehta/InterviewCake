def k_longest_substring(string, k):
    char_dict = {}
    start = 0
    end = 0
    length = 0
    while len(string) > end >= start:
        if string[end] in char_dict:
            char_dict[string[end]] = char_dict[string[end]] + 1
        else:
            char_dict[string[end]] = 1

        if len(char_dict.keys()) > k:
            length = max(length, end - start)
            char_dict[string[start]] = char_dict[string[start]] - 1
            if char_dict[string[start]] == 0:
                char_dict.pop(string[start])
            start = start + 1
            end = end + 1
        else:
            end = end + 1
    return max(length, end-start)


test_cases = input()
for i in range(int(test_cases)):
    print(k_longest_substring(input(), input()))
def get_valid_sentence(string, words):
    hash_set = set()
    for word in words:
        hash_set.add(word)
    words = []
    helper(string, words, hash_set)
    return " ".join(words[::-1])


def helper(string, words, dictionary):
    if len(string) == 0:
        return True
    for i in range(1, len(string)+1):
        sub_string = string[0:i]
        if sub_string in dictionary and helper(string[i:], words, dictionary):
            words.append(sub_string)
            return True
    return False


print get_valid_sentence("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"])

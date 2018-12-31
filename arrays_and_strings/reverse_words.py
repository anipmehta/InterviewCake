def reverse_words(message):
    reverse_characters(message, 0, len(message) - 1)
    start_index = 0
    for i in xrange(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_characters(message, start_index, i - 1)
            start_index = i + 1


def reverse_characters(message, left_index, right_index):
    while left_index < right_index:
        message[left_index], message[right_index] = message[right_index], message[left_index]
        right_index -= 1
        left_index += 1


sentence = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']
reverse_words(sentence)
print ''.join(sentence)

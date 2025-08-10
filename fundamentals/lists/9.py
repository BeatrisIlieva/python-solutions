def merge(words, start_index, end_index):
    words_copy = words.copy()
    new_word = ''
    valid_end_index = end_index + 1 if end_index + \
        1 < len(words) else len(words) - 1

    for index in range(start_index, valid_end_index):
        new_word += words_copy[index]

    del words[start_index:valid_end_index]

    words.insert(start_index, new_word)

    return words


def divide(words, index, partitions):
    partition_length = len(words[index]) // partitions

    word_as_list = list(words[index])

    splitted_words = []

    while word_as_list:
        if len(word_as_list) < partition_length * 2:
            word_as_list.append(''.join(word_as_list[0]))
            break
        
        splitted_words.extend(word_as_list[0:partition_length])
        del word_as_list[0:partition_length]

    words.pop(index)
    words.insert(index, ''.join(splitted_words))
    
    return words


actions_mapper = {
    'merge': merge,
    'divide': divide,
}

words = input().split(' ')

command = input().split(' ')

while len(command) > 1:
    action, first_digit, second_digit = command

    words = actions_mapper[action](words, int(first_digit), int(second_digit))

    command = input().split(' ')

print(' '.join(words))


# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1

# abcd efgh ijkl mnop qrst uvwx yz
# merge 4 10
# divide 4 5
# 3:1

def merge(words, start_index, end_index):
    valid_start_index = max(0, start_index)
    valid_end_index = min(end_index + 1, len(words))

    if valid_start_index >= len(words) or valid_start_index >= valid_end_index:
        return words

    new_word = ''.join(words[valid_start_index:valid_end_index])

    words = words[:valid_start_index] + [new_word] + words[valid_end_index:]

    return words


def divide(words, index, partitions):
    word = words[index]
    base_length = len(word) // partitions
    pos = 0

    new_words = []

    for i in range(partitions):
        if i == partitions - 1:
            new_words.append(word[pos:])
            break

        new_words.append(word[pos: pos + base_length])

        pos += base_length
        
    words = words[:index] + new_words + words[index + 1:]

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


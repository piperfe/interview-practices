def reverse_order(word):
    word_in_array = convert_in_array_of_chars(word)
    init_to_end = 0
    end_to_init = len(word_in_array) - 1

    for character in word_in_array:
        if init_to_end >= end_to_init:
            return convert_in_string(word_in_array)

        word_in_array[init_to_end] = word_in_array[end_to_init]
        word_in_array[end_to_init] = character

        init_to_end += 1
        end_to_init -= 1


def convert_in_string(word_in_array):
    word_already_reversed = ''
    return word_already_reversed.join(word_in_array)


def convert_in_array_of_chars(word):
    word_in_array = []
    word_in_array.extend(word)
    return word_in_array

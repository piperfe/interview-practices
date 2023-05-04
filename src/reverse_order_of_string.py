def reverse_order(word):
    word_in_array = convert_in_array_of_chars(word)

    init_to_end = 0
    end_to_init = len(word_in_array) - 1

    while init_to_end < end_to_init:
        init_to_end_character = word_in_array[init_to_end]
        end_to_init_character = word_in_array[end_to_init]

        word_in_array[init_to_end] = end_to_init_character
        word_in_array[end_to_init] = init_to_end_character

        init_to_end += 1
        end_to_init -= 1

    return convert_in_string(word_in_array)


def convert_in_string(array_of_chars):
    string = ''
    return string.join(array_of_chars)


def convert_in_array_of_chars(string):
    array_of_chars = []
    array_of_chars.extend(string)
    return array_of_chars

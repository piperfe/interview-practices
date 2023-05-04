def move_zeros_to_the_left(array):
    index = 0
    zeros_in_array_index = 0

    for number in array:
        if is_zero(number):

            array[index] = array[zeros_in_array_index]
            array[zeros_in_array_index] = 0

            if is_zero(array[zeros_in_array_index]):
                zeros_in_array_index += 1

        index += 1

    return array


def is_zero(number):
    return number == 0

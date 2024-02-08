string = "the sky is blue"
string = list(string)


def get_last_index(string, character):
    for index in range(len(string)):
        if string[-index - 1] == character:
            return len(string) - index - 1


def shift_character_right(string, start_index):
    shifted_value = string[-1]

    for current_index in range(start_index, len(string)):
        current_value = string[current_index]
        string[current_index] = shifted_value
        shifted_value = current_value


def shift_word_right(string, start_index):
    if start_index < len(string):
        last_word_length = len(string) - get_last_index(string, ' ') - 1

        # shift each character of last word
        for character_index in range(last_word_length):
            shift_character_right(string, start_index)

        # shift space
        shift_character_right(string, start_index + last_word_length)

        # recursively call for subsing
        shift_word_right(string, start_index + last_word_length + 1)


shift_word_right(string, 0)

print("".join(string))

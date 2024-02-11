string = "pwwekwp"

global_maxima = 0

for start_index in range(len(string)):
    local_non_repeating_string = ""

    for character in string[start_index:]:
        if character not in local_non_repeating_string:
            local_non_repeating_string += character
        else:
            global_maxima = max(len(local_non_repeating_string), global_maxima)
            local_non_repeating_string = character
        global_maxima = max(len(local_non_repeating_string), global_maxima)

print(global_maxima)

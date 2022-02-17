from goto import with_goto


@with_goto
def main():
    with open('phrase.txt') as input_file:
        lines = input_file.readlines()

    words_to_avoid = ['a', 'an', 'was', 'am', 'were', 'the', 'at', 'for', 'to', 'on', 'in', 'from']
    limited_output = 25
    words_set = {}

    i = 0

    label .iterate_through_lines
    line = lines[i].strip()
    current_word = ''
    word_in_lower_case = ''
    j = 0

    label .iterate_through_symbols

    if line[j] == ' ' or j + 1 == len(line):
        if j + 1 == len(line):
            current_word += line[j]
        word_exist = False

        m = 0
        label .to_lower

        ch = ord(current_word[m])
        if ch > 64 and ch < 91:
            word_in_lower_case += chr(ch + 32)
        else:
            word_in_lower_case += chr(ch)
        m += 1

        if m < len(current_word):
            goto.to_lower

        current_word = word_in_lower_case
        word_in_lower_case = ''

        k = 0
        label .iterate_through_words

        if k >= len(list(words_set.keys())) or word_exist:
            goto .continue_counting_words

        if list(words_set.keys())[k] == current_word:
            word_exist = True

        k += 1
        goto.iterate_through_words

        label .continue_counting_words
        if word_exist:
            words_set[current_word] += 1
        else:
            # we have check if it is a stop word:
            k = 0
            is_stop_word = False
            label .iterate_through_words_to_avoid

            if words_to_avoid[k] == current_word:
                is_stop_word = True

            k += 1
            if k < len(words_to_avoid):
                goto .iterate_through_words_to_avoid

            if not is_stop_word and current_word:
                words_set[current_word] = 1

        current_word = ''
    else:
        current_word += line[j]

    j += 1
    if j < len(line):
        goto .iterate_through_symbols
    i += 1
    if i < len(lines):
        goto .iterate_through_lines

    words_set = list(words_set.items())

    i = 0
    label .iterate_set

    j = i
    max_word_index, max_word_count = j, 0
    label .while_j_less_len_words_freq

    if max_word_count < words_set[j][1]:
        max_word_index = j
        max_word_count = words_set[j][1]
    j += 1
    if j < len(words_set):
        goto.while_j_less_len_words_freq
    words_set[i], words_set[max_word_index] = words_set[max_word_index], words_set[i]
    i += 1
    if i < len(words_set):
        goto .iterate_set
    i = 0
    label .limit

    word, frequency = words_set[i]
    print(f'{word} - {frequency}')
    i += 1
    if i < limited_output and i < len(words_set):
        goto .limit


if __name__ == '__main__':
    main()
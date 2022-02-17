from goto import with_goto

@with_goto
def main():
    page_size = 45
    words_frequency_limit = 100

    with open('dictionary.txt') as input_file:
        file_lines = input_file.readlines()

    words_occurrence = {}
    i = 0
    label .iterate_through_lines
    line = file_lines[i]
    current_word = ''
    word_in_lower_case = ''
    j = 0

    label .iterate_through_symbols

    if line[j] == ' ' or (j + 1 == len(line) and line[-1] == '\n') or line[j] == ',' or line[j] == '.' or line[j] == '!' or line[j] == '?' or line[j] == ':' or line[j] == ';':
        word_exist = False

        if(current_word != ''):

            if (current_word[0] == '“' or current_word[0] == '"' or current_word[0] == '\''):
                duplicate_word = current_word
                pure_word = ''
                f = 0
                label.clean_word

                if (f + 1 < len(duplicate_word)):
                    pure_word += duplicate_word[f + 1]
                    current_word = pure_word
                    f += 1
                    goto.clean_word

            m = 0
            label.to_lower

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

        if k >= len(list(words_occurrence.keys())) or word_exist:
            goto .continue_counting_words

        if list(words_occurrence.keys())[k] == current_word:
            word_exist = True

        k += 1
        goto.iterate_through_words

        label .continue_counting_words
        if word_exist:
            words_occurrence[current_word][0] += 1
        else:
            if current_word:
                words_occurrence[current_word] = [1]

        if current_word:
            page_number = i // page_size + 1
            if words_occurrence[current_word][-1] != page_number or len(words_occurrence[current_word]) == 1:
                words_occurrence[current_word].append(page_number)

        current_word = ''
    else:
        current_word += line[j]

    j += 1
    if j < len(line):
        goto .iterate_through_symbols

    i += 1
    if i < len(file_lines):
        goto .iterate_through_lines

    i = 0
    words = list(words_occurrence.keys())
    label .iterate_through_keys

    word = words[i]

    if words_occurrence[word][0] > words_frequency_limit:
        del words_occurrence[word]

    if(word == '“' or word == '"' or word == '\'' or word == '”'):
        del words_occurrence[word]

    i += 1
    if i < len(list(words_occurrence.keys())):
        goto .iterate_through_keys

    words_occurrence = list(words_occurrence.items())

    i = 0
    label .sorting

    j = i
    min_word_index, min_word = j, words_occurrence[j][0]
    label .while_j_less_len_words_freq

    if min_word > words_occurrence[j][0]:
        min_word_index = j
        min_word = words_occurrence[j][0]

    j += 1
    if j < len(words_occurrence):
        goto.while_j_less_len_words_freq

    words_occurrence[i], words_occurrence[min_word_index] = words_occurrence[min_word_index], words_occurrence[i]

    i += 1
    if i < len(words_occurrence):
        goto .sorting

    i = 0
    label .printing_words

    word, count_and_pages_list = words_occurrence[i]

    print(word, end=' - ')

    k = 1
    label .printing_pages

    if(k != len(count_and_pages_list) - 1):
        print(count_and_pages_list[k], end=', ')
    else:
        print(count_and_pages_list[k], end=' ')

    k += 1
    if k < len(count_and_pages_list):
        goto.printing_pages

    print()

    i += 1
    if i < len(words_occurrence):
        goto .printing_words


if __name__ == '__main__':
    main()
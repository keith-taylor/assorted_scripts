words_to_ignore_list = ["a", "for", "is", "by", "to", "from", "I", "in", "written",
                        "created", "directed", "starring", "the", "be"]

elements_list = [
    'Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B', 'Ba',
    'Be', 'Bh', 'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cf',
    'Cl', 'Cm', 'Co', 'Cr', 'Cs', 'Cu', 'Db', 'Ds', 'Dy', 'Er',
    'Es', 'Eu', 'F', 'Fe', 'Fm', 'Fr', 'Ga', 'Gd', 'Ge', 'H',
    'He', 'Hf', 'Hg', 'Ho', 'Hs', 'I', 'In', 'Ir', 'K', 'Kr',
    'La', 'Li', 'Lr', 'Lu', 'Md', 'Mg', 'Mn', 'Mo', 'Mt', 'N',
    'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'No', 'Np', 'O', 'Os', 'P',
    'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb',
    'Re', 'Rf', 'Rg', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se',
    'Sg', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th',
    'Ti', 'Tl', 'Tm', 'U', 'Uub', 'Uuh', 'Uuo', 'Uup', 'Uuq', 'Uus',
    'Uut', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr'
]

elements_list_lower = []
for each_element in elements_list:
    elements_list_lower.append(each_element.lower())


def break_it_bad(input_text):
    """
    Takes a list of strings and returns them with colour highlighting
    that is reminiscent of the Breaking Bad TV series title sequence.
    :param input_text: a list of strings
    :return output_list: a formatted list of: strings and lists_of_strings
    """
    output_text = []
    for each_line in input_text:
        output_text.append(process_lines_of_text(each_line))
    return output_text


def process_lines_of_text(input_line_of_text):
    output_line_of_text = ""  #
    words_changed = 0  # a count of words changed in each line being processed
    max_words_to_change = 2  # set the max value for words to format

    words_in_each_line = input_line_of_text.split()  # a list contain the words from each line of text
    # go through each word in this line of text and...
    #   send each word to 'word_scan' unless we have two reformatted words already, or...
    #       the word is in the `ignore_list`
    # each word, scanned/re-formatted (or not) is re-added to the output_line_of_text to be returned
    text_as_list = []
    for each_word in words_in_each_line:
        if each_word.lower() in words_to_ignore_list:  # skip any words in the words_to_ignore list
            text_as_list.append(each_word)
        elif words_changed == max_words_to_change:  # don't bother scanning the word for matches if the limit reached
            text_as_list.append(each_word)
        else:
            each_word, match_found = word_scan(each_word)  # send the word to be scanned for matches in elements_list
            text_as_list.append(each_word)
            if match_found == True:
                words_changed += 1
    for word in text_as_list:  # change from list back to string
        output_line_of_text += word + " "
    return output_line_of_text


def word_scan(input_word):
    # takes a word as an argument and breaks it into a list of letters.
    # The list is then used as input for a search...
    #       for one letter and two-letter matches in elements_list_lower
    # a preference is given to two letter matches (this search is done first)
    # the word's capitalisation is changed to show the elements and returned to the calling function

    chars_in_each_word = [letter for letter in input_word]
    match_found = False # was a match found
    # checks for any two letter matches, exits on first one it finds
    for i in range(1, len(input_word)):
        two_letter_combo = chars_in_each_word[i-1] + chars_in_each_word[i]
        if two_letter_combo.lower() in elements_list_lower:
            two_letter_match_index = elements_list_lower.index(two_letter_combo.lower())
            formatted_word = [
                input_word.split(two_letter_combo)[0],
                str(elements_list[two_letter_match_index]),
                input_word.split(two_letter_combo)[1]
                ]
            output_word = f"[white]{formatted_word[0]}[bold green]{formatted_word[1]}[/bold green]{formatted_word[2]}"
            match_found = True
            return output_word, match_found  # if a match is found

    # check for any one letter matches (this runs only if two-char search above finds no matches)
    # stores the first one it finds
    if len(input_word) > 1:  # checks word is not a one letter word
        for each_letter in range(0, len(input_word)):  # iterate over the letters in the word
            if chars_in_each_word[each_letter].lower() in elements_list_lower:  # have we found a match?
                one_letter_match_index = elements_list_lower.index(chars_in_each_word[each_letter].lower())
                formatted_word = [
                    input_word.split(input_word[each_letter])[0],
                    str(elements_list[one_letter_match_index]),
                    input_word.split(input_word[each_letter])[1]
                    ]
                output_word = f"[white]{formatted_word[0]}[bold green]{formatted_word[1]}[/bold green]{formatted_word[2]}"
                # print(formatted_list)
                match_found = True
                return output_word, match_found # if a match is found
    else:
        return input_word, match_found  # if no match is found

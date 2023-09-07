words_to_ignore_list = ["a", "for", "is", "by", "to", "from", "I", "in", "written",
                        "created", "directed", "starring", "the", "be", "it", "of"]

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


def break_it_bad(input_text, max_words_to_change):
    """
    Takes a list of strings and returns them with formatting
    that is reminiscent of the Breaking Bad TV series title sequence.
    The formatting is based on matches to a list of chemical elements where matches
    are highlighted in green+bold text.
    :param input_text: a list of strings
    :return output_text: a formatted list of: strings and lists_of_strings
    """
    output_text = []
    for each_line in input_text:  # process each string found in the input list
        output_text.append(process_lines_of_text(each_line, max_words_to_change))
    return output_text


def process_lines_of_text(input_line_of_text, max_words_to_change):
    """
    Takes a text string and breaks this into a list of words.
    Each word in the list is then send to word_scan() and each returned word is used to re-assembled the string...
        (but now including any formatting changes) which is then returned to the calling function.
    :param input_line_of_text:
    :return: output_line_of_text
    """
    # go through each word in this line of text and...
    #   send each word to 'word_scan' unless we have two reformatted words already, or...
    #       the word is in the `ignore_list`
    # each word, scanned/re-formatted (or not) is re-added to the output_line_of_text to be returned
    output_line_as_list = []
    output_line_as_text = ""
    words_changed = 0  # a count of words changed in each line being processed
    elements_matched = []

    input_line_as_list = input_line_of_text.split()  # a list contain the words from each line of text


    for each_word in input_line_as_list:
        # just add the word to the list without scanning if any of below are true:
        if (each_word.lower() in words_to_ignore_list) or (words_changed == max_words_to_change) or len(each_word) < 2:
            output_line_as_list.append(each_word)
        else:
            # send the word to be scanned
            each_word, match_found, matched_element, elements_matched = process_words_into_chars(each_word, elements_matched)
            if match_found is True:
                words_changed += 1
                output_line_as_list.append(each_word)
    for word in output_line_as_list:  # change from list back to string
        output_line_as_text += word + " "
    return output_line_as_text


def process_words_into_chars(input_word, elements_matched):
    # takes a word as an argument and breaks it into a list of letters.
    # The list is then used as input for a search...
    #       for one letter and two-letter matches in elements_list_lower
    # a preference is given to two letter matches (this search is done first)
    # the word's capitalisation is changed to show the elements and returned to the calling function
    chars_in_each_word = [letter for letter in input_word]
    print(f"receiving elements_matched: {elements_matched}")

    # try: 2 chars, unused matches only
    for i in range(1, len(chars_in_each_word)):  # get a 2 char search term
        search_chars = chars_in_each_word[i - 1] + chars_in_each_word[i]
        print(f"STRICT: 2 search_chars (lower case): {search_chars.lower()}")
        if search_chars.lower() not in elements_matched:  # try novel matches only
            print("trying for a novel match")
            match_found, matched_element = is_element(search_chars)
            if match_found is True:
                print(f"2 strict: {search_chars}")
                elements_matched.append(search_chars.lower())
                return format_word(input_word, search_chars, matched_element), match_found, matched_element, elements_matched

    for i in range(0, len(chars_in_each_word)):  # try a one char match
        search_chars = chars_in_each_word[i]
        match_found, matched_element = is_element(search_chars)
        if match_found is True:
            print(f"1: {search_chars}")
            elements_matched.append(search_chars.lower())
            return format_word(input_word, search_chars, matched_element), match_found, matched_element, elements_matched
        else:  # if no matches found after all 3 attempts return input as output
            matched_element = None
            match_found = False
            return input_word, match_found, matched_element, elements_matched


    for i in range(1, len(chars_in_each_word)):
        for i in range(1, len(chars_in_each_word)):  # get a 2 char search term
            search_chars = chars_in_each_word[i - 1] + chars_in_each_word[i]
            print(f"NON-STRICT: 2 search_chars (lower case): {search_chars.lower()}")
            match_found, matched_element = is_element(search_chars)
            if match_found is True:
                elements_matched.append(search_chars.lower())
                return format_word(input_word, search_chars, matched_element), match_found, matched_element, elements_matched

    match_found = False
    matched_element = None
    return input_word, match_found, matched_element, elements_matched

def is_element(search_chars):
    match_found = False
    if search_chars.lower() in elements_list_lower:
        match_found = True
        matched_element = search_chars.lower()
        return match_found, matched_element  # if a match is found
    else:
        matched_element = None
        return match_found, matched_element   # if no match is found


def format_word(input_word, search_chars, matched_element):
    matched_element_index = elements_list_lower.index(matched_element.lower())
    return f"[white]{input_word.split(search_chars)[0]}[bold green]{elements_list[matched_element_index]}[/bold green]{input_word.split(search_chars)[1]}"

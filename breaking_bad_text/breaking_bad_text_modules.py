import random

words_to_ignore_list = ["a", "for", "is", "by", "to", "from", "I", "in", "written",
                        "created", "directed", "starring", "the", "be", "it", "of",
                        "guest", "edited", "director", "photography", "music", "casting"]

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
    :param max_words_to_change: max num. of words to be highlighted per line
    :param input_text: a list of strings
    :return output_text: a formatted list of: strings and lists_of_strings
    """
    output_text = []
    elements_matched = []  # a list to contain any matches made in this line of text
    for each_line in input_text:  # process each string found in the input list
        processed_text, elements_matched = process_lines_of_text(each_line, max_words_to_change, elements_matched)
        output_text.append(processed_text)
    print(elements_matched)
    return output_text


def process_lines_of_text(input_line_of_text, max_words_to_change, elements_matched):
    """
    Takes a line of text as a string and breaks this into a list of words.
    Each word in the list is then send to word_scan() (in random order) and each returned word is used to
    re-assembled the string (but now including any formatting changes) which is then returned to the calling function.
    :param elements_matched: the list containing any matches made
    :param input_line_of_text: a string
    :param max_words_to_change: how many formatting changes should be made in each line of text
    :return: output_line_of_text reassembled text with formatting changes
    """
    # go through each word in this line of text and...
    #   send each word to 'word_scan' unless we have two reformatted words already, or...
    #       the word is in the `ignore_list` or the word is too small (<2 chars).
    # each word, scanned and re-formatted (or not) is re-added to the output_line_as_list.
    # This is rebuilt into a string and returned.

    output_line_as_text = ""
    words_changed = 0  # a count of words changed in each line being processed

    input_line_as_list = input_line_of_text.split()  # creates a list containing the words from this line of text
    output_line_as_list = [None] * len(input_line_as_list)  # a list to contain the output as received from word_scan

    # creates a list of random indexes (matching the number of words in the input text)
    search_order_list = generate_search_order_list(len(input_line_as_list))

    # iterate through the random indexes in search order list to grab each word in turn
    # check if we should bypass processing for this word
    # if not, send the word to the function `process_words_into_chars`
    # either way the input or output word is added into output_line_as_list to re-create the text
    for i in search_order_list:
        # get each word in turn
        word = input_line_as_list[i]
        # just add the word to the list without processing if any of below are true:
        if (word.lower() in words_to_ignore_list) or (words_changed == max_words_to_change) or len(word) < 2:
            output_line_as_list[i] = input_line_as_list[i]  # skip processing & use the unformatted word
        else:
            # send the word to be processed
            word, match_found, matched_element, elements_matched = process_words_into_chars(word, elements_matched)
            # was the word matched to a chemical element and reformatted?
            if match_found is True:
                words_changed += 1
                output_line_as_list[i] = word  # use the newly formatted word
            else:
                output_line_as_list[i] = input_line_as_list[i]  # use the unformatted word

    # change from a list strings back to a string
    for word in output_line_as_list:
        output_line_as_text += word + " "

    return output_line_as_text, elements_matched


def process_words_into_chars(input_word, elements_matched):
    # takes a word as an argument and breaks it into a list of letters.
    # The list is then used as input for a search...
    #       for one letter and two-letter matches in elements_list_lower
    # a preference is given to two letter matches (this search is done first)
    # the word's capitalisation is changed to show the elements and returned to the calling function

    # convert words into chars
    chars_in_each_word = [letter for letter in input_word]

    # iterate over combination of sequential chars
    # try: 2 chars, unused matches only (if match already used in this line, skip it)
    for i in range(1, len(chars_in_each_word)):  # get a 2 char search term
        search_chars = chars_in_each_word[i - 1] + chars_in_each_word[i]
        print(f"2 char, unmatched only, search term is: {search_chars}")
        if search_chars.lower() not in elements_matched:  # try novel matches only
            match_found, matched_element = is_element(search_chars)
            if match_found is True:
                print(f"Unused match found: {search_chars}")
                elements_matched.append(search_chars.lower())
                print(f"elements_matched updated: {elements_matched}")
                # exit with a match (if found)
                return (format_word(input_word, search_chars, matched_element), match_found,
                        matched_element, elements_matched)

    for i in range(0, len(chars_in_each_word)):  # try a one char match
        search_chars = chars_in_each_word[i]
        print(f"1 char matches, search term is: {search_chars}")
        match_found, matched_element = is_element(search_chars)
        if match_found is True:
            print(f"1 char match found: {search_chars}")
            elements_matched.append(search_chars.lower())
            print(f"elements_matched updated: {elements_matched}")
            return (format_word(input_word, search_chars, matched_element), match_found,
                    matched_element, elements_matched)

    for i in range(1, len(chars_in_each_word)):  # get a 2 char search term
        search_chars = chars_in_each_word[i - 1] + chars_in_each_word[i]
        print(f"2 char, any match, search term is: {search_chars}")
        match_found, matched_element = is_element(search_chars)
        if match_found is True:
            print(f"2 char match found: {search_chars}")
            elements_matched.append(search_chars.lower())
            # exit with a match (if found)
            return (format_word(input_word, search_chars, matched_element), match_found,
                    matched_element, elements_matched)

    # if we haven't exited by finding a match above:
    match_found = False
    matched_element = None
    return input_word, match_found, matched_element, elements_matched


def is_element(search_chars):
    match_found = False
    if search_chars.lower() in elements_list_lower:
        match_found = True
        matched_element = search_chars.lower()
        return match_found, matched_element  # if a match is found: is_element
    else:
        matched_element = None
        return match_found, matched_element   # if no match is found


def format_word(input_word, search_chars, matched_element):
    matched_element_index = elements_list_lower.index(matched_element.lower())
    return (f"[white]{input_word.split(search_chars)[0]}[bold green]{elements_list[matched_element_index]}"
            f"[/bold green]{input_word.split(search_chars)[1]}")


def generate_search_order_list(length_of_search_order_list):
    """
       Generates a list, of length len(input_line_as_list) of integers (staring at 0) in random order.
    These are used to randomize the order the words are sent to word_scan to prevent
    matches being biased towards the front of longer lines of text.
    :param: length_of_search_order_list
    :return: search_order_list
    """
    search_order_list = []
    while len(search_order_list) < length_of_search_order_list:
        index_num = random.randint(0, length_of_search_order_list-1)
        if index_num not in search_order_list:
            search_order_list.append(index_num)
    return search_order_list

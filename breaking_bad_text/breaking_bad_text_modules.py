words_to_ignore_list = ["a", "for", "is", "by", "to", "from", "I", "in", "written",
                        "created", "directed", "starring", "the", "be"]

elements_list = [
    'Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B',
    'Ba', 'Be', 'Bh', 'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd',
    'Ce', 'Cf', 'Cl', 'Cm', 'Co', 'Cr', 'Cs', 'Cu', 'Db',
    'Ds', 'Dy', 'Er', 'Es', 'Eu', 'F', 'Fe', 'Fm', 'Fr',
    'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'Hs',
    'I', 'In', 'Ir', 'K', 'Kr', 'La', 'Li', 'Lr', 'Lu',
    'Md', 'Mg', 'Mn', 'Mo', 'Mt', 'N', 'Na', 'Nb', 'Nd',
    'Ne', 'Ni', 'No', 'Np', 'O', 'Os', 'P', 'Pa', 'Pb',
    'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re',
    'Rf', 'Rg', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se',
    'Sg', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te',
    'Th', 'Ti', 'Tl', 'Tm', 'U', 'Uub', 'Uuh', 'Uuo', 'Uup',
    'Uuq', 'Uus', 'Uut', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr'
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
    output_list = []
    for each_line in input_text:
        output_list.append(process_each_line(each_line))
    return output_list

def process_each_line(line):
    words_in_each_line = line.split()  # a list contain the words from each line of text
    output_line = []  #
    words_changed = 0  # a count of words changed in each line being processed
    max_words_to_change = 3  # set the max value for words to format
    formatted_char_list = []  # we shall return this list of words (some now formatted)

    # go through each word in this line of text
    # send each word to 'word_scan' unless we have two reformatted words already
    # or the word is in the `ignore_list`
    # each word, scanned/re-formatted or not is re-added to the output_line to be returned
    for each_word in words_in_each_line:
        if each_word.lower() in words_to_ignore_list:  # skip any words in the words_to_ignore list
            output_line.append(each_word)
        elif words_changed == max_words_to_change:  # don't bother scanning the word for matches if the limit reached
            output_line.append(each_word)
        else:
            each_word = word_scan(each_word)  # send the word to be scanned for matches in elements_list
            output_line.append(each_word)
            if type(each_word) == list:
                words_changed += 1
    # if the word
    for word in output_line:
            if type(word) == list:
                formatted_char_list.append(f"[white]{word[0]}[bold green]{word[1]}[/bold green]{word[2]}")
                # formatted_line.append(formatted_word)
            else:
                formatted_char_list.append(word)
            # print(formatted_list)
    formatted_string = " ".join(formatted_char_list)
    return formatted_string

def word_scan(input_word):
    # takes a word as an argument and breaks it into a list of letters.
    # The list is then used as input for a search...
    #       for one letter and two-letter matches in elements_list_lower
    # a preference is given to two letter matches (this search is done first)
    # the word's capitalisation is changed to show the elements and returned to the calling function

    split_word = [letter for letter in input_word]

    # checks for any two letter matches, exits on first one it finds
    for i in range(1, len(input_word)):
        two_letter_combo = split_word[i-1] + split_word[i]
        if two_letter_combo.lower() in elements_list_lower:
            two_letter_match_index = elements_list_lower.index(two_letter_combo.lower())
            output_word_as_list = [
                input_word.split(two_letter_combo)[0],
                str(elements_list[two_letter_match_index]),
                input_word.split(two_letter_combo)[1]
                ]
            return output_word_as_list

    # check for any one letter matches (this runs only if two-char search above finds no matches)
    # stores the first one it finds
    one_letter_match_index = None
    if len(input_word) > 1:  # checks word is not a one letter word
        for each_letter in range(0, len(input_word)):  # iterate over the letters in the word
            if split_word[each_letter].lower() in elements_list_lower:  # have we found a match?
                one_letter_match_index = elements_list_lower.index(split_word[each_letter].lower())
                output_word_as_list = [
                    input_word.split(input_word[each_letter])[0],
                    str(elements_list[one_letter_match_index]),
                    input_word.split(input_word[each_letter])[1]
            ]
        return output_word_as_list  # if a match is found
    else:
        return input_word  # if no match is found





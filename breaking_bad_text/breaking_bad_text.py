from breaking_bad_text_modules import *
from rich import print
import time

elements_dict_lower = {}
for each_element in elements_list:
    elements_dict_lower[str(each_element.lower())] = False

test_text_1 = [
    "This is the test text.", "It contains lines of text.",
    "Please use this to check.",
    "This is Purple Parents - can be Fevered Little shilas.",
    "Gaps in germs pootle labour sensing titles.",
    "Breaking Bad",
    "Created by Vince Gilligan",
    "Fertile Fecal Frank France"
]

# This is Purple Parents -

test_text_2 = ["This is the test text."]

max_words_to_change = 2  # set the max value for words to format

output_list = break_it_bad(test_text_1, max_words_to_change)


for each_line in output_list:
    print(each_line)
    time.sleep(0.75)



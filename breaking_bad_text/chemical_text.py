from breaking_bad_text_modules import *
from rich import print

test_text_1 = [
    "This is the test text.", "It contains lines of text.",
    "Please use this to check.",
    "Purple Parents can be Fevered Little shills.",
    "Gaps in germs pootle labour sensing titles.",
    "Breaking Bad",
    "Created by Vince Gilligan"
]

test_text_2 = ["breaking bad", "Created by Vince Gilligan."]

test_text_3 = ["This"]

output_list =  break_it_bad(test_text_1)

for list in output_list:
    print(list)

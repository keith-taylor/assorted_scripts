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

output_list =  break_it_bad(test_text_1)

for each_line in output_list:
    print(each_line)


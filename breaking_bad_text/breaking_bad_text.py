from breaking_bad_text_modules import *
from rich import print
import time

elements_dict_lower = {}
for each_element in elements_list:
    elements_dict_lower[str(each_element.lower())] = False

titles_text = [
    "Breaking Bad",
    "Created by Vince Gilligan",
    "Bryan Cranston",
    "Anna Gunn",
    "Aaron Paul",
    "Dean Norris",
    "Betsy Brandt",
    "RJ Mittie",
    "Bob Odenkirk",
    "Giancarlo Esposito",
    "Jonathan Banks",
    "Guest Starring \n Nigel Gibbs",
    "Edited by \n Skip Macdonald",
    "Production Designer \n Mark Freeborn",
    "Director of Photography \n Nelson Cragg",
    "Music by \n Dave Porter",
    "Casting by \n Sharon Baily C.S.A. \n Sherry Thomas C.S.A."
]

max_words_to_change = 2  # set the max value for words to format

output_list = break_it_bad(titles_text, max_words_to_change)


for each_line in output_list:
    print(each_line)
    time.sleep(0.75)

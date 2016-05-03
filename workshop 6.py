"""

STATE_NAMES = {"QLD":"Queensland", "NSW": "New South Wales", "NT":"Northern Territory", "WA":"Western Australia", "ACT":"Australian Capital Territory", "VIC":"Victoria", "TAS":"Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()



COLOR_NAMES = {"AliceBlue":"#f0f8ff","AntiqueWhite":"#faebd7","AntiqueWhite1":"#ffefdb","AntiqueWhite2":"#eedfcc","AntiqueWhite3":"#cdc0b0","AntiqueWhite4":"#8b8378","aquamarine1":"#7fffd4","aquamarine2":"#76eec6","aquamarine4":"#458b74","azure1":"#f0ffff"}

color = input("Enter color name: ")
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = input("Enter color name: ")
"""
import string

text_line= {}
text =input("Text: ").split()

for each_word in text:
    word = each_word.strip(string.punctuation)
    if word not in text_line:
        text_line[word] = 1
    else:
        text_line[word] +=1

for word in sorted(text_line):
    print("{} : {}".format(word, text_line[word]))


import nltk
from nltk import word_tokenize, pos_tag
import keyboard
text = open("MegaBig.txt",'r',encoding='utf-8').read()
words = word_tokenize(text)
pos_tags = pos_tag(words)
seed_text = input("Enter a seed text: ")
tokenized_seed = word_tokenize(seed_text)
pos_tagger = pos_tag(tokenized_seed)
tag_needle = []
for i in range(len(pos_tagger)):
  tag_needle.append(pos_tagger[i][1])
matching_elements = []
last_needle_element = tag_needle[-1]
'''
for i in range(len(pos_tags)):
  if last_needle_element == pos_tags[i][1]:
    try:
      matching_elements.append(pos_tags[i+1][0])
    except:
      pass
'''
last_word = tokenized_seed[-1]
for i in range(len(pos_tags)):
  if last_word == pos_tags[i][0]:
    try:
      matching_elements.append(pos_tags[i+1][0])
    except:
      pass
element_counts = {}
# Count the occurrences of elements
for element in matching_elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
sorted_counts = sorted(element_counts.items(), key=lambda x: x[1], reverse=True)
i = 0
print("Top Ten: ")
for element, count in sorted_counts:
    i = i + 1
    if element in tokenized_seed:
      i = i - 1
      continue
    print(f"{seed_text} {element}")
    if i == 10:
      break
print("press 'c' to leave")
keyboard.wait("c")

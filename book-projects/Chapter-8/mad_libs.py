#! python3
# mad_libs.py - Reads in a text file and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# The results are then printed to the screen and saved to a new text file.

import re

# Open the text file
story_file = open('story.txt')

# Read the file's contents and split into separate words.
story = story_file.read()
story_words = story.split()

# Find words such as ADJECTIVE, NOUN, etc. and prompt the user to replace them.
adj_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
verb_regex = re.compile(r'VERB')
for i in story_words:
    adj = adj_regex.findall(i)
    noun = noun_regex.findall(i)
    verb = verb_regex.findall(i)
    if adj:
        story = re.sub(adj_regex,
                       str(input("Enter an adjective: ")), story, 1)
    elif noun:
        story = re.sub(noun_regex,
                       str(input("Enter a noun: ")), story, 1)
    elif verb:
        story = re.sub(verb_regex,
                       str(input("Enter a verb (past tense): ")), story, 1)

# Display the results on the screen
print(story)

# Save to a new text file.
new_story_file = open('new_story.txt', 'a')
new_story = new_story_file.write(story)

# Close both files.
story_file.close()
new_story_file.close()

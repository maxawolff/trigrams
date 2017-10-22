"""Kata fourteen."""


def read_text(source_file):
    """Take a .txt file, read it, and save as a string."""
    import io
    f = io.open(source_file, encoding='utf-8')
    source_txt = f.read()
    f.close()
    return source_txt


def string_to_list(text):
    """Take a string return a list of strings sepperated on spaces."""
    list_of_words = text.split(' ')
    new_list = []
    for word in list_of_words:
        if word.isalnum():
            new_list.append(word)
    return new_list


"""
def clean_up_text(a_string):
   Remove unwanted characters from string.
    while not a_string.isalnum():
        for letter in a_string:
            if not letter.isalnum():
"""


def remove_ns(a_string):
    """Remove the newline characters from a string."""
    list_of_sentences = a_string.split('\n')
    sentences = ''
    for item in list_of_sentences:
        sentences += ' ' + item
    return sentences

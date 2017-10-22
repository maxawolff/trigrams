"""Kata fourteen."""

key_dict = {}
list_of_keys = []


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


def remove_ns(a_string):
    """Remove the newline characters from a string."""
    list_of_sentences = a_string.split('\n')
    sentences = ''
    for item in list_of_sentences:
        sentences += ' ' + item
    return sentences


def make_dictionary(list_of_strings):
    """."""
    key_dict = {}
    for idx in range(0, len(list_of_strings) - 2):
        key = list_of_strings[idx] + ' ' + list_of_strings[idx + 1]
        if key in key_dict:
            key_dict[key].append(list_of_strings[idx + 2])
        else:
            key_dict[key] = [list_of_strings[idx + 2]]
    return key_dict


def make_keys(list_of_strings):
    """."""
    list_of_keys = []
    for idx in range(0, len(list_of_strings) - 2):
        key = list_of_strings[idx] + ' ' + list_of_strings[idx + 1]
        if key not in list_of_keys:
            list_of_keys.append(key)
    return list_of_keys


def choose_random_word(key, a_dict):
    """."""
    import random
    if key not in a_dict:
        return("That key is not in the dictionary")
    else:
        return(random.choice(a_dict[key]))


def choose_random_key(list_of_keys):
    """."""
    import random
    return(random.choice(list_of_keys))


def choose_next_word(key):
    """."""
    word = choose_random_word(key_dict[key], key_dict)
    if word == "That key is not in the dictionary":
        choose_next_word()

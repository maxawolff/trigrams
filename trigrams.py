"""Kata fourteen."""

key_dict = {}


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


def make_keys(list_of_keys):
    """."""
    for idx in range(0, len(list_of_keys) - 2):
        key = list_of_keys[idx] + ' ' + list_of_keys[idx + 1]
        if key in key_dict:
            key_dict[key].append(list_of_keys[idx + 2])
        else:
            key_dict[key] = [list_of_keys[idx + 2]]
    return key_dict

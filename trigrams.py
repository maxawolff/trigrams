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
    """Take a string return a list of strings sepperated on space.

    also removes non-alpha numeric characters, originally to remove spaces
    """
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
    """Generate a dictionary with two word keys and the next word as value."""
    key_dict = {}
    for idx in range(0, len(list_of_strings) - 2):
        key = list_of_strings[idx] + ' ' + list_of_strings[idx + 1]
        if key in key_dict:
            key_dict[key].append(list_of_strings[idx + 2])
        else:
            key_dict[key] = [list_of_strings[idx + 2]]
    return key_dict


def make_keys(list_of_strings):
    """Generate keys gives a list of strings."""
    list_of_keys = []
    for idx in range(0, len(list_of_strings) - 1):
        key = list_of_strings[idx] + ' ' + list_of_strings[idx + 1]
        if key not in list_of_keys:
            list_of_keys.append(key)
    return list_of_keys


def choose_random_key(list_of_keys):
    """Choose a random key given a list of keys."""
    import random
    return(random.choice(list_of_keys))


def main(n, path):  # pragma: no cover
    """Function to run when program is called, makes the trigram."""
    words = ''
    raw_text = read_text(path)
    better_text = remove_ns(raw_text)
    list_of_strings = string_to_list(better_text)
    list_of_keys = make_keys(list_of_strings)
    dict_of_kvp = make_dictionary(list_of_strings)
    starting_val = choose_random_key(list_of_keys)
    words = starting_val
    # chooses random two words to start

    for i in range(0, n - 2):
        while(starting_val not in dict_of_kvp):
            starting_val = choose_random_key(list_of_keys)
        possible_words = dict_of_kvp[starting_val]
        chosen_word = choose_random_key(possible_words)
        # chooses a word that can follow the first two
        words += ' ' + chosen_word
        # new word is added to words
        some_list = words.split(' ')
        starting_val = some_list[len(some_list) - 2] + ' ' + some_list[len(some_list) - 1]
        # resets starting value to be the last two words in words
    print(words)
    return words


if __name__ == '__main__':
    import sys
    main(int(sys.argv[1]), str(sys.argv[2]))

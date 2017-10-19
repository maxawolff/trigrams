"""Kata fourteen."""


def processes_input(source_file):
    """."""
    import io
    f = io.open(source_file, encoding='utf-8')
    source_txt = f.read()
    f.close()
    print(source_txt)
    return source_txt


def input_string_to_list(string):
    """."""
    list_of_words = string.split(' ')
    for i in list_of_words:
        word = i.split('\n')
        return word
    return list_of_words

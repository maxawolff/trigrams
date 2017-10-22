"""."""
import pytest


def test_read_text():
    """."""
    from trigrams import read_text
    # assert processes_input('sherlock_sample.txt') == True
    if read_text('sherlock_sample.txt'):
        assert True
    else:
        assert False


words = [(1, 'was'), (2, 'on'), (3, 'the'), (5, 'of'),
         (0, 'One'), (7, 'returning')]


@pytest.mark.parametrize('n, result', words)
def test_sting_to_list(n, result):
    """."""
    from trigrams import string_to_list, read_text, remove_ns
    test_string = read_text('sherlock_sample.txt')
    another_string = remove_ns(test_string)
    str_list = string_to_list(another_string)
    assert str_list[n] == result


def test_remove_ns():
    """."""
    from trigrams import remove_ns
    assert remove_ns(
        '\nHello world \nhow are you') == '  Hello world  how are you'


def test_make_keys():
    """."""
    test_list = ["I", "wish", "I", "may", "I", "wish", "I", "might"]
    test_dict = {
        "I wish": ["I", "I"], "wish I": ["may", "might"],
        "may I": ["wish"], "I may": ["I"]}
    from trigrams import make_keys
    assert make_keys(test_list) == test_dict

"""."""
import pytest


def test_open_file():
    """."""
    from trigrams import processes_input
    # assert processes_input('sherlock_sample.txt') == True
    if processes_input('sherlock_sample.txt'):
        assert True
    else:
        assert False


words = [(2, 'was'), (6, 'of'), (0, 'One'), (9, 'returning')]


@pytest.mark.parametrize('n, result', words)
def test_sting_list(n, result):
    """."""
    from trigrams import input_string_to_list, processes_input
    test_string = processes_input('sherlock_sample.txt')
    list = input_string_to_list(test_string)
    # assert list[n] == result
    assert list == 'One'

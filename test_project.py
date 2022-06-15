from project import *
import string


def test_is_word_guessed():
    assert is_word_guessed('campus', ['a', 'p', 'u', 'r']) == False
    assert is_word_guessed('campus', ['a', 'p', 'u', 'r', 'm', 'c', 's']) == True


def test_get_guessed_word():
    assert get_guessed_word('purples', ['a', 'p', 'u', 'r'], 'pu_p___') == 'purp___'
    assert get_guessed_word('campus', ['a', 'p', 'u', 'r'], '_a_p__') == '_a_pu_'


def test_get_available_letters():
    assert get_available_letters(['a', 'c', 'z'], list(string.ascii_lowercase)) == ['b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    assert get_available_letters([' ', '1', 'a'], list(string.ascii_lowercase)) == ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def main():
    test_is_word_guessed()
    test_get_guessed_word()
    test_get_available_letters()

if __name__ == "__main__":
    main()

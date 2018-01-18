"""
Group 10 : R.S.
"""

from g6_polarity_feel_v1_2 import del_stop_word_list


def test_del_stop_word_list():
    text = ["Romain", '"', "dit", ":", "J", "'", "aime", ',', ';',
            "les", "(", "patates", ")", ".", "Et", "toi", "?", '[', ']']
    element = del_stop_word_list(text)
    assert element == ["Romain", "dit", "J", "aime", "patates", "Et"]

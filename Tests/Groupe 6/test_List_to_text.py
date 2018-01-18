"""
Group 10 : R.S.
"""

from g6_polarity_feel_v1_2 import List_to_text


def test_List_to_text():
    text = ["Romain", "dit", "J", "aime", "patates", "Et"]
    element1 = List_to_text(text)
    text = ["Romain", "dit", ":", "J", "'", "aime", ',', ';',
            "les", "(", "patates", ")", ".", "Et", "toi", "?", '[', ']']
    element2 = List_to_text(text)
    assert element1 == "Romain dit J aime patates Et"
    assert element2 == "Romain dit : J ' aime , ;" + \
        " les ( patates ) . Et toi ? [ ]"

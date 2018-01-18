"""
Group 10 : R.S.
"""

from g6_polarity_feel_v1_2 import Text_to_list


def test_Text_to_list():
    text = "Romain dit : J ' aime , ; les ( patates ) . Et toi ? [ ]"
    element1 = Text_to_list(text)
    text = "Romain dit J aime patates Et"
    element2 = Text_to_list(text)
    assert element1 == ["Romain", "dit", "J", "aime", "patates", "Et"]
    assert element2 == ["Romain", "dit", "J", "aime", "patates", "Et"]

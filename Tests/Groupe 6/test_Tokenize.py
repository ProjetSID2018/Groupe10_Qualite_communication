"""
Group 10 : R.S.
"""

from g6_polarity_feel_v1_2 import Tokenize


def test_Tokenize():
    text = "Je suis un chat"
    element1 = Tokenize(text)
    text = "Nous Sommes en train de FaiRe des tests unitaIres"
    element2 = Tokenize(text)
    assert element1 == ["Je", "suis", "un", "chat"]
    assert element2 == [
        "Nous",
        "Sommes",
        "en",
        "train",
        "de",
        "FaiRe",
        "des",
        "tests",
        "unitaIres"]

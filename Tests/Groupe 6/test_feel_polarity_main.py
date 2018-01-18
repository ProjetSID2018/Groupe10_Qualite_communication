"""
Group 10 : R.S.
"""

from g6_polarity_feel_v1_2 import feel_polarity_main


def test_feel_polarity_main():
    # haine =        (0,0,0,1,0,1,1,0)
    # crotale =      (0,1,0,0,0,1,1,0)
    # aborder =      (0,0,0,1,1,0,0,1)
    # broyer =       (0,1,1,1,0,1,1,0)
    # odontologie =  (0,1,0,0,0,0,0,1)
    # pétiller =     (1,0,0,0,0,0,0,1)
    # rôder =        (0,1,0,0,1,0,1,0)
    # sou entendre = (0,1,0,1,1,0,0,1)
    # suicide =      (0,1,1,1,0,0,1,0)
    # vol =          (0,1,1,1,1,1,1,0)
    word = [
        "haine",
        "crotale",
        "aborder",
        "broyer",
        "odontologie",
        "pétiller",
        "rôder",
        "sou entendre",
        "suicide",
        "vol"]
    element1 = feel_polarity_main(word)
    word = []
    element2 = feel_polarity_main(word)
    assert element1 == {
        'rate_angry': 0.6,
        'rate_disgust': 0.4,
        'rate_fear': 0.7,
        'rate_joy': 0.1,
        'rate_negativity': 0.6,
        'rate_positivity': 0.4,
        'rate_sadness': 0.3,
        'rate_surprise': 0.4}
    assert element2 == {
        'rate_angry': 0.0,
        'rate_disgust': 0.0,
        'rate_fear': 0.0,
        'rate_joy': 0.0,
        'rate_negativity': 0.0,
        'rate_positivity': 0.0,
        'rate_sadness': 0.0,
        'rate_surprise': 0.0}

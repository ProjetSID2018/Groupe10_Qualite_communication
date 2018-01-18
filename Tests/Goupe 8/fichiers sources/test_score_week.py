# -*- coding: utf-8 -*-
# Groupe 10
# Pierrick HERVE
# Christelle LATORRE
# V1 : 4 tests + le SetUp()
from fonctions_groupe8_a_tester import score_week
import pytest
from io import StringIO
import numpy
import json


@pytest.fixture()
def setUp():
    file = json.load(open("score_weekV2.json", "r"))
    top_word = 3
    return score_week(file, top_word)


"""
All Tfs are between 0 and 1
"""


def test_score_week1(setUp):
    step = 0.00000001
    expected = numpy.arange(0, 1 + step, step)
    values_extracted = []
    values = setUp[1].values()
    for val in values:
        for i in range(len(val)):
            values_extracted.append(val[i])
    for val in values_extracted:
        assert val in expected


"""
The size of the first dictonnary returned correspondes to top_world
"""


# def test_score_week2(setUp):
# file = open("score_weekV2.json", "r")
# file = json.load(file)
# top_word = 1

# res = score_week(file,top_word)
# print(res[1])

# assert

"""
the first word returned is the most important one
"""


# def test_score_week3(setUp):
# assert


"""
The mean of TFs is correct
"""


# def test_score_week4(setUp):
# assert

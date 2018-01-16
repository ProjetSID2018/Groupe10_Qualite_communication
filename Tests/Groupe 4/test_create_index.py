# -*- coding: utf-8 -*-
# Groupe 10
# Pierrick HERVE
# V1 : 4 tests + le SetUp()
from g4_utils_v32 import create_index
import pytest
import os
import re
import sys
from io import StringIO


@pytest.fixture()
def setUp():
    return create_index()


"""
file exist
"""


def test_create_index1(setUp):
    path = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.basename(__file__)
    assert os.path.isfile(path + '\\' + file_name)


"""
file is not empty
"""


def test_create_index2(setUp):
    file_content = open("hash_text.csv", "r").read()
    assert file_content != ''


# TODO: A TESTER avec des vrais données
"""
first value has the expected format
"""
#def test_create_index3(setUp):
    #first_value = open("hash_text.csv", "r").readline()
    #dates = re.finditer('[0-9]{4}\-[0-9]{2}\-[0-9]{2}', first_value)
    #assert dates == '[0-9]{4}\-[0-9]{2}\-[0-9]{2}'

"""
the message "creer" is printed
"""


def test_create_index4(setUp):
    # save the standard output
    old_stdout = sys.stdout
    # define the new output
    result = StringIO()
    sys.stdout = result
    # call the function to test
    create_index()
    # get back the standard output
    sys.stdout = old_stdout
    # we get the content of the output
    result_string = result.getvalue()
    assert result_string == 'creer\n'

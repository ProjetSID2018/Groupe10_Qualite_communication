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
    return parserV1()

"""
An error is raised
"""
#def test_parserV1():
    #with pytest.raises(StandardError):

        
"""
Everything is ok
"""
def test_parserV1(setUp):
    assert
    
   
"""
the execution time is printed
"""
def test_parserV1(setUp):
    assert


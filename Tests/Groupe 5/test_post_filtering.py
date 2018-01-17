# -*- coding: utf-8 -*-
# Groupe 10
# Pierrick HERVE
# V1 : 3 test + setUp()
from g5_database_posts import post_filtering
import pytest


@pytest.fixture()
def setUp():
    json = {"title": 'test article',
            "newspaper": 'newspaper name',
            "author": 'Pierrick HERVE',
            "date_publi": '16/01/2018',
            "theme": 'unit tests',
            "content": 'Lorem Ipsum'
            }
    return post_filtering(json)


"""
the url is the expected url
"""


def test_post_filtering1(setUp):
    url_attendue = 'http://130.120.8.250:5005/var/www/html/projet2018/code/\
    bd_index/API_V2/index/filtering'
    url = str(setUp.url)
    assert url == url_attendue


"""
the response code is 200
"""


def test_post_filtering2(setUp):
    status_code = setUp.status_code
    status_code_attendu = 200
    assert status_code == status_code_attendu


"""
the request is a POST request
"""


def test_post_filtering3(setUp):
    request = str(setUp.request)
    request_attendu = '<PreparedRequest [POST]>'
    assert request == request_attendu

"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 11 2018
@author: Maxime BRIENS
============================================================================"""
import requests


def post_EN(json):
    url_EN= 'http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/\
        API/index/entity'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_EN, headers=headers, json=json)
    return response


def post_POSTAG(json):
    url_POS = 'http://130.120.8.250:5005/var/www/html/projet2018/code/\
        bd_index/API/index/postagging'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_POS, headers=headers, json=json)
    return response


# def post_WORD(json):
#    url_POS = 'http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/API/index/word'
#    headers = {'Content-Type': 'application/json'}
#    response = requests.post(url_POS, headers = headers, json = json)
#    return response

def post_filtering(json):
    url_POS = 'http://130.120.8.250:5005/var/www/html/projet2018/code/\
    bd_index/API_V2/index/filtering'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_POS, headers=headers, data=json)
    return response

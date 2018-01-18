#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:28:26 2018

@author: Hbabou Nabil, Seguela Morgan

V1.0 
Extraction des articles du fux RSS

V1.1
Decoupage du code en Fonctions
"""

import os
import lxml.html as lh
import json
import datetime as date
from bs4 import BeautifulSoup
import requests
import re
import unidecode
import g4_utils_v32 as utilsg4
import html


def get_rss_infos():
    """Get all articles link
    
    Returns:
        list -- list of articles url
    """

    url_rss_lib = "http://www.liberation.fr/rss"
    req = requests.get(url_rss_lib)
    data = req.text
    soup = BeautifulSoup(data, "lxml")

    rss_items = soup.find_all("li")

    rss_list = []

    link_rss = []

    for ri in rss_items:
        if ri.get("class") == ['rss-item']:
            rss_list.append(ri.a.get('href'))
            
    for rl in rss_list:
        req = requests.get(rl)
        data = req.text
        soup = BeautifulSoup(data, "lxml")
        entre = soup.find_all('entry')
        for e in entre :
            link_rss.append(e.link.get('href'))

    return link_rss


def get_information(article_link):
    """Extact informations from all these articles
    
    Arguments:
        article_link {string} -- url of an article
    
    Returns:
        dict -- dict of all informations
    """ 
    
    if "video" in article_link or "/apps/" in article_link or "checknews" in article_link or not re.search(r"\d\d\d\d/\d\d/\d\d", article_link):
        return None

    else:
        
        date_article = re.search(r"\d{4}/\d{2}/\d{2}", article_link)[0]
        date_article = date.datetime.strptime(date_article, "%Y/%m/%d")
        
        diff_date = date.datetime.now() - date_article   
        
        if diff_date.days > 7:
            return None

        else: 
            req = requests.get(article_link)
            req.encoding = "utf-8"
            data = req.text
            soup = BeautifulSoup(data, "lxml")

            if soup.find("div", class_ = "direct-headband") or article_link != req.url:
                return None
            else:               
                balise_title = soup.find("h1")
                balise_title = balise_title.get_text()
                balise_title = re.sub(r"\s\s+", "", balise_title)

                newspaper = "Liberation"
                title = unidecode.unidecode(balise_title)

                author = ""
                for span in soup.find_all('span'):
                    if span.get("class") == ['author']:
                        if(span.a):
                            author = span.a.string
                    if span.get("class") == ['date']:
                        if(span.time):
                            date_p = date.datetime.strptime(span.time.get("datetime"),"%Y-%m-%dT%H:%M:%S").date()
                            date_p = date_p.strftime("%d/%m/%Y")

                content = ""        
                for div in soup.find_all('div'):
                    for p in div.find_all('p'):
                        content += p.get_text() + " "
                content = re.sub("<>", "", content)
                content = unidecode.unidecode(content)
                
                new_article = utilsg4.recovery_article(title, newspaper, [author], date_p, content, " ")

                return new_article

def recuperation_info_libe(file_target = "data/clean/robot/" + str(date.datetime.now().date()) +"/"):
    """Main fonction that get all articles url, extract the informations and create a JSON File
    """

    source = "liberation/"

    link_rss = get_rss_infos()
    
    list_articles = []

    for lr in link_rss:
        if "www.liberation.fr" in lr:
            informations = get_information(lr)
        else:
            informations = None
        if informations:
            list_articles.append(get_information(lr))
    utilsg4.create_json(file_target, list_articles, source, "libe")

    


if __name__ == '__main__':
    recuperation_info_libe()

    

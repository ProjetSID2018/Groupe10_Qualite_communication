# -*- coding: utf-8 -*-
# Group 4 Robot - Lea BESNARD, Laetitia KRUMEICH, Sofian BENJEBRIA,
# Noémie DELOEUVRE , Morgan SEGUELA

import os
import datetime as date
from bs4 import BeautifulSoup
import requests
import re
import unidecode
import g4_utils_v32 as utilsg4
import time

#fileTarget = "C:/Users/lea/Desktop/PROJET/"
#"https://www.ladepeche.fr/services/flux-rss/"

def recovery_link_new_articles_ld(url_rss):
    # We retrieve the rss feeds for each article page.
    # Each HTML-coded article is scanned with beautiful soup.
    soup = utilsg4.recovery_flux_url_rss(url_rss)
    list_link = []
    for link in soup.find_all("a"):
        if link.get("class") == ["rss"]:
            url = link.get("href")
            url = "https://www.ladepeche.fr/" + url
            soup = utilsg4.recovery_flux_url_rss(url)
            items = soup.find_all("item")
            # We retrieve all articles
            for item in items:
                list_link.append(re.search(r"<link/>(.*)", str(item))[1])
    return(list_link)

def recovery_new_articles_ld(file_target = "data/clean/robot/" + str(date.datetime.now().date()) +"/"):

    links = recovery_link_new_articles_ld("https://www.ladepeche.fr/services/flux-rss/")

    list_articles = []
    i = 0
    for article in links:
        new_article = recovery_information_ld(article)
        list_articles.append(new_article)
        if i == 50:
            break
        i += 1
            
    utilsg4.create_json(file_target, list_articles, "ladepeche/", "LD")

def recovery_information_ld(url):

    soup = utilsg4.recovery_flux_url_rss(url)
    # Retrieve the title
    for meta in soup.find_all('meta'):
        if meta.get("property") == 'og:title':
            title = meta.get("content")

    # Retrieve the publication date
    for time in soup.find_all('time'):
        if time.get("itemprop") == 'datePublished':
            date = time.get("itemprop")
            for valeur in re.finditer('[0-9]{2}\/[0-9]{2}\/[0-9]{4}',
                                      str(time)):
                date = valeur.group(0)

    # Retrieve the author
    author = []
    for div in soup.find_all('div'):
        if div.get("class") == ['article_author']:
            author.append(div.span.get_text())

    # Retrieve the content
    content = ""
    for div in soup.find_all('div'):
        if div.get("itemprop") == 'articleBody':
            for p in div.find_all('p'):
                content += p.get_text() + " "

    # Retrieve the theme
    theme = ""
    for h2 in soup.find_all('h2'):
        if h2.get("itemprop") == 'about':
            theme = h2.get_text()

    article = utilsg4.recovery_article(title, 'La Depeche', author,
                                     date, content, theme)
    return(article)

if __name__ == '__main__':
    recovery_new_articles_ld()

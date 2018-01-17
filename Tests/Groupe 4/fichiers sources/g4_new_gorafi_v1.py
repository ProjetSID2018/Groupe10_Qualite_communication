# -*- coding: utf-8 -*-
"""
 Group 4
 Realized by BENJEBRIA Sofian, DELOEUVRE Noémie, MOTHES Céline Mothes,
             SEGUELA Morgan
 V1 : create code
 V1.1 : create function
"""

import unidecode
import re
import g4_utils_v33 as utils


def recovery_information_lg(url):
    """
        Arguments:
            url : string
        Return :
            article : dictionary
        It retrieve for each article the title, newspaper, author, date, theme
    """
    soup = utils.recovery_flux_url_rss(url)

    # Retrieving the title
    balise_title = soup.title.string
    sep = balise_title.split("—")
    title = unidecode.unidecode("—".join(sep[:-1]))

    # Retrieving of author and publication date
    author = []
    for span in soup.find_all('span'):
        if span.get("class") == ['context']:
            author.append(span.a.get_text())
            for valeur in re.finditer('[0-9]{2}\/[0-9]{2}\/[0-9]{4}',
                                      str(span)):
                date_p = valeur.group(0)

    # Retrieving the theme
    for ul in soup.find_all('ul'):
        if ul.get("class") == ['post-categories']:
            for li in ul.find_all('li'):
                theme = li.get_text()

    # Retrieving the content of the article
    contents = ""
    for div in soup.find_all('div'):
        if div.get("class") == ['content']:
            for p in div.find_all('p'):
                contents += p.get_text() + " "
    new_article = utils.recovery_article(title, "Le Gorafi", author, date_p,
                                         contents, theme)
    return(new_article)


def recovery_link_new_articles_lg(url_rss):
    """
        Argument:
            url_rss : string
        Return:
            link_article = list
        Retrieving links of new articles thanks to the rss feed
    """
    soup = utils.recovery_flux_url_rss(url_rss)
    items = soup.find_all("item")
    links_article_gorafi = []
    for item in items:
        links_article_gorafi.append(re.search(r"<link/>(.*)", str(item))[1])
    return(links_article_gorafi)


def recovery_new_article_lg(file_target = "/var/www/html/projet2018/data/clean/robot/"):
    """
         Retrieving new articles thanks to the rss feed
         and create for each article a json
    """
    url_rss = "http://www.legorafi.fr/feed/"
    links_article = recovery_link_new_articles_lg(url_rss)
    list_article = []
    for link_article in links_article:
        new_article = recovery_information_lg(link_article)
        if new_article["theme"] != "Magazine":
            list_article.append(new_article)
    utils.create_json(file_target, list_article, "LeGorafi", "lg")


if __name__ == '__main__':
    recovery_new_article_lg()
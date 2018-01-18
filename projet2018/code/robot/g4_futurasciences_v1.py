""" -*- coding: utf-8 -*-
 Groupe 4
 MOTHES Céline
 HERVE Pierrick
 V1 : create code
 V1.1 : create function
"""
import unidecode
import re
import g4_utils_v32 as utils
import datetime as date


def recovery_information_fusc(url):
    """
        Arguments:
            url : string
        Return :
            article : dictionary
        It retrieve for each article the title, newspaper, author, date, theme
    """
    soup = utils.recovery_flux_url_rss(url)
    # retrieve title
    title = unidecode.unidecode(soup.title.string)
    indice = title.find('|')
    if indice != -1:
        title = title[:indice-1]

    # retrieve the author
    author = []
    for h3 in soup.find_all('h3'):
        if h3.get('itemprop') == 'author':
            author.append(h3.get_text())

    # retrieve date
    publi_date = soup.time.get_text()
    publi_date = re.search(r"\d{2}/\d{2}/\d{4}", publi_date)[0]

    content = ''
    for p in soup.find_all('p'):
        for p2 in re.finditer('py0p5', p.get('class')[-1]):
            content += p.get_text()
    content = unidecode.unidecode(content)

    # retrieve theme
    theme = ''
    for meta in soup.find_all('meta'):
        if meta.get('property') == 'og:url':
            tmp = meta.get('content')[32:]
            indice = tmp.find('/')
            theme = tmp[:indice]

    article = utils.recovery_article(title, 'FuturaSciences', author,
                                     publi_date, content, theme)
    return(article)


def recovery_link_new_articles(url_rss):
    """
        Argument:
            url_rss : string
        Return:
            retrieving links of new articles thanks to the rss feed
    """
    soup = utils.recovery_flux_url_rss(url_rss)
    list_link = []
    for link in soup.find_all("a"):
        if link.get("class") == ["first-capitalize"]:
            list_link.append("https://www.futura-sciences.com" +
                             link.get("href"))
    return(list_link)


def recovery_new_articles_fusc(file_target = "data/clean/robot/" + str(date.datetime.now().date()) +"/"):
    """
        it create a json for each new article
    """
    links = recovery_link_new_articles("https://www.futura-sciences.com/" +
                                       "flux-rss/")
    list_articles = []
    for article in links:
        new_article = recovery_information_fusc(article)
        list_articles.append(new_article)
    utils.create_json(file_target, list_articles, "FuturaSciences/", "fusc")


if __name__ == '__main__':
    recovery_new_articles_fusc()

"""============================================================================
-*- coding: utf-8 -*-
Created on Wed Jan 10 13:57:06 2018

@author: Cedric, Paul, Clément BRANDAO

============================================================================"""

import pickle
from functions.g5_clean_text import clean_symbols
from functions.g5_POS import tokeniz
from functions.g5_named_entity import handing_entity
stop_words = pickle.load(open('C:/Users/mbriens/Documents/M2/Projet/GIT/Groupe5_Filtrage/functions/stopwords.p', 'rb'))
#stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/functions/stopwords.p', 'rb'))

"""============================================================================
    links
============================================================================"""

# LINK ON SERVER
# path_source = '/var/www/html/projet2018/data/clean/robot'
# path_target = '/var/www/html/projet2018/data/clean/filtering'

# TEST LINK
path_source = '../Data/source_press_article'
path_target = '../Data/target_press_article'

"""============================================================================
    import json
============================================================================"""
# Global variable, used many times and only needs to be loaded once
# stop_words = get_stopwords()


def analys_token(article, text_token, entity, entity_, with_stopwords=True, is_title=False):
    """
        Summary:
            This function create the dictionnary.
            Requires global variable "stop_words"
        In:
            - text_token: list of tokenized word
            - entity:
            - entity_:
            - with_stopwords: boolean:
                    * 'True' if stopwords are kept,
                    * 'False' if they are dropped.
        Out:
            - info_token : a dictionnary:
                each compartiment is a dictionnary which contains informations
                for each words
    """
#    info_post = []
    words = []
    lemma = []
    info_token = {}
    post_w = {}
    post_w['word_info'] = []
    info_title=[]
    i = 1
    for token in text_token:
        words.append(token.text)
        lemma.append(token.lemma_)
        if not is_title:
            if str(token.text) in stop_words:
                tag = 'STOPWORD'
            else:
                tag = token.pos_
    
            if str(token) in entity_.keys() and with_stopwords:
                info_token[i] = {'word': token.text,
                                 'lemma': token.lemma_,
                                 'pos_tag': 'Null',
                                 'type_entity': entity_[str(token)],
                                 'position': i,
                                 'title': is_title}
            elif with_stopwords:
                info_token[i] = {'word': token.text,
                                 'lemma': token.lemma_,
                                 'pos_tag': tag,
                                 'type_entity': 'Null',
                                 'position': i,
                                 'title': is_title}
            elif str(token.text) not in stop_words:
                post_w['article_info'] = {'date_publication': article['date_publi'],
                                          'name_newspaper': article['newspaper'],
                                          'author': article['author'],
                                          }
                if str(token) in entity_.keys():
                    post_w['word_info'].append({
                            'word': token.text,
                            'lemma': token.lemma_,
                            'post_tag': 'Null',
                            'type_entity': entity_[str(token)],
                            'position': i,
                            'title': is_title
                                })
                else:
                    post_w['word_info'].append({
                                'word': token.text,
                                'lemma': token.lemma_,
                                'post_tag': tag,
                                'type_entity': 'Null',
                                'position': i,
                                'title': is_title
                                })
    
    #            info_post.append({'word': token.text,
    #                              'lemma': token.lemma_,
    #                              'position': i})
            i += 1
            continue
        else:
#            if str(token.text) in stop_words:
#                tag = 'STOPWORD'
#            else:
            tag = token.pos_
            if str(token.text) not in stop_words:
                if str(token) in entity_.keys():
                    info_title.append({
                                'word': token.text,
                                'lemma': token.lemma_,
                                'post_tag': 'Null',
                                'type_entity': entity_[str(token)],
                                'position': i,
                                'title': is_title
                                    })
                else:
                    info_title.append({
                                'word': token.text,
                                'lemma': token.lemma_,
                                'post_tag': tag,
                                'type_entity': 'Null',
                                'position': i,
                                'title': is_title
                                })
    if not is_title:
        if with_stopwords:
            info_token['words'] = words
            info_token['list_lemma'] = lemma
            return info_token
        else:
            return post_w
    else:
        return info_title


def tag_text(article, f_stopwords=True, isTitle=False):
    
    """
        Summary:
        In:
            - article: content of the article
            /!\ il faudra a l'avenir qu'on soit rigoureux sur le nom des
            arguments : soit utiliser 'text', soit 'content', mais le meme
            de partout.
            - f_stopwords: boolean used with parameter "with_stopwords"
            from analys_token
        Out:
            2 results (see analys_tokens)
            if stopwords = True:
                a dict with:
                    - a list of all the words alongside the list of all the
                    words stems
                    - a list of of each POS-TAG (in which stop-words are tagged
                    as such regardless of what Tag they got)
           if stopwords = False:
               - a list of all the words striped of stopwords
               - a list of the word stems
    """
    if isTitle:
        text = article['title']
    else:
        text = article['content']
    # remove punctuation
    clean_text = clean_symbols(text)
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = handing_entity(tokeniz(clean_text))
    for keys in entity.keys():
        clean_text = clean_text.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(clean_text)
    print(entity,entity_)
    # Here, we decide what to return based on the bool flag f_stopwords
    if f_stopwords:
        return analys_token(article, tokens, entity, entity_, with_stopwords=True, is_title=isTitle)
    else:
        return analys_token(article, tokens, entity, entity_, with_stopwords=False, is_title=isTitle)


def make_article_filtering(article):
    """
        Summary:
            This functions...
        In:
            - article: a dictionnary structured as the source article
            (from gr4: robot)
        Out:
            - res_article: dictionnary structured an article, as a result from
            gr5 (filtering).
    """
    res_art = {}
    res_art['article'] = {
            'date_publication': article['date_publi'],
            'name_newspaper': article['newspaper'],
            'surname_author': article['author']
    }
    res_art['position_words'] = tag_text(
            article['content'],
            f_stopwords=True
    )
    return res_art


# def make_dict_filtering(articles):
#    """
#        Summary:
#            This functions...
#        In:
#            - articles: dictionnary which contains articles
#        Out:
#            - dict_filtering: dictionnary which contains articles
#    """
#    # initialize articles
#    dict_filtering = articles
#    n_art = len(articles)
#    with tqdm(desc='Filtering', total=n_art) as progress_bar:
#        for plain_text in articles:
#            dict_filtering[plain_text]['content'] = tag_text(
#                    articles[plain_text]['content'])
#            progress_bar.update()
#            continue
#    return dict_filtering
#
#
# def make_dict_post_filtering(articles):
#    """
#        Summary:
#            This functions...
#        In:
#            - articles: dictionnary which contains articles
#        Out:
#            - dict_filtering: dictionnary which contains articles
#    """
#    # initialize articles
#    dict_filtering = articles
#    n_art = len(articles)
#    dic = []
#    with tqdm(desc='Filtering', total=n_art) as progress_bar:
#        for plain_text in articles:
#            dict_filtering[plain_text]['content'] = tag_text(
#                    articles[plain_text]['content'], False
#                    )
#            dic.append(dict_filtering[plain_text]['content'])
#            progress_bar.update()
#            continue
#    return dic

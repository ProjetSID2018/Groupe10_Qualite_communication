# Groupe 6 LAFONT Nicolas, QUESNOT Sandy, VAYSSE Robin

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wikipedia as wk


def wikipedia_search(named_entity):
    
    """
    entree : chaine de caractere correspondant a une entite nommee.
    sortie : lien url de la page wikipedia associee a l'entite de type chaine
             de caractere.
    
    Cette fonction effectue une recherche sur wikipedia et retourne l'url de la
    page la plus optimale pour une entite nommee donnee.
    """
    
    
    
    wk.set_lang("fr")
    search = wk.search('Attentats du 11/09/2001')[0].replace(' ', '_')
    url_begin = 'https://fr.wikipedia.org/wiki/'
    return url_begin + search

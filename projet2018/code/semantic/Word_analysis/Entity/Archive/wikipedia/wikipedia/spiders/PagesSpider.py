#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from bs4 import BeautifulSoup
from wikipedia.items import WikipediaItem


class PagesSpider(CrawlSpider):
    name = "wikipedia_pages"
    allowed_domains = ["wikipedia.org"]

    start_urls = [
        "https://fr.wikipedia.org/wiki/"
    ]

    rules = (
            Rule(LinkExtractor(allow="https://fr\.wikipedia\.org/wiki/(.)+(_.+)*",
                        deny=[
                            "https://fr\.wikipedia\.org/wiki/Wikipedia.*",
                            "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal",
                            "https://fr.wikipedia.org/wiki/Oeuvre_libre",
                            "https://fr.wikipedia.org/wiki/Portail",
                        ]),
            callback='parse_wikipedia_page',
            follow = True),
        )

    def parse_wikipedia_page(self, response):
        item = WikipediaItem()
        soup = BeautifulSoup(response.body)

        item['url'] = response.url
        item['title'] = response.css('title::text').extract_first()[:-11]

        return item

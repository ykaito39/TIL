# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:04:02 2019
独学プログラマー 20章
@author: ell_Sub2
"""

import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site_route = site #ルート(UNIXでいう/)
        self.articles = []
        self.articles_title = []
    
    def _parsed(self, site):
        """
        requests.get([url]) -> Get Request Object
        Request.text -> Get HTML Data
        """
        #htmlを取得
        r = requests.get(self.site_route)
        #if r.is_redirect: #うまくいかないでつ
        #    print("piyo")
        requests.
        #パースする
        parser = "html.parser"
        sp = BeautifulSoup(r.text, parser)
        
        return sp
        
    def get_articles_url(self):
        sp = self._parsed(self.site_route)
        #URLにarticles(意訳:記事)が含まれるリンクのみを取得
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                self.articles.append(self.site_route + url)
        print(self.articles)
    
    #残骸
    def get_articles_title(self):
        self.get_articles_url() #全部、開くとリダイレクトされてる...?
        for article in self.articles:
            sp = self._parsed(article)
            for tag in sp.find_all("title"):
                print(tag)
                title = tag.get("")
                self.articles_title.append(title)
        
        print(self.articles_title)
        

url = "https://news.google.jp/"
Scraper(url).get_articles_url()
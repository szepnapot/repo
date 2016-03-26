import wikipedia
import time
from bs4 import BeautifulSoup

class WikiInfo():

    def __init__(self,lang = 'hu',searchinf = {}):
        "set lenguage for 'magyar' if lang_select won't called"
        "wikipedia default is 'english'"
        self.l = lang
        self.i = searchinf


    def lang_select(self,lng):
        "set language for the request"
        print "Language set to:",wikipedia.languages()[lng]
        wikipedia.set_lang(lng)

    def search_info(self,search):
        "title,url put into a dictionary"
        self.s = str(search)
        page = wikipedia.page(search)
        self.cont = page.content
        self.tit = page.title
        self.url = page.url
        return self.cont
        return self.tit
        return self.urlS

    def page_info(self):
        self.i['search'] = (self.tit,self.url)
        return self.i
                
    def txt_write(self):
        "write page content into txt"
        edata = self.cont.encode('utf-8')
        fname = str(self.tit)+"_plain"
        with open(fname+".txt","w") as f:
            f.write(edata)
            print len(edata),"bytes of data written into file.\n",fname
            f.close()

    def html_write(self):
        "write page content into .html"
        fname = str(self.tit)+"_html"
        raw_html = wikipedia.WikipediaPage(self.s).html().encode('utf-8')
        with open(fname+".html","w") as f:
            f.write(raw_html)
            print len(raw_html),"bytes of data written into file.\n"
            f.close()

        

        

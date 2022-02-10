from cmath import inf
from inspect import Attribute
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sqlite3

from app import scrap_link

# scrap shahid for the movies story and info
sq = sqlite3.connect('data.db', check_same_thread=False)
db = sq.cursor()
def scrap(url):
   req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
   web_byte = urlopen(req)
   soup = BeautifulSoup(web_byte, "html.parser")
   div =soup.findAll("div" , attrs = { "class":"content-box" } )
   for i in range(len(div)):
      movie_title=div[  i  ].h3.text
      movie_bage=div[  i  ].find("a").attrs["href"]
      reqe = Request(movie_bage, headers={'User-Agent': 'Mozilla/5.0'})
      webbyte = urlopen(reqe)
      soup2 = BeautifulSoup(webbyte, "html.parser")
      view =soup2.find("a" , attrs = { "class":"btns-play watch-btn primary btn" } ).attrs['href']
      dec=soup2.find('p',class_=None)
      dec_c=str(dec).replace("'","`")
      infos = soup2.find_all("a" , attrs = { "class":"click-all" } )
      info=""
      for i in infos:
         info= info+","+i.text
      poster =soup2.find("a" , attrs = { "class":"poster-image" } ).attrs['style'].split('url')[1]
      db.execute(f"insert into data('title','dec','movie_img','view_link','info') VALUES ('{movie_title}','{dec}','{poster}','{view}','{info}')")
      sq.commit()


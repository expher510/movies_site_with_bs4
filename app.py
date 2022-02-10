from distutils.log import error
from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import re

sq = sqlite3.connect('data.db', check_same_thread=False)
db = sq.cursor()
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def scrap_link(url):
    reqe = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webbyte1 = urlopen(reqe)
    soup3 = BeautifulSoup(webbyte1, "html.parser")
    div3 =soup3.find("iframe" ).attrs['src']
    return div3


app = Flask(__name__)
@app.route("/category/<cat>/")
def category(cat):
   data = db.execute(f"SELECT * FROM data where (info) like '%{cat}%';")
   mdata = data.fetchall()
   return render_template('page.html',mdata=mdata)



@app.route("/search")
def search():
   search=request.args.get("search")
   data = db.execute(f"SELECT * FROM data where (title) like '%{search}%';")
   mdata = data.fetchall()
   return render_template('index.html',mdata=mdata)


@app.route("/",methods=['post','GET'])
def index():
   data = db.execute(f"SELECT * FROM data LIMIT 50 OFFSET 0;")
   mdata = data.fetchall()
   if request.method=="POST":
      link=request.form.get("btn_link")
      video_link=scrap_link(link)
      return render_template('video.html',mdata=mdata,video_link=video_link)
   
   return render_template('index.html',mdata=mdata,page=1)

@app.route("/page/<page>",methods=['post','GET'])
def page(page):
   if page =="":
      return 'error'
   data = db.execute(f"SELECT * FROM data LIMIT 50 OFFSET {(int(page)-1)*50};")
   mdata = data.fetchall()
   n=len(mdata)
   return render_template('page.html',mdata=mdata,page=int(page),n=n)


if __name__=="__main__":
    app.run(debug=True)
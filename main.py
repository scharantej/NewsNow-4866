
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('SELECT * FROM articles ORDER BY publication_date  DESC')
    articles = c.fetchall()
    conn.close()
    return render_template('index.html', articles=articles)

@app.route('/news/<article_id>')
def news(article_id):
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('SELECT * FROM articles WHERE id=?', (article_id,))
    article = c.fetchone()
    conn.close()
    return render_template('news.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)

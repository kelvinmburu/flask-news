from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    hello = 'Hello kelvin'
    return render_template('index.html',hello = hello)

@app.route('/news/<int:news_id>')
def news(news_id):
    
    '''
    View news section that returns the movie details and its data.
    '''
    
    return render_template('news.html',id = news_id)
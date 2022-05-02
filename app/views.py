from flask import render_template
from app import app
from .request import get_article_top_headlines

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting the top articles_results
    tech_articles = get_article_top_headlines('technology')
    #all_articles = get_article_everything('all')
    #all_sources = get_sources()
    print(tech_articles)
    title = 'Home - Welcome to the best News Article Website'
    return render_template('index.html',title = title,tech_articles = tech_articles)

@app.route('/news/<int:news_id>')
def news(news_id):
    
    '''
    View news section that returns the movie details and its data.
    '''
    
    return render_template('news.html',id = news_id)
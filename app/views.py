from flask import redirect, render_template, url_for
from app import app
from .request import get_article_by_source, get_article_everything, get_article_top_headlines, get_sources, search_article
from app import request

# Views


@app.route('/')
def home():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting the top articles_results
    tech_articles = get_article_top_headlines('technology')
    all_articles = get_article_everything('all')
    all_sources = get_sources()

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search', article=search_article))

    return render_template('index.html', tech_articles=tech_articles, all_articles=all_articles, all_sources=all_sources)


@app.route('/worldnews')
def worldnews():
    '''
    View news section that returns the movie details and its data.
    '''

    worldnews = get_article_everything('world')

    return render_template('worldnews.html', worldnews=worldnews)


@app.route('/kenya')
def kenya():
    kenya_articles = get_article_everything('kenya')

    return render_template('kenya.html', kenya_articles=kenya_articles)


@app.route('/business')
def business():
    business_articles = get_article_everything('business')

    return render_template('business.html', business_articles=business_articles)


@app.route('/technology')
def technology():
    technology_articles = get_article_everything('technology')

    return render_template('technology.html', technology_articles=technology_articles)


@app.route('/health')
def health():
    health_articles = get_article_everything('health')

    return render_template('health.html', health_articles=health_articles)


@app.route('/sources')
def sources():
    all_sources = get_sources('sources')
    
    return render_template('sources.html', all_sources=all_sources)

@app.route('/search/<article>')
def search(article):
    searched_articles_list = article.split(" ")
    article_name_format = "+".join(searched_articles_list)
    searched_articles = search_article(article_name_format)
    
    heading = article.upper()
    
    return render_template('search.html',searched_articles=searched_articles,heading=heading)

@app.route('/source/<source_name>')
def source(source_name):
    article_display = get_article_by_source(source_name)
    title = source_name.upper()
    
    return render_template('source.html',article_display=article_display,title=title)
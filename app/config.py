class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&category={}&apiKey={}'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY = 'c17afabafba441d7b8112d9d2614aeb7'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
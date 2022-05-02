class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c17afabafba441d7b8112d9d2614aeb7'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
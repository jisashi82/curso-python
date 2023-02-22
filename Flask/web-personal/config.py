class Config:
    
    #CONFIGURACION BASE
    DEBUG =True
    TESTING=True
    
    #CONFIGURACION DE BASE DE DATOS
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:Admin2013@localhost/my_webpersonal"
    
    
class ProductionConfig(Config):
    DEBUG =False
    
class DevelopmentConfig(Config):
    DEBUG=True
    TESTING=True
    
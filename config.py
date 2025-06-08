class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/voting_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret-key'
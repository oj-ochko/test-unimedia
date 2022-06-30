import env
from sqlalchemy import create_engine


def connect_db():
    engine = create_engine("mysql://" + env.db_user + ":" +
                           env.db_password + "@" + env.db_server, echo=True)
    return engine


def create_db(db):
    engine = connect_db()
    engine.execute("CREATE DATABASE IF NOT EXISTS " + db)  


def use_db(db):
    engine = connect_db()
    engine.execute("USE " + db) 
    return engine

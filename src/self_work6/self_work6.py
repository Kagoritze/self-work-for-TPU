import psycopg2
from config import host, user, password, db_name


class DataBaseManager():

    def __init__(self, host, user, password, db_name):
        self.connection = psycopg2.connect(dbname=db_name,
                                           user=user,
                                           password=password,
                                           host=host)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

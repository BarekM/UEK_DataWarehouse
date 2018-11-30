import mysql.connector

import config


class DatabaseConnection(object):

    def __init__(self):
        self.__db_name = config.db_name
        self.__db_host = config.db_host
        self.__db_user = config.db_user
        self.__db_password = config.db_password

    def __connect(self):
        self.__db_connection = mysql.connector.connect(user=self.__db_user,
                                                       password=self.__db_password,
                                                       host=self.__db_host,
                                                       database=self.__db_name)
        self.__cursor = self.__db_connection.cursor()

    def __disconnect(self):
        self.__db_connection.close()

    def select(self, query):
        self.__connect()
        self.__cursor.execute(query)
        query_results = self.__cursor.fetchall()
        self.__disconnect()
        return query_results

    def input_one(self, query):
        self.__connect()
        self.__cursor.execute(query)
        self.__db_connection.commit()
        self.__disconnect()

    def input_all(self, query):
        self.__connect()
        self.__cursor.executemany(query)
        self.__db_connection.commit()
        self.__disconnect()

    def clear_database(self):
        self.__connect()
        query = 'SHOW TABLES'
        self.__cursor.execute(query)
        query_result = self.__cursor.fetchall()
        for result in query_result:
            query_temp = 'DELETE FROM {0}'.format(result)
            self.__cursor.execute(query_temp)
        self.__db_connection.commit()
        self.__disconnect()

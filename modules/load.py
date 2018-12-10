import glob
import csv

import mysql.connector

import config
from modules.helpers import read_json, dict_to_string


class DatabaseConnection(object):

    def __connect(self):
        self.__db_connection = mysql.connector.connect(user=self.__db_user,
                                                       password=self.__db_password,
                                                       host=self.__db_host,
                                                       database=self.__db_name)
        self.__cursor = self.__db_connection.cursor()

    def __disconnect(self):
        self.__db_connection.close()

    def __init__(self):
        self.__db_name = config.db_name
        self.__db_host = config.db_host
        self.__db_user = config.db_user
        self.__db_password = config.db_password
        self.__connect()

    def select(self, query):
        # self.__connect()
        self.__cursor.execute(query)
        query_results = self.__cursor.fetchall()
        # self.__disconnect()
        print("Query executed: Select")
        return query_results

    def input_one(self, query):
        # self.__connect()
        self.__cursor.execute(query)
        self.__db_connection.commit()
        # self.__disconnect()
        print("Query executed: Insert one")

    def input_all(self, query):
        # self.__connect()
        self.__cursor.executemany(query)
        self.__db_connection.commit()
        # self.__disconnect()
        print("Query executed: Insert all")

    def clear_database(self):
        # self.__connect()
        # query = 'SHOW TABLES'
        # self.__cursor.execute(query)
        # query_result = self.__cursor.fetchall()
        # for result in query_result:
        #     query_temp = 'DELETE FROM {0}'.format(result)
        #     self.__cursor.execute(query_temp)
        # self.__db_connection.commit()
        # self.__disconnect()
        # self.__connect()
        query = 'TRUNCATE table tbl_main'
        self.__cursor.execute(query)
        self.__db_connection.commit()
        # self.__disconnect()
        print("Query executed: Clear DB")

    def __del__(self):
        try:
            self.__disconnect()
        except (ImportError, AttributeError):
            pass


# ======================================================================================================================

def load_files():
    try:
        count_success = 0
        count_try = 0
        count_duplicate = 0
        db_con = DatabaseConnection()
        # build files list to be loaded
        files_list = glob.glob('{0}\\*.json'.format(config.path_transformed))
        for path_file in files_list:
            dict_file = read_json(path_file)
            query_values = dict_to_string(dict_file)
            query = "INSERT INTO tbl_main VALUES({0})".format(query_values)
            try:
                db_con.input_one(query)
                count_success += 1
            except Exception as e:
                if 'Duplicate entry' in str(e):
                    count_duplicate += 1
            count_try += 1
            message = 'Uploaded {0} out of {1}. Duplicates found: {2}'.format(count_success, count_try, count_duplicate)
        exit_code = 0
    except Exception as e:
        exit_code = 1
        message = str(e)
    status = (exit_code, message)
    print(status)
    return status


def output_db():
    dbc = DatabaseConnection()
    query1 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'tbl_main'"
    query2 = "SELECT * FROM tbl_main"
    column_names = dbc.select(query1)
    results = dbc.select(query2)

    lst_column_names = [str(y) for y in [x[0] for x in column_names]]
    output_to_csv = [tuple(lst_column_names)] + results

    with open('{0}\\out.csv'.format(config.path_print), 'w', newline='') as c:
        writer = csv.writer(c)
        writer.writerows(output_to_csv)




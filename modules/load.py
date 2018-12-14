import glob
import csv
import datetime
import shutil

import mysql.connector

import config
from modules.helpers import read_json, dict_to_string, write_pretty_json, get_filename


class _DatabaseConnection(object):

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
        self.__cursor.execute(query)
        query_results = self.__cursor.fetchall()
        return query_results

    def input_one(self, query):
        self.__cursor.execute(query)
        self.__db_connection.commit()

    def clear_database(self):
        query = 'TRUNCATE table tbl_main'
        self.__cursor.execute(query)
        self.__db_connection.commit()

    def __del__(self):
        try:
            self.__disconnect()
        except (ImportError, AttributeError):
            pass


# ======================================================================================================================

def load_files():
    message = ''
    try:
        count_success = 0
        count_try = 0
        count_duplicate = 0
        db_con = _DatabaseConnection()
        # build files list to be loaded
        files_list = glob.glob('{0}\\*.json'.format(config.path_transformed))
        for path_file in files_list:
            dict_file = read_json(path_file)
            query_values = dict_to_string(dict_file)
            query = "INSERT INTO tbl_main VALUES({0})".format(query_values)
            try:
                db_con.input_one(query)
                count_success += 1
                # move file to processed
                path_destination = '{0}\\{1}'.format(config.path_processed, get_filename(path_file))
                shutil.move(path_file, path_destination)
            except Exception as e:
                if 'Duplicate entry' in str(e):
                    count_duplicate += 1
                else:
                    print(str(e))
                    path_destination = '{0}\\{1}'.format(config.path_errors, get_filename(path_file))
                    shutil.move(path_file, path_destination)
            count_try += 1
        message = 'Uploaded {0} out of {1}. Duplicates found: {2}'.format(count_success, count_try, count_duplicate)
        exit_code = 0
    except Exception as e:
        exit_code = 1
        message = str(e)
    if not message:
        message = 'No records to be uploaded.'
    status = (exit_code, message)
    return status


def output_db():
    try:
        dbc = _DatabaseConnection()
        query1 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'tbl_main'"
        query2 = "SELECT * FROM tbl_main"
        column_names = dbc.select(query1)
        results = dbc.select(query2)

        lst_column_names = [str(y) for y in [x[0] for x in column_names]]
        output_to_csv = [tuple(lst_column_names)] + results

        path_output = '{0}\\db_output_{1}.csv'.format(config.path_print, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
        with open(path_output, 'w', newline='') as c:
            writer = csv.writer(c)
            writer.writerows(output_to_csv)
        exit_code = 0
        message = 'Output generated: {0}'.format(path_output)
    except Exception as e:
        message = str(e)
        exit_code = 1
    status = (exit_code, message)
    return status


def output_files():
    try:
        dbc = _DatabaseConnection()
        query1 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'tbl_main'"
        query2 = "SELECT * FROM tbl_main"
        column_names = dbc.select(query1)
        lst_column_names = [str(y) for y in [x[0] for x in column_names]]
        results = dbc.select(query2)

        counter_files = 0
        for r in results:
            dict_current_file = {}
            for x in range(0, len(lst_column_names)):
                dict_current_file[lst_column_names[x]] = r[x]
            path_json = '{0}\\{1}.json'.format(config.path_print_files, dict_current_file['id'])
            write_pretty_json(path_json, dict_current_file)
            counter_files += 1
        exit_code = 0
        message = 'Exported {0} files to directory: {1}'.format(counter_files, config.path_print_files)
    except Exception as e:
        exit_code = 1
        message = str(e)
        print(message)
    status = (exit_code, message)
    return status


def clear_db():
    try:
        dbc = _DatabaseConnection()
        dbc.clear_database()
        exit_code = 0
        message = 'Database cleared.'
    except Exception as e:
        exit_code = 1
        message = str(e)
    status = (exit_code, message)
    return status





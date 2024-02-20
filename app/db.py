import pandas
import pypyodbc as odbc
import sys


class DataBase_User:
    def __init__(self, DRIVER_NAME="SQL SERVER", SERVER_NAME="MALAY-PC\\SQLEXPRESS", DATABASE_NAME="Extra"):
        self.DRIVER_NAME = DRIVER_NAME
        self.SERVER_NAME = SERVER_NAME
        self.DATABASE_NAME = DATABASE_NAME

    def connect(self):
        connection_string = f"""DRIVER={self.DRIVER_NAME};
                        SERVER={self.SERVER_NAME};
                        DATABASE={self.DATABASE_NAME};
                        Trust_Connection=yes;"""
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        return conn, cursor

    def get_table(self, column_name):
        conn, cursor = self.connect()
        cursor.execute(f"SELECT * FROM User_Table Order by {column_name}")
        myresult = cursor.fetchall()
        df = pandas.DataFrame(myresult, columns=('ID', 'Username', 'Password'))
        conn.close()
        return df

    def insert_into_table(self, username, password):
        conn, cursor = self.connect()
        # print(self.search_from_table(username))
        if ((self.search_from_table(username)) is None):
            return False
        else:
            sql_insert_query = f"INSERT INTO User_Table (Username, Password) VALUES ('{username}', '{password}')"
            cursor.execute(sql_insert_query)
            conn.commit()
            return True

        conn.close()

    def delete_from_table(self, username, password):
        conn, cursor = self.connect()
        sql_insert_query = f"DELETE FROM User_Table where (Username='{username}' and Password='{password}')"
        cursor.execute(sql_insert_query)
        conn.commit()
        table = self.get_table("Id")
        print(table)
        conn.close()

    def search_from_table(self, username):
        conn, cursor = self.connect()
        sql_insert_query = f"Select * from  User_Table where (Username='{username}')"
        cursor.execute(sql_insert_query)
        data = cursor.fetchall()
        conn.close()
        if not pandas.DataFrame(data).empty:
            return True
        else:
            return False

    def search_from_table_up(self, username, password):
        conn, cursor = self.connect()
        sql_insert_query = f"Select * from  User_Table where (Username='{username}' and Password='{password}')"
        cursor.execute(sql_insert_query)
        data = cursor.fetchall()
        conn.close()
        if not pandas.DataFrame(data).empty:
            return True
        else:
            return False

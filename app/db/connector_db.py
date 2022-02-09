import mysql.connector as MC
import os


class Connector:
    def __init__(self, host, user, password, database, port):
        """
        Contains the connection data to mysql
        """

        self.conn = MC.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
        )
        self.cursor = self.conn.cursor(buffered=True, dictionary=True)

    def fetch_rows(self, request):
        """
        Execute mysql requests
        Returns the list of data
        """

        self.cursor.execute(request)
        data_list = self.cursor.fetchall()
        return data_list

    def close(self):
        """
        Close cursor
        """
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

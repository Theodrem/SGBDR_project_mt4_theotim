import mysql.connector as MC
import os


class Connector:
    def __init__(self):
        """
        Contains the connection data to mysql
        """

        self.conn = MC.connect(
            host=os.environ.get("HOST_SGBDR"),
            user=os.environ.get("USER_SGBDR"),
            password=os.environ.get("PASSWORD_SGBDR"),
            database=os.environ.get("DATABASE_SGBDR"),
            port=os.environ.get("PORT_SGBDR"),
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

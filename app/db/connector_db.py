import mysql.connector as MC
from decouple import config


class Connector:
    def __init__(self):
        """
        Contains the connection data to mysql
        """

        self.conn = MC.connect(
            host=config("HOST_SGBDR"),
            user=config("USER_SGBDR"),
            password=config("PASSWORD_SGBDR"),
            database=config("DATABASE_SGBDR"),
            port=config("PORT_SGBDR"),
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

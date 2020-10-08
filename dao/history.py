import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class History:

    def __init__(self):
        self.db_host = os.environ.get("DB_HOST")
        self.db_user = os.environ.get("DB_USER")
        self.db_pass = os.environ.get("DB_PASS")
        self.db_name = os.environ.get("DB_NAME")

    def save_history(self, user, query):
        db = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_name)
        cursor = db.cursor()
        try:
            cursor.execute('insert into HISTORY values("%s", "%s")' % \
                (user, query))
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        db.close()

    def get_history(self, user, query):
        db = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_name)
        cursor = db.cursor()
        recent_searches = ""
        try:
            cursor.execute('select * from HISTORY where USER = "%s"' % user)
            results = cursor.fetchall()
            for row in results:
                if query in row[1]:
                    recent_searches = recent_searches + "\n" + str(row[1])
            return recent_searches
        except Exception as e:
            print(e)
        db.close()
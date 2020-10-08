import os
from dotenv import load_dotenv, find_dotenv
import sqlite3

load_dotenv(find_dotenv())


class History:

    """
    A class used to represent User History
    This class is responsible for providing methods to save and retrieve user history from the db.
    Its an abstraction layer for underneath db. Caller does not need to know any db specific requirements.
    
    ...

    Methods
    -------
    save_history(user, query)
        Saves the query for the given user
    
    get_history(user, query)
        Gets the search queries containing the given query for the given user.
    """

    def save_history(self, user, query):
        # create a db connection and a cursor.
        db = sqlite3.connect('discord.db')
        cursor = db.cursor()
        try:
            # execute and commit the query
            cursor.execute('insert into HISTORY values("%s", "%s")' % \
                (user, query))
            db.commit()
        except Exception as e:
            print(e)
            # rollback the query if an exception occurs
            db.rollback()
        # close cursor and db connection.
        cursor.close()
        db.close()

    def get_history(self, user, query):
        # create a db connection and a cursor.
        db = sqlite3.connect('discord.db')
        cursor = db.cursor()
        # Initialize recent searches as empty
        recent_searches = ""
        try:
            # Excute a query to fetch history of the given user.
            cursor.execute('select * from HISTORY where USER = "%s"' % user)
            results = cursor.fetchall()
            # Add queries from the user history which matches the given query to recent_searches.
            # recent_searches contain "\n" separated queries
            for row in results:
                if query in row[1]:
                    recent_searches = recent_searches + "\n" + str(row[1])
            return recent_searches
        except Exception as e:
            print(e)
        # close db connection ans cursor.
        cursor.close()
        db.close()
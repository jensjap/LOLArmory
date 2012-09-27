#!/usr/bin/python

import MySQLdb
import sys

class DBConnector:
    """ usage: object requires server name, username, 
               user password, and database name before 
               connect() method may be called.

    Class will build database connector object """


    def __init__(self):
        """ load instance variables """

        # collect errors
        self.a_errors         = []

        # collect query results
        self.a_dbResults      = []

        # collect number of successful udpates
        self.i_sqlUpdateCount = 0


    def setServerName(self, s_serverName):
        # setter: server name
        self.s_serverName = s_serverName


    def getServerName(self):
        # getter: server name
        return self.s_serverName


    def setDatabaseName(self, s_dbName):
        # setter: database name
        self.s_dbName = s_dbName


    def getDatabaseName(self):
        # getter: database name
        return self.s_dbName


    def setUsername(self, s_username):
        # setter: username
        self.s_username = s_username


    def getUsername(self):
        # getter: username
        return self.s_username


    def setPassword(self, s_password):
        # setter: user password
        self.s_password = s_password


    def __getPassword(self):
        # getter: user password
        return self.s_password


    def connect(self):
        # open database connection
        self.db = MySQLdb.connect("%s,%s,%s,%s") % (self.s_serverName,
                                                    self.s_username,
                                                    self.s_password,
                                                    self.s_dbName)
        # prepare a cursor object using cursor() method
        self.cursor = db.cursor()


    def executeQuery(self, s_query):
        try:
            # execute SQL query
            self.cursor.execute(s_query)

            # commit changes
            self.db.commit()
        except:
            # rollback if there is an error
            self.db.rollback()


    def disconnect(self):
        # close database connection
        self.db.close()

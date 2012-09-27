#!/usr/bin/python

def buildInfoRetrievalSQLQuery(s_charName, i_infoSelection):
    """ usage: buildInfoRetrievalSQLQuery(Character Name, Info Selection)

        Function requires two paramenters. It will build the 
        query to retrieve the selected information based on the 
        Character Name and Info Selection

        return SQL query string """

    d_infoSelection = {
        1: "character_description",
        2: "character_stats"
    }

    s_sqlQuery = "SELECT %s FROM LOLArmory.character \
WHERE name = '%s'" % (d_infoSelection[i_infoSelection], 
                                    s_charName)

    return s_sqlQuery.strip('\n')

def createCharacterSQLQuery(s_charName):
    s_sqlQuery = """INSERT INTO LOLArmory.character (name)
                    VALUES (%s)
                    LIMIT 1""" % s_charName
    return s_sqlQuery
    
# ### Unit TEST ###
# s_charName      = 'jens'
# i_infoSelection = 2

# sqlStatement = buildInfoRetrievalSQLQuery(s_charName, i_infoSelection)
# print(sqlStatement)

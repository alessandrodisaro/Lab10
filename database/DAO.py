from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select * from country c """
        cursor.execute(query, ())
        results = []
        for row in cursor:
            results.append(Country(row["CCode"], row["StateAbb"], row["StateNme"]))
        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def getAllConfiniInAnno(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select *
                    from contiguity c 
                    where c.year < %s
                    and c.conttype = 1"""
        cursor.execute(query, (anno,))
        results = []
        for row in cursor:
            results.append(Contiguity(**row))
        cursor.close()
        cnx.close()
        return results

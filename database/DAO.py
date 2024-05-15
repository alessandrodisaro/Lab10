from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select distinct (c.CCode) , c.StateAbb  , c.StateNme 
                    from country c , contiguity c2 
                    where c2.year <= %s
                    and c.CCode = c2.state1no
                    order by c.StateNme 
                     """
        cursor.execute(query, (anno,))
        results = []
        for row in cursor:
            results.append(Country(row["CCode"], row["StateAbb"], row["StateNme"]))
        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def getAllEdges(anno, idMap):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # query = """select c.dyad,c.state1no,c.state1ab,c.state2no,c.state2ab,c.year,c.conttype,c.version
        #     from contiguity c , country cc
        #     where c.year < %s
        #     and c.state1no = cc.CCode
        #     and c.conttype = 1
        #     order by cc.StateNme  """

        query = """select distinct state1no, state2no
                       from contiguity c 
                       where conttype = 1
                       and  year <= %s
                       and state1no < state2no """
        cursor.execute(query, (anno,))
        results = []
        for row in cursor:
            results.append(Contiguity(idMap[row["state1no"]], idMap[row["state2no"]]))
        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def getAllConfiniInAnno(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # query = """select c.dyad,c.state1no,c.state1ab,c.state2no,c.state2ab,c.year,c.conttype,c.version
        #     from contiguity c , country cc
        #     where c.year < %s
        #     and c.state1no = cc.CCode
        #     and c.conttype = 1
        #     order by cc.StateNme  """

        query = """select distinct state1no, state2no
                    from contiguity c
                    where conttype = 1
                    and  year <= %s
                    and state1no < state2no """
        cursor.execute(query, (anno,))
        results = []
        for row in cursor:
            results.append(Contiguity(row["state1no"], row["state2no"]))
        cursor.close()
        cnx.close()
        return results

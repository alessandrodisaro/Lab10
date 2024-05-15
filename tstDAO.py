from database.DAO import DAO

nodi = DAO.getAllCountries(2000)
for nodo in nodi:
    print(nodo)
print(len(nodi))
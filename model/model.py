import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}  # forse inutile
        self._loadAllCountries()

    def detNumNodes(self):
        return self._grafo.number_of_nodes()

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def _loadAllCountries(self):
        nodi = DAO.getAllCountries()
        self._grafo.add_nodes_from(nodi)



    def getStatiConfinanti(self,anno):
        edges = DAO.getAllConfiniInAnno(anno)
        for arco in edges:
            self._grafo.add_edge(arco.state1no, arco.state2no)

        results = set()
        for u, v in self._grafo.edges:
            results.add((u, self._grafo.degree(u)))
        return results

    def getComponentiConesse(self):
        return nx.number_connected_components(self._grafo)




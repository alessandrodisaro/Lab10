import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}  # forse inutile
        self._loadAllCountries()
        for country in self._grafo.nodes:
            self._idMap[country.CCode] = country

    def detNumNodes(self):
        return self._grafo.number_of_nodes()

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def _loadAllCountries(self):
        nodi = DAO.getAllCountries()
        self._grafo.add_nodes_from(nodi)

    def getTuttiStati(self):
        return DAO.getAllCountries()

    def getStatiConfinanti(self, anno):
        edges = DAO.getAllConfiniInAnno(anno)
        for arco in edges:
            self._grafo.add_edge(arco.state1no, arco.state2no)

        results = set()
        for u, v in self._grafo.edges:
            results.add((self._idMap[u], self._grafo.degree(u)))
        return results

    def getComponentiConesseNCC(self):  # usato per avere il numero di cmponenti connesse nel controller (parte del 1' punto)
        return nx.number_connected_components(self._grafo)

    def getComponentiConesseDFS(self, part):
        self._riscriviGrafo()
            ####
        nodo = self._idMap[int(part)]
            ####
        edges = nx.dfs_edges(self._grafo, self._idMap[int(part)])
        # tree = nx.node_connected_component(self._grafo, self._idMap[int(part)])
        # results = []
        # for elem in edges:
        #     results.append(elem)                    # prima = results.append(elem)
        # return results
        #
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited



    def _riscriviGrafo(self):
        self._grafo.clear()
        self._loadAllCountries()
        self._grafo.add_edges_from(self.getStatiConfinanti(2017))  # prendo tutte le connessioni fino al 2016, che e' il imite dei records nel db





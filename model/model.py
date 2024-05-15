import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}  # forse inutile


    def detNumNodes(self):
        return self._grafo.number_of_nodes()

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    # def _inserisciNodi(self, anno):
    #     self._loadAllCountries(anno)
    #     for country in self._grafo.nodes:
    #         self._idMap[country.CCode] = country

    # def _loadAllCountries(self, anno):
    #     nodi = DAO.getAllCountries(anno)
    #     self._grafo.add_nodes_from(nodi)

    # def getTuttiStati(self, anno):
    #     return DAO.getAllCountries(anno)

    def getStatiConfinanti(self, anno):
        edges = DAO.getAllConfiniInAnno(anno)
        for arco in edges:
            self._grafo.add_edge(arco.state1no, arco.state2no)
        print(self._grafo.number_of_edges())
        results = set()
        for u, v in self._grafo.edges:
            results.add((u, self._grafo.degree(u)))
        return results


    ##########
    def buildGraph(self, anno):
        self._grafo.clear()
        nodi = DAO.getAllCountries(anno)
        for nodo in nodi:
            self._idMap[nodo.CCode] = nodo
        self._grafo.add_nodes_from(nodi)
        archi = DAO.getAllEdges(anno, self._idMap)
        for arco in archi:
            self._grafo.add_edge(arco.state1no, arco.state2no)
    #########

    def getPartiConesseNCC(self):  # usato per avere il numero di cmponenti connesse nel controller (parte del 1' punto)
        return nx.number_connected_components(self._grafo)

    def getComponentiConesseDFS(self, part):
        edges = nx.dfs_edges(self._grafo, self._idMap[int(part)])
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    def _prendiStati(self, anno):
        return DAO.getAllCountries(anno)


    # def inizializzazioneRicorsione(self, partenza):
    #     results = []
    #     results = self.recursion([], partenza, [])
    #     return results
    #
    # def recursion(self,parziale, partenza, destinazioni):
    #     #condizione terminale
    #     if( parziale[ultimo_elem].degree==0)  #utlimo nodo aggiunto njell esplorazione
    #         destinazioni.append(nodo)
    #         ####
    #         print(nodo)
    #         ####
    #     else:
    #         parziale.append(self._grafo.successor)
    #         self.recursion(parziale,parziale[ultimo_nodo], destinazioni)
    #         parziale.pop()
    #



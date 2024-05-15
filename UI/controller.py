import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._dd_stato_value = None

    def handleCalcola(self, e):

        confini = self._model.getStatiConfinanti(self._view._txtAnno.value)
        self._view._txt_result.clean()
        if confini is not None:
            self._view._txt_result.controls.append(ft.Text(f"Grafico creato correttamente"))
        else:
            self._view._txt_result.controls.append(ft.Text(f"Grafico NON e' stato creato correttamente"))

        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getComponentiConesseNCC()} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito i dettagli sui nodi"))

        for arco in confini:
            self._view._txt_result.controls.append(ft.Text(f"{arco[0]} -- {arco[1]} vicini"))

        self._view.update_page()

    def handleRicerca(self, e):
        # metodo dfs
        raggiungibili = self._model.getComponentiConesseDFS(self._view._dd_StatoIn.value)
        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Gli stati raggiungibili a partire da {self._model._idMap[int(self._view._dd_StatoIn.value)]}"))
        # COL TREE
        # for i in range(1, len(raggiungibili)):  # prima = for paese in raggiungibili:
        #     self._view._txt_result.controls.append(ft.Text(raggiungibili[i][1]))  # prima = self._view._txt_result.controls.append(ft.Text(paese[1]))
        # self._view.update_page()
        # COL VISITED
        for i in range(1, len(raggiungibili)):
            self._view._txt_result.controls.append(ft.Text(raggiungibili[i].StateNme))
        self._view.update_page()

    #     self._view._txt_result.controls.append(ft.Text(raggiungibili[i][1]))  # prima = self._view._txt_result.controls.append(ft.Text(paese[1]))
    # self._view.update_page()

    def loadDdStati(self):
        stati = self._model.getTuttiStati()
        for stato in stati:
            self._view._dd_StatoIn.options.append(
                ft.dropdown.Option(key=stato.CCode, text=stato.StateNme, on_click=self.reaDdStato))
        self._view.update_page()

    def reaDdStato(self, e):
        self._dd_stato_value = e.control.data


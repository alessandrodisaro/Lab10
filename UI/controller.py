import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):

        confini = self._model.getStatiConfinanti(self._view._txtAnno.value)
        self._view._txt_result.clean()
        if confini is not None:
                self._view._txt_result.controls.append(ft.Text(f"Grafico creato correttamente"))
        else:
            self._view._txt_result.controls.append(ft.Text(f"Grafico NON e' stato creato correttamente"))

        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getComponentiConesse()} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito i dettagli sui nodi"))

        for arco in confini:
            self._view._txt_result.controls.append(ft.Text(f"{arco[0]} -- {arco[1]} vicini"))

        self._view.update_page()

    def handleRicerca(self):
        pass

    def loaDdStati(self):
        stati = self._model.getTuttiStati()
        for stato in stati:
            self._view._dd_StatoIn.controls.Option.append(options=[key= , value= ])




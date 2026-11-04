import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dd(self):
        biblioteche=self._model.get_biblioteche()

        self._view.dd_biblioteche.options.append(ft.dropdown.Option(text="Nessun filtro"))

        for biblioteca in biblioteche:
            self._view.dd_biblioteche.options.append(ft.dropdown.Option(text=biblioteca))

        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO

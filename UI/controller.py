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
    def popola_dd_biblioteche(self):
        biblioteche=self._model.get_biblioteche()

        self._view.dd_biblioteche.options.append(ft.dropdown.Option(text="Nessun filtro"))

        for biblioteca in biblioteche:
            biblioteca_nome=biblioteca.nome
            self._view.dd_biblioteche.options.append(ft.dropdown.Option(text=biblioteca_nome))

        self._view.update()

    def popola_dd_generi(self):
        generi=self._model.get_generi()

        self._view.dd_generi.options.append(ft.dropdown.Option(text="Nessun filtro"))

        for genere in generi:
            self._view.dd_generi.options.append(ft.dropdown.Option(text=genere))

        self._view.update()


    # CALLBACKS DROPDOWN
    # Qui metto le funzioni che si eseguono in automatico quando l'utente seleziona dalla dropdown (on_select)
    # Quindi si salvano la scelta dell'utente

    def get_biblioteca(self,e):
        self.biblioteca_selezionata=self._view.dd_biblioteche.value
        if self.biblioteca_selezionata=="Nessun filtro" or self.biblioteca_selezionata=="":
            self.biblioteca_selezionata = None

        print(f"Biblioteca selezionata: {self.biblioteca_selezionata}")

    def get_genere(self,e):
        self.genere_selezionato=self._view.dd_generi.value
        if self.genere_selezionato=="Nessun filtro" or self.genere_selezionato=="":
            self.genere_selezionato = None

        print(f"Genere selezionato: {self.genere_selezionato}")

    # AZIONE: MOSTRA LIBRI
    # Qui metto la funzione legata al pulsante che cerca i libri

    def handler_filtro(self):

        genere=self.genere_selezionato
        biblioteca=self.biblioteca_selezionata
        libri_filtrati=self._model.get_libri_filtrati(biblioteca,genere)

        self._view.lista_libri_filtrati.controls.clear()

        if libri_filtrati:
            for el in libri_filtrati:
                libro_in_testo=ft.Text(str(el))
                self._view.lista_libri_filtrati.controls.append(libro_in_testo)
        else:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio")

        self._view.update()

from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    # Funzione che prende dal dao la lista dei libri in base alla biblioteca e al genere selezionata
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        dao=LibroDAO()
        libri_filtrati=dao.filtra_libri_dal_db(biblioteca,genere)

        return libri_filtrati

    # Funzione che prende dal dao la lista di tutti i libri, e poi crea una lista di tutti i generi presenti che ritorna
    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        print("Prendendo i generi ...")
        dao=LibroDAO()
        libri=dao.leggi_libri_dal_db()

        generi=[]
        for libro in libri:
            if libro.genere not in generi:
                generi.append(libro.genere)

        return generi

    # --- BIBLIOTECHE ---
    # Funzione che prende dal dao la lista di tutte le biblioteche e la ritorna
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        print("Prendendo le biblioteche ...")
        biblioteche=BibliotecaDAO()

        return biblioteche.leggi_biblioteche_dal_db()

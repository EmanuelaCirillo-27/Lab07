from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # Funzione che interroga il database facendosi dare tutti i libri e poi restituirne una lista
    def leggi_libri_dal_db(self):

        cnx = DBConnect.get_connection()

        if cnx is not None:

            query=""" SELECT *
                    FROM libro"""

            cursor = cnx.cursor()
            cursor.execute(query)

            libri=[]
            for row in cursor:
                libro=Libro(*row)
                libri.append(libro)

            cursor.close()
            cnx.close()

            return libri

        else:
            return "Nessun database trovato"

    # Funzione che interroga il database facendosi dare tutti quei libri che rispettano biblioteca e genere dati,
    # gestendo anche l'opzione "Nessun filtro" che indica che il relativo filtro (nome della biblioteca o genere)
    # non è attivo (COALESCE)
    def filtra_libri_dal_db(self, biblioteca, genere):

        cnx = DBConnect.get_connection()

        if cnx is not None:
            query=""" SELECT l.*
                    FROM libro l, biblioteca b
                    WHERE b.id = l.id_biblioteca
                    AND b.nome = COALESCE(%s, b.nome)
                    AND l.genere = COALESCE(%s, l.genere)
                        """

            cursor = cnx.cursor()
            cursor.execute(query,(biblioteca,genere))

            libri_filtrati=[]
            for row in cursor:
                libro=Libro(*row)
                libri_filtrati.append(libro)

            cursor.close()
            cnx.close()

            return libri_filtrati

        else:
            return "Nessun database trovato"

#AND l.genere = COALESCE(%s, l.genere) AND b.nome = COALESCE(%s, b.nome)
#AND b.nome= '{biblioteca}' AND l.genere= '{genere}'
from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # Funzione che interroga il database facendosi dare tutte le biblioteche e poi restituirne una lista
    def leggi_biblioteche_dal_db(self):

        #db=DBConnect()
        #cnx=db.get_connection()
        cnx= DBConnect.get_connection()

        if cnx is not None:

            query=""" SELECT *
                        FROM biblioteca"""

            cursor=cnx.cursor()
            cursor.execute(query)

            biblioteche=[]

            for row in cursor:
                biblioteca=Biblioteca(*row)
                biblioteche.append(biblioteca)

            cursor.close()
            cnx.close()

            return biblioteche

        else:
            return "Nessun database trovato"


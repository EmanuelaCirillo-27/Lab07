from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

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

#AND l.genere = COALESCE(%s, l.genere) AND b.nome = COALESCE(%s, b.nome)
#AND b.nome= '{biblioteca}' AND l.genere= '{genere}'
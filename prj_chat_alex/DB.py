import libraries as L

class DataBase():
    def __init__(self):
        self.db = L.mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Ventilatoregallinatrust04_"
        )

        #generazione cursore
        self.cursor = self.db.cursor(buffered = True)

        #creazione database se non esiste
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS Chat_PRJ")

        #chiudo il db così da poter riaprire direttamente il database invece dell'istanza (procedimento utile solo al primo avvio ma rimane la soluzione migliore)
        self.db.close()

        #mi connetto al database
        self.db = L.mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Ventilatoregallinatrust04_",
            database = "Chat_PRJ"
        )

        #genero il cursore
        self.cursor = self.db.cursor(buffered = True)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contatti (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(255), hostname VARCHAR(255), chiave VARCHAR(255))")

        #tabella messaggi, contiene tutti i messaggi ricevuti ed inviati l'orario e il mittente
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Messaggi (messaggi VARCHAR(512), data DATETIME, mittente INT, destinatario INT, id INT AUTO_INCREMENT PRIMARY KEY)")

        #faccio un controllo per id, se l'ip NULL non viene trovato significa che l'utente non è registrato e quindi apre la finestra per la registrazione 
        self.cursor.execute("SELECT * FROM contatti WHERE id = 1")
    
    def insert_name(self, values):
        sql =  "INSERT INTO contatti (hostname) VALUES (%s)"
        self.cursor.execute(sql, values)
        self.db.commit()
        
    def Invio(self, values):
        sql = "INSERT INTO messaggi (messaggi, data, mittente, destinatario) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, values)
        self.db.commit()
    
    def Carica(self, values):
        sql = "SELECT data,messaggi,mittente FROM messaggi WHERE mittente = %s OR destinatario = %s"
        contatto = (values[2], values[2], )
        self.cursor.execute(sql, contatto)
        result = self.cursor.fetchall()
        return result
    
    def Treeview_Print(self):
        self.cursor.execute("SELECT hostname,ip,id FROM contatti")
        risultato = self.cursor.fetchall()
        return risultato
        
    def ctx_Delete_Contact(self, values):
        sql = "DELETE FROM contatti WHERE id = %s"
        self.cursor.execute(sql, values)
        self.db.commit()
        
    def Delete_Contact(self, values):
        sql =  "DELETE FROM contatti WHERE hostname = %s AND ip = %s"
        self.cursor.execute(sql, values)
        self.db.commit()
        
    def ctx_Update_Contact(self, values):
        sql = "UPDATE contatti SET hostname = %s WHERE id = %s"
        self.cursor.execute(sql, values)
        self.db.commit()
        
    def Update_Contact(self, values):
        sql =  "UPDATE contatti SET hostname = %s WHERE hostname = %s AND ip = %s"
        self.cursor.execute(sql, values)
        self.db.commit()
        values = (values[0], values[2], )
        sql = "SELECT id FROM contatti WHERE hostname = %s AND ip = %s"
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()
    
    def Insert_Contact(self, values):
        sql =  "INSERT INTO contatti (hostname, ip) VALUES (%s, %s)"
        self.cursor.execute(sql, values)
        self.db.commit()
        sql = "SELECT id FROM contatti WHERE hostname = %s AND ip = %s"
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        return result
    
    def Update_My_Contact(self, values):
        sql =  "Update contatti SET hostname = %s WHERE id = 1"
        self.cursor.execute(sql, values)
        self.db.commit()
        
    def Control(self):
        self.cursor.execute("SELECT * FROM contatti WHERE id = 1")
        result = self.cursor.fetchone()
        return result
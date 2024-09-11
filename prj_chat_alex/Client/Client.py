"""
Questo modulo rappresente il client nella comunicazione tra due utenti.
"""
import socket

#Uso una funzione per inviare i dati. 
#In questo modo evito di ricevere indirizzo ip e messaggio da inviare tramite command line arguments
#La funzione viene chiamata esclusivamente da funzioni esterne
def send(msg, network):
    #decido la porta 1060 per l'invio dei dati
    port = 1060

    #creo una socket tcp (passando alla funzione socket l'argomento "socket.SOCK_STREAM")
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #mi connetto al server all'indirizzo ip network alla porta port
    sck.connect((network, port))

    sck.send(msg.encode("UTF-8"))

    #ricevo dal server una risposta
    data = sck.recv(1024)

    print("the server sent: ", data.decode("UTF-8"))

    #chiudo la connessione
    sck.close()


#serve per il testing delle socket
if __name__ == "__main__":
    send("ciao", '127.0.0.1')
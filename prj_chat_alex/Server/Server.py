"""
Questo modulo rappresenta il server nella comunicazione tra due utenti.
L'esecuzione della funzione contenuta all'interno del modulo verrà avviata 
insieme all'applicazione e verra interrotta all'interruzione dell'applicazione stessa
"""
import socket


def server(ipAddress):
    #creo una socket tcp(passando alla funzione socket l'argomento "socket.SOCK_STREAM")
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bindo la scoket al mio indirizzo ip e alla porta 1060
    sck.bind((ipAddress, 1060))

    #metto la socket in attesa di una richiesta di comunicazione
    sck.listen(11)

    print("listening at: ", sck.getsockname())

    while True:
        #quando ricevo una richiesta di connessione accetto e creo una socket per rispondere, 
        #inoltre mi salvo l'indirizzo nella variabile addr
        connectionSck, addr = sck.accept()

        #decodifico il messaggio
        data = connectionSck.recv(1024).decode("UTF-8")

        print("recived from: ", addr)

        #salvo in addeStr l'indirizzo ip (lo slicing serve ad eliminare la porta usata dal mittente)
        addrStr = str(addr)[2:str(addr).find(',')-1]

        #aggiungo al messaggio l'indirizzo ip del mittente ed un separatore '//'
        data = addrStr + "//" + data

        #salvo in un file temporaneo l'indirizzo del mittente e il messaggio ricevuto
        file = open("tempFile.txt", "w")
        file.write(data)
        file.close()
        

        #mando al client la risposta "recived" per segnalare che tutto è andato a buon fine 
        ans = "recived"
        connectionSck.send(ans.encode("UTF-8"))

        #chiudo la connessione
        connectionSck.close()

#serve per il testing delle socket
if __name__ == '__main__':
    server('127.0.0.1')

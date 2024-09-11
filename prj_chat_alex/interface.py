import libraries as L
        
class Root():
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Inizializzazione classe, genero DB e finestra
    def __init__(self):
        self.DB = L.DataBase()
        self.Root_win = L.Tk()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#funzione Caricamento messaggi da DB
    def Carica(self):
        result = self.DB.Carica(self.values)
        for x in result:
            self.msg.configure(state = L.NORMAL)
            if x[2] == 1:
                self.msg.insert(L.END,"\n")
                self.msg.insert(L.END, x[0])
                self.msg.insert(L.END, "\n" + "io-> " + x[1])   
            else:
                self.msg.insert(L.END, "\n")
                self.msg.insert(L.END, x[0])
                self.msg.insert(L.END, "\n" + self.values[0] + "-> " + x[1])
            self.msg.configure(state = L.DISABLED)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#funzione Invio messaggi e caricamento messaggi su DB
    def Invio(self, event):
        self.msg.configure(state = L.NORMAL)
        invio = L.time.strftime("%H:%M ") + "io-> " + self.casella_testo.get()
        selected = self.tabella.focus()
        dest = self.tabella.item(selected, 'values')
        values = (self.casella_testo.get(), L.datetime.datetime.now(), 1, dest[2], )
        self.msg.insert(L.END, "\n" + invio)
        self.msg.configure(state = L.DISABLED)
        self.DB.Invio(values)
        self.casella_testo.delete(0 , L.END)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Chiamata Popup menu
    def ctx_menu_popup(self, event):
        try:
            self.ctx_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.ctx_menu.grab_release()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Finestra Chat
    def Chat(self, event):
        selected = self.tabella.focus()
        self.values = self.tabella.item(selected, 'values')
        #se il valore dell'ip è presente apro la chat 
        if self.values[1] != 'None':
            #genero la finestra della chat e blocco la finestra contatti
            self.Chat = L.Toplevel(self.Root_win)
            self.Chat.grab_set()
            #creo i 2 frame necessari per la struttura della finestra
            self.frame1 = L.Frame(self.Chat)
            self.frame1.pack(fill = L.BOTH, expand = True)
            self.frame2 = L.Frame(self.Chat, height = 150)
            self.frame2.pack(fill = L.X)
            #imposto il nome della finestra come il nome del contatto e imposto dimensioni e posizione
            self.Chat.title(self.values[0])
            self.Chat.geometry('400x600+660+150')
            #da vedere Chat.iconbitmap('')
            self.Chat.resizable(False, True)
            
            #creo la finestra di dialogo
            self.msg = L.Text(self.frame1, state = L.DISABLED)
            self.msg.pack(fill = L.BOTH, expand = True)
            self.Carica()

            #casella di testo e pulsante per l'invio dei messaggi
            self.casella_testo = L.Entry(self.frame2)
            self.button = L.Button(self.frame2, text = "Invia")
            self.button.pack(fill = L.X, expand = True, side = L.RIGHT)
            self.casella_testo.pack(ipady = 3, fill = L.X, expand = True, side = L.LEFT)

            #imposto il focus sulla casella di testo
            self.casella_testo.focus()
            
            self.button.bind("<Button-1>", self.Invio)
            self.casella_testo.bind("<Return>", self.Invio)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Finestra configurazione iniziale
    def Config_Window(self):
        def insert_name(event):
            #comando sql con parametro da inserire(nome utente) e esecuzione, fa il commit e chiude la finestra
            if name_entry.get() != "":
                values = (name_entry.get(), )
                self.DB.insert_name(values)
                result = self.DB.Control()
                values = (result[2], result[1], result[0], )
                self.tabella.insert('', L.END, values = values)
                first_screen.destroy()
        first_screen = L.Toplevel(self.Root_win)
        first_screen.grab_set()
        first_screen.attributes('-topmost', 1)
        first_screen.title("Inizializzazione")
        first_screen.geometry('400x200+760+300')
        #da vedere first_screen.iconbitmap('')
        first_screen.resizable(False, False)

        #richiedo il nome
        label = L.Label(first_screen, text = 'Inserisci Nome', font = ('Plantagenet Cherokee', 18), justify = 'center').pack()

        #variabile di appoggio, entry dove verrà scritto il noome
        name = L.StringVar()
        name_entry = L.ttk.Entry(first_screen, textvariable = name)
        name_entry.pack(padx = 5, pady = 5)

        #bottone per la conferma, non metto il command qui per poter usare il doppio comando (enter e button, altrimenti la funzione che richiede un event non funzionerebbe col pulsante)
        name_button = L.ttk.Button(first_screen, text = "Conferma")
        name_button.pack(pady = 10, padx = 10)

        #focus sulla casella di testo
        name_entry.focus()

        #se viene premuto invio o il pulsante chiama la funzione
        name_entry.bind("<Return>", insert_name)
        name_button.bind("<Button-1>", insert_name)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Finestra root
    def Root_Window(self):
        
        self.Root_win.title("Contatti")
        self.Root_win.geometry('650x600+660+100')
        self.Root_win.minsize(650,600)
        #da vedere root_window.iconbitmap('')

        #impposto un menu
        self.menubar = L.Menu(self.Root_win)
        self.Root_win.config(menu = self.menubar)
        self.file_menu = L.Menu(self.menubar, tearoff = 0)

        #inserisco le opzioni e le rispettive funzioni(vedi sopra per le funzioni)
        self.menubar.add_cascade(label = 'Aggiungi Contatto', command = lambda : L.Window.Insert_Contact(self))
        self.menubar.add_cascade(label = 'Modifica Contatto', command = lambda : L.Window.Update_Contact(self))
        self.menubar.add_cascade(label = 'Cancella Contatto', command = lambda : L.Window.Delete_Contact(self))
        self.menubar.add_cascade(label = 'Cambia Nome', command = lambda : L.Window.Update_My_Contact(self))

        #menu contestuale
        self.ctx_menu = L.Menu(self.Root_win, tearoff = 0)
        self.ctx_menu.add_command(label = "Cancella Contatto", command = lambda : L.Window.ctx_Delete_Contact(self))
        self.ctx_menu.add_separator()
        self.ctx_menu.add_command(label = "Modifica Contatto" , command = lambda : L.Window.ctx_Update_Contact(self))

        #grazie al treeview genero la tabella e le colonne
        colonne = ('hostname', 'ip', 'id')
        self.tabella = L.ttk.Treeview(self.Root_win, columns = colonne, show = 'headings')
        self.tabella.heading('hostname', text = 'Nome')
        self.tabella.heading('ip', text = 'IP')
        self.tabella.heading('id', text = 'ID')

        risultato = self.DB.Treeview_Print()
        
        #stampo la tabella e la inserisco nella finestra con grid
        for riga in risultato:
            self.tabella.insert('', L.END, values = riga)
            
        self.tabella.grid(row = 0, column = 0, sticky = 'nwse')
        
        res = self.DB.Control()
        if not res:
            self.Config_Window()

        self.tabella.bind("<Button-3>", self.ctx_menu_popup)
        self.tabella.bind("<Double-1>", self.Chat)

        self.Root_win.mainloop()
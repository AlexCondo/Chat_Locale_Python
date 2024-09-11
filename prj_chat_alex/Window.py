import libraries as L

def ctx_Delete_Contact(self):
    #prendo il valore della casella selezionata nella tabella
    selected = self.tabella.focus()
    values = self.tabella.item(selected, 'values')
    #se le entry non sono vuote faccio l'inserimento e aggiorno la tabella
    if values != L.NULL and values[1] != 'None':
        values = (values[2], )
        self.DB.ctx_Delete_Contact(values)
        x = self.tabella.selection()[0]
        self.tabella.delete(x)
        
def Delete_Contact(self):
    def delete_contact(event):
        #se le entry non sono vuote cancello il contatto e aggiorno la tabella
        if name_entry.get() != "" and ip_entry.get() != "":
            values = (name_entry.get(), ip_entry.get())
            self.DB.Delete_Contact(values)
            for x in self.tabella.get_children():
                Valore = self.tabella.item(x)
                if(Valore["values"][0] == name_entry.get() and str(Valore["values"][1]) == ip_entry.get()):
                    self.tabella.delete(x)
        Delete_window.destroy()
    
    Delete_window = L.Toplevel(self.Root_win)
    Delete_window.grab_set()
    Delete_window.title("Cancella Contatto")
    Delete_window.geometry('400x200+760+300')
    #da vedere update_window.iconbitmap('')
    Delete_window.resizable(False, False)

   #richiedo il nome
    label = L.Label(Delete_window, text = 'Inserisci Nome', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto il nome
    name = L.StringVar()
    name_entry = L.ttk.Entry(Delete_window, textvariable = name)
    name_entry.pack(padx = 5, pady = 5)

    #richiedo l'ip
    label = L.Label(Delete_window, text = 'Inserisci IP', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto l'ip
    ip = L.StringVar()
    ip_entry = L.ttk.Entry(Delete_window, textvariable = ip)
    ip_entry.pack(padx = 5, pady = 5)

    #bottone per la conferma, non metto il command qui per poter usare il doppio comando (enter e button, altrimenti la funzione che richiede un event non funzionerebbe col pulsante)
    name_button = L.ttk.Button(Delete_window, text = "Conferma")
    name_button.pack(pady = 10, padx = 10)

    #focus sulla casella di testo
    name_entry.focus()

    #se viene premuto invio o il pulsante chiama la funzione
    ip_entry.bind("<Return>", delete_contact)
    name_button.bind("<Button-1>", delete_contact)
        
def ctx_Update_Contact(self):
    def update_contact(event):
        #prendo il valore della casella selezionata nella tabella
        selected = self.tabella.focus()
        values = self.tabella.item(selected, 'values')           
        id = values[2]
        values = (new_name_entry.get(), values[1], )
        #se le entry non sono vuote faccio la modifica e aggiorno la tabella
        if values != '' and values[1] != 1:
            self.DB.ctx_Update_Contact(values)
            self.tabella.item(selected, text ="", values = (new_name_entry.get(), values[1], id))
        update_my_window.destroy()
        
    update_my_window = L.Toplevel(self.Root_win)
    update_my_window.grab_set()
    update_my_window.title("Modifica Contatto")
    update_my_window.geometry('400x200+760+300')
    #da vedere update_window.iconbitmap('')
    update_my_window.resizable(False, False)

    #richiedo il nome
    label = L.Label(update_my_window, text = 'Inserisci Nuovo Nome', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto il nome
    new_name = L.StringVar()
    new_name_entry = L.ttk.Entry(update_my_window, textvariable = new_name)
    new_name_entry.pack(padx = 5, pady = 5)
        
    #bottone per la conferma, non metto il command qui per poter usare il doppio comando (enter e button, altrimenti la funzione che richiede un event non funzionerebbe col pulsante)
    name_button = L.ttk.Button(update_my_window, text = "Conferma")
    name_button.pack(pady = 10, padx = 10)

    #focus sulla casella di testo
    new_name_entry.focus()

    #se viene premuto invio o il pulsante chiama la funzione
    new_name_entry.bind("<Return>", update_contact)
    name_button.bind("<Button-1>", update_contact)
    
def Update_Contact(self):
    def update_contact(event):
        #se le entry non sono vuote faccio la modifica e aggiorno la tabella
        if name_entry.get() != "" and ip_entry.get() != "" and new_name_entry.get() != "":
            values = (new_name_entry.get(), name_entry.get(), ip_entry.get())
            result = self.DB.Update_Contact(values)
            for selected in self.tabella.get_children():
                Valore = self.tabella.item(selected)
                if(Valore["values"][0] == name_entry.get() and str(Valore["values"][1]) == ip_entry.get()):
                    self.tabella.item(selected, text ="", values = (new_name_entry.get(), ip_entry.get(), result))
        update_window.destroy()
                    
    #finestra per l'aggiunta di un contatto
    update_window = L.Toplevel(self.Root_win)
    update_window.grab_set()
    update_window.title("Modifica Contatto")
    update_window.geometry('450x200+760+300')
    #da vedere update_window.iconbitmap('')
    update_window.resizable(False, False)

    #richiedo il nome
    label = L.Label(update_window, text = 'Inserisci Nome', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto il nome
    name = L.StringVar()
    name_entry = L.ttk.Entry(update_window, textvariable = name)
    name_entry.pack(padx = 5, pady = 5)

    #richiedo l'ip
    label = L.Label(update_window, text = 'Inserisci IP', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()
        
    #variabile di appoggio, entry dove verrà scritto l'ip
    ip = L.StringVar()
    ip_entry = L.ttk.Entry(update_window, textvariable = ip)
    ip_entry.pack(padx = 5, pady = 5)

    #richiedo il nuovo nome
    label = L.Label(update_window, text = 'Inserisci Nuovo Nome', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto il nuovo nome
    new_name = L.StringVar()
    new_name_entry = L.ttk.Entry(update_window, textvariable = new_name)
    new_name_entry.pack(padx = 5, pady = 5)

    #bottone per la conferma, non metto il command qui per poter usare il doppio comando (enter e button, altrimenti la funzione che richiede un event non funzionerebbe col pulsante)
    name_button = L.ttk.Button(update_window, text = "Conferma")
    name_button.pack(pady = 10, padx = 10)

    #focus sulla casella di testo
    name_entry.focus()

    #se viene premuto invio o il pulsante chiama la funzione
    new_name_entry.bind("<Return>", update_contact)
    name_button.bind("<Button-1>", update_contact)
    
def Insert_Contact(self):
    def insert_contact(event):
        #se le entry non sono vuote faccio l'inserimento e aggiorno la tabella
        if name_entry.get() != "" and ip_entry.get() != "":
            values = (name_entry.get(), ip_entry.get(), )
            result = self.DB.Insert_Contact(values)
            values = (values[0], values[1], result, )
            self.tabella.insert('', L.END, values = values)
        add_window.destroy()
                
    #finestra per l'aggiunta di un contatto
    add_window = L.Toplevel(self.Root_win)
    add_window.grab_set()
    add_window.title("Aggiungi Contatto")
    add_window.geometry('400x200+760+300')
    #da vedere add_window.iconbitmap('')
    add_window.resizable(False, False)

    #richiedo il nome
    label = L.Label(add_window, text = 'Inserisci Nome', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()
        
    #variabile di appoggio, entry dove verrà scritto il nome
    name = L.StringVar()
    name_entry = L.ttk.Entry(add_window, textvariable = name)
    name_entry.pack(padx = 5, pady = 5)

    #richiedo l'ip
    label = L.Label(add_window, text = 'Inserisci IP', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto l'ip
    ip = L.StringVar()
    ip_entry = L.ttk.Entry(add_window, textvariable = ip)
    ip_entry.pack(padx = 5, pady = 5)

    #bottone per la conferma, non metto il command qui per poter usare il doppio comando (enter e button, altrimenti la funzione che richiede un event non funzionerebbe col pulsante)
    name_button = L.ttk.Button(add_window, text = "Conferma")
    name_button.pack(pady = 10, padx = 10)

    #focus sulla casella di testo
    name_entry.focus()

    #se viene premuto invio o il pulsante chiama la funzione
    ip_entry.bind("<Return>", insert_contact)
    name_button.bind("<Button-1>", insert_contact)
    
def Update_My_Contact(self):
    def Update_my_contact(event):
        #se le entry non sono vuote faccio la modifica e aggiorno la tabella
        if new_name_entry.get() != "":
            values = (new_name_entry.get(), )
            self.DB.Update_My_Contact(values)
            value = self.tabella.item('I001', 'values')
            self.tabella.item('I001', text ="", values = (new_name_entry.get(), value[1], value[2]))
        update_my_window.destroy()

    #finestra per l'aggiunta di un contatto
    update_my_window = L.Toplevel(self.Root_win)
    update_my_window.grab_set()
    update_my_window.title("Modifica Mio Contatto")
    update_my_window.geometry('400x200+760+300')
    #da vedere update_window.iconbitmap('')
    update_my_window.resizable(False, False)

    #richiedo il nome
    label = L.Label(update_my_window, text = 'Inserisci Nuovo Nome', font = ('Plantagenet Cherokee', 10), justify = 'center').pack()

    #variabile di appoggio, entry dove verrà scritto il nome
    new_name = L.StringVar()
    new_name_entry = L.ttk.Entry(update_my_window, textvariable = new_name)
    new_name_entry.pack(padx = 5, pady = 5)

    #bottone per la conferma, non metto il command qui per poter usare il doppio comando (enter e button, altrimenti la funzione che richiede un event non funzionerebbe col pulsante)
    name_button = L.ttk.Button(update_my_window, text = "Conferma")
    name_button.pack(pady = 10, padx = 10)

    #focus sulla casella di testo
    new_name_entry.focus()

    #se viene premuto invio o il pulsante chiama la funzione
    new_name_entry.bind("<Return>", Update_my_contact)
    name_button.bind("<Button-1>", Update_my_contact)

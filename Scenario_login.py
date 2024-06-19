#dichiarazione del database
database={ 
    "nome_login":"Pino",
    "password":"12345",
    "dom1":"Qual è il tuo colore preferito? ", #1 domanda segreta
    "risp1":"giallo", #risposta alla prima domanda segreta
    "dom2":"Qual è il tuo animale preferito? ", #2 domanda segreta
    "risp2":"cane"            #risposta alla seconda domanda segreta
}
nome=input("Inserisci il nome utente: ") #acquisizione nome login
password=input("Inserisci la password: ") #acquisizione password login

if(nome==database.get("nome_login") and (password==database.get("password"))): #se il nome e la password inseriti corrispondono ai valori nel database
     print("Benvenuto")
     print("Scegli tra queste due domande:\n",database.get("dom1"),"\n",database.get("dom2")) #visualizzazione delle due domande segrete del database
     scelta=input("Digita 1 per scegliere la prima o 2 per scegliere la seconda domanda: ") #selezione di una delle due domande segrete
     if (scelta=="1"):  #se sceglie la prima domanda
          colore=input(database.get("dom1")) #richiede l'inserimento della risposta alla domanda segreta
          if(colore==database.get("risp1")): #se la risposta corrisponde a quella contenuta nel db
               print("Benveuto, la risposta alla domanda segreta è corretta")
               print("Visualizzazione menù opzioni disponibili:") #visualizzazione menù opzioni di modifica disponibili
               print("1.Aggiungi campo\n2.Modifica campo")
               selez=input("Seleziona un valore: ")
               if(selez=="1"): #se seleziona "Aggiungi campo"
                        chiave_agg=input("Digita un campo da inserire: ") #input della nuova chiave che si desidera inserire
                        val_agg=input("Digita un valore da inserire per il campo: ") #nuovo valore della nuova chiave
                        database[chiave_agg]=val_agg #inserimento della nuova chiave e del suo nuovo valore
                        print("valori inseriti: ") #visualizza sia 
                        print(chiave_agg, val_agg) #la nuova chiave e il nuovo valore aggiunti
                        print(database) #sia l'intero db
               elif(selez=="2"):  #se selezione "Modifica campo"
                        chiave_mod=input("Digita un campo da modificare: ")   #richiede di inserire la chiave che va modificato 
                        print(" Il campo selezionato è: ",database.get(chiave_mod))   #visualizza il valore della chiave selezionata
                        val_mod=input("Digita un valore da inserire per il campo: ") #chiede l'input del nuovo valore da inserire nella chiave selezionata
                        database[chiave_mod]=val_mod #modifica il valore della chiave
                        print(database)       #visualizza il db modificato

     elif(scelta=="2"):  #se seleziona la seconda domanda segreta
          anim=input(database.get("dom2")) #richiede l'inserimento della risposta alla domanda segreta
          if(anim==database.get("risp2")): #se la risposta corrisponde a quella contenuta nel db
               print("Benvenuto, la risposta alla domanda segreta è corretta") #si comporta come per la domanda 1
               print("Visualizzazione menù opzioni disponibili:")
               print("1.Aggiungi campo\n2.Modifica campo")
               selez=input("Seleziona un valore: ")
               if(selez=="1"):
                        chiave_agg=input("Digita un campo da inserire: ")
                        val_agg=input("Digita un valore da inserire per il campo: ")
                        database[chiave_agg]=val_agg
                        print("valori inseriti: ")
                        print(chiave_agg, val_agg)
                        print(database)
               elif(selez=="2"):
                        chiave_mod=input("Digita un campo da modificare: ")
                        print(" La domanda è: ",database.get(chiave_mod))
                        val_mod=input("Digita un valore da inserire per il campo: ")
                        database[chiave_mod]=val_mod
                        print(database)
     else:  #se ha inserito un numero diverso da quelli richiesti per selezionare la domanda...
          print("Scelta sbagliata") #...termina il programma

elif (nome==database.get("nome_login") and (password!=database.get("password"))):  #se è corretto il nome ma non la password
      print("password errata") #output password sbagliata
else:
     print("Nome utente inesistente") #oppure se ha sbagliato il nome, stampa l'errore
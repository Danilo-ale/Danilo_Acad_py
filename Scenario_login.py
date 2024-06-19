database={
    "nome_login":"Pino",
    "password":"12345",
    "dom1":"Qual è il tuo colore preferito? ",
    "risp1":"giallo",
    "dom2":"Qual è il tuo animale preferito? ",
    "risp2":"cane"
}

nome=input("Inserisci il nome utente: ")
password=input("Inserisci la password: ")

if(nome==database.get("nome_login") and (password==database.get("password"))):
     print("Benvenuto")
     print("Scegli tra queste due domande:\n",database.get("dom1"),"\n",database.get("dom2"))
     scelta=input("Digita 1 per scegliere la prima o 2 per scegliere la seconda domanda: ")
     if (scelta=="1"):
          colore=input(database.get("dom1"))
          if(colore==database.get("risp1")):
               print("Benveuto, la risposta alla domanda segreta è corretta")
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

     elif(scelta=="2"):
          anim=input(database.get("dom2"))
          if(anim==database.get("risp2")):
               print("Benvenuto, la risposta alla domanda segreta è corretta")
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
     else:
          print("Scelta sbagliata")

elif (nome==database.get("nome_login") and (password!=database.get("password"))):
      print("password errata")
else:
     print("Nome utente inesistente")


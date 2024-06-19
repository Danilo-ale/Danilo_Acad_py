nome_login="pino"
cogn_login="verde"
passw_login="12345"
nome=input("inserisci il tuo nome: ")
if(nome_login==nome.lower()):
    cognome=input("Ciao "+nome_login+", inserisci il tuo cognome: ")
    if(cogn_login==cognome.lower()):
        password=input("Ciao "+ nome_login +" "+ cogn_login + ", inserisci password: ")
        if(passw_login==password):
            print("Accesso consentito")
        else:
            print("Accesso negato")
    else:
        print("Cognome errato")

else:
    print("Nome errato")
import random
database={
    "utente1":["pino", "1234"],
    "utente2":["gerryscotti","098"]
}

def accesso(nome, passw):
    for credenziali in database.values():
        if nome==credenziali[0] and passw ==credenziali[1]:
            return True
    return False

def primo(num):
    if int(num)%2==0:
        return False
    else:
        return True


while True:
    lista_cas=[]
    nome=input("Inserisci nome utente: ")
    passw=input("Inserisci password: ")
    acc=accesso(nome,passw)
    if acc:
        numero=0
        while numero<=0:
            numero=int(input("Inserisci un numero positivo: "))     #input numero
            if(numero<=0):          #controllo num positivo
             print("Devi inserire un numero positivo. ")
        while True:
            
            numeri=[*range(1,numero+1)]     #creazione range
            print("Menù:")      #menù
            print("1. Genera numeri casuali")
            print("2. Somma dei numeri pari")
            print("3. Stampa i numeri dispari")
            print("4. Numero primo?")
            print("5. Visualizza numeri primi")
            print("6. verifica se la somma nella lista sono numeri primi")
            scelta=input("scegli una delle opzioni: ")
            if scelta=="1":
                contr=0
                while contr < numero:
                    lista_cas.append(random.randint(1, numero))
                    contr+=1
                print(lista_cas)
            elif scelta=="2":
                if len(lista_cas)==0:
                    print("Lista numeri casuali vuota. Riprova prima con l'opzione precedente")
                else:
                    sum=0
                    for i in lista_cas:
                        if i%2==0:
                            sum+=int(i)
                    print("La somma dei numeri pari nella lista è: ", sum)
            elif scelta=="3":
                if len(lista_cas)==0:
                    print("Lista numeri casuali vuota. Riprova prima con l'opzione precedente")
                else:
                    for i in lista_cas:
                        if int(i)%2!=0:
                            print(i)
            elif scelta=="4":
                verifica=primo(int(numero))
                if verifica:
                    print("Numero primo")
                else:
                    print("numero non primo")
            elif scelta=="5":
                pass
            elif scelta=="6":
                pass
            else:
                print("Selezione sbagliata")
            scelta=input("Continuare? ").lower()
            if scelta!="si":
                break
    else:
        print("Utente sconosciuto")
    scelta=input("Ripetere il programma? ").lower()
    if scelta!="si":
        print("Chiusura")
        break
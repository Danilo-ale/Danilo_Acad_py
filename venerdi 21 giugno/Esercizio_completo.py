database={
    "nome_login":"Pino Postino",
    "password":"124"
}

while True:
    disp=[]
    numero=0

    print("Devi fare il login prima di visualizzare il menù:")
    nome=input("Inserisci nome utente: ")
    passw=input("Inserisci password: ")
    if(nome==database.get("nome_login").lower() and (passw==database.get("password"))):
        while numero<=0:
            numero=int(input("Inserisci un numero positivo: "))     #input numero
            if(numero<=0):          #controllo num positivo
             print("Devi inserire un numero positivo. ")
        while True:
            numeri=[*range(1,numero+1)]     #creazione range
            print("Menù:")      #menù
            print("1. Somma dei numeri pari")
            print("2. Stampa i numeri dispari")
            print("3. Numero primo?")
            scelta=input("Seleziona un opzione: ")
            if scelta=="1":             #se sceglie la prima opzione...
                sum=0
                for num in numeri:      #... si calcola la somma dei numeri che rispettano la condizione dei num pari
                    if num%2==0:
                        sum+=num
                print(f"La somma è {sum}")  #stampa sum
            elif scelta=="2":           #se sceglie la seconda opzione...
                print("Somma numeri dispari:")
                for num in numeri:      #stampa i numeri che rispettano la condizione dei num dispari
                    if num%2!=0:
                        print(num)
            elif scelta=="3":       #se sceglie l'opzione 3...
                div=2
                contr=True    #controllo che viene utilizzato per
                while contr and div<numero/2:
                    if numero%div==0:
                        contr=False
                    div+=1
                if contr==False:
                    print("Numero non primo")
                else:
                    print("Numero primo")

            else:
                print("selezione sbagliata")
            
            scelta=input("Ripetere il menù? ").lower()      #chiede se vuole ripetere il menù con le operazioni sul numero già inserito
            if scelta!="si":
                break
    else:
        print("Utente inesistente")
    scelta=input("Continuare con il programma? ").lower()       #chiede se vuole continuare ad usare il programma
    if scelta!="si":
        break
print("Arrivederci")
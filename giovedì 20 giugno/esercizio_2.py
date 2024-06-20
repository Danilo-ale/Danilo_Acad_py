"""
Esercizio su Python: Cicli e Condizioni
Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e 
stampa "Pari" se il numero è pari e "Dispari" se il numero è dispari.


Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un
 numero intero positivo n e stampa tutti i numeri da n a 0 (compreso),
   decrementando di 1.Deve potersi ripete all'infinito

Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e
 stampa il quadrato di ciascun numero nella lista.

Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema
 che prende in input una lista di numeri interi che precedente 
 è stata valorizzata dall'utente.
Il sistema deve:
Utilizzare un ciclo for per trovare il numero massimo nella lista.
Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, 
altrimenti stampare il numero massimo trovato e il numero di elementi nella lista
"""

lista=[]            #liste
lista2=[]   
while True:   #ripete il programma 
    print("Scegli un opzione:")      #menù
    print("1. Pari o dispari")
    print("2. Countdown")
    print("3. Quadrato di ogni elemento di una lista")
    print("4. Max, somma e numero elementi di una lista")
    sel=input("Seleziona un opzione: ")
    if(sel=="1"):           #se seleziona la prima opzione
        n=int(input("Inserisci un numero: "))
        if(n%2!=0):     #verifica che sia pari o dispari
             print("Numero primo")
        else:
            print("Numero non primo")     
    elif(sel=="2"):     #se seleziona 2
        while True:     #ripete ciò che fa il punto 2, come da traccia
            max=int(input("Inserisci il numero: "))  #richiede inserimento del numero del countdown
            if(max>0):      #se è maggiore di 0
                for i in reversed(range(0, max+1)):   #stampa il countdown
                    print(i)
            else:
                print("Numero non positivo")
            scelta=input("Continuare con il countdown? ")   #chiede se continuare con l'opzione 2
            if(scelta.lower()=="no"):
                break
            else:
                pass             
    elif(sel=="3"):     #se seleziona 3
        n_max=int(input("Quanti numeri nella lista? "))   #chiede quanti numeri vuole inserire
        for i in range(n_max):     #chiede di inserire i numeri
            numero=int(input("Scrivi il numero: "))
            lista.append(numero)        #li inserire nella lista
        print("Numeri al quadrato: ")
        for num in lista:
            print(num**2)       #stampa i numeri al quadrato di ciascuna posizione
    elif(sel=="4"):         #se seleziona 4
        print("Inserimento numeri in lista...")
        lista2=[]           #azzera la lista (magari precedentemente riempita)
        contr=True
        while contr==True:          #fa inserire i numeri in lista fino a quando vuole l'utente
            n=input("Inserire un numero: ")
            if(n.isnumeric()):      #controlla se è un numero
                lista2.append(n)    #li mette nella lista
            else:
                print("Non è un numero")
            scelta=input("Continuare? ")
            if(scelta.lower()!="si"):       #chiede se vuole continuare ad inserire numeri
                contr=False
        if(len(lista2)!=0):     #se la lunghezza della lista è <0...

            max=lista2[0]       #stabilisce che il max sia al primo posto
            for i in lista2:    
                if(i>max):      #verifica per ogni elemento se è > max precedente
                    max=i       #se è maggiore, diventa il nuovo max
            print("Il massimo della lista è:",max)
            counter=0
            sum=0           #azzero il counter e la variabile della somma
            while counter<len(lista2):          #ripete il while fino alla lunghezza della lista
                counter+=1      #somma il contatore
                sum=sum+int(lista2[counter-1])  #somma 
            print("La somma è:",sum)
            print("Il numero di elementi è:",counter)
        else:
            print("Lista vuota")    #stampa l'errore se la lista è vuota
    else:
        print("Comando sbagliato")
    cont=input("Continuare? ")
    if(cont.lower()=="no"):
        break

print("Terminazione")
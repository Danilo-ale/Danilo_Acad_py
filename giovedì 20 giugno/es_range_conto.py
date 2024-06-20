lista_nprimi=[]   #lista numeri primi da riempire

contr=True   #variabile di controllo

while contr:        #fino a quando la lista non è piena o l'utente vuole ripetere
    if(len(lista_nprimi)==5):   #se la lista è piena, chiude il ciclo
        print("Spiacente, lista numeri primi piena.")
        print(lista_nprimi)
        break
    max=int(input("Inserisci il numero: "))
    if(max%2!=0):   #controllo numero primo o no
        print("Numero primo")
        lista_nprimi.append(max)   #in caso sia un num primo viene aggiunto alla lista
        print("Attenzione, numeri primi in lista: ",len(lista_nprimi))
    else:
        print("Numero non primo")
    for i in reversed(range(0, max+1)):   #si fa il conto alla rovescia con il metodo reversed()
        print(i)
    rip=input("vuoi ripetere? ") #si chiede se si vuole continuare
    if rip.lower()=="no":
        contr==False

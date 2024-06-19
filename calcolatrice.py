"""
Descrizione: Scrivi un programma che chieda all'utente di inserire due
numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 

Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
non valida".
"""
while(True):
    operazioni=["+","-","*","/"]
    num1=int(input("inserisci il primo numero: "))
    num2=int(input("inserisci il secondo numero: "))
    print(num1, num2)
    oper=input("inserisci l'operazione da svolgere (+,-, *, /): ")


    if(oper=="+"):
        print(num1+num2)
    elif(oper=="-"):
        print(num1-num2)
    elif(oper=="/"):
        print(num1/num2)
    elif(oper=="*"):
        print(num1*num2)
    else:
        scelta=input("Operatore sbagliato. Continuare? Scrivere Si o No")
        if(scelta=="No"):
            break
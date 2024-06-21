"""Scrivi un sistema ché faccia quanto segue:

Chieda all'utente di inserire un numero intero positivo n.
Se il numero inserito non è positivo, chieda nuovamente l'inserimento fino a quando non viene inserito un numero positivo.
Una volta ottenuto un numero positivo n, il programma dovrà:
Stampare tutti i numeri pari da 0 a n inclusi.
Calcolare e stampare la somma di tutti i numeri dispari da 0 a n inclusi.
terminare solo dopo tre tentativi ("hai finito i tentativi") o dopo che una soma totale supera 250 ("hai vinto")"""

sum=0
tentat=0
while sum<250 and tentat<3:
    disp=[]
    num=0
    while(num<=0):     
        num=int(input("Inserisci un numero intero e positivo: "))
        if(num<=0):
            print("Devi inserire un numero positivo")
    tentat+=1
    numeri=[*range(0,num+1)]
    for i in numeri:
        print(i)
        if i%2!=0:
            disp.append(i)
    for i in disp:
        sum+=i

print("Somma: ", sum, "Numero tentativi:", tentat)
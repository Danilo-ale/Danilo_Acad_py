import random

def casuale():
    return random.randint(1,100+1)


def acquisizione():
    x=int(input("Inserisci un numero: "))
    return x
def verifica(num,x):            #funzione per verificase se ha indovinato
    if num==x:
        return True
    else:
        return False
    
def magmin(num,x):          #funzione per determinare maggiore o minore
    if (num>x):
        return True
    else:
        return False

x=casuale()
print(x)
while True:
    num=acquisizione()          #Input numero
    print(num)
    ver=verifica(num,x)     #chiama verifica
    if ver==True:
        print("Hai vinto!")
        break
    else:
        magg_min=magmin(num,x)          #chiama magmin
        if magg_min==True:
            print("numero maggiore di quello da indovinare")
        else:
            print("Numero minore di quello da indovinare")
        scelta=input("Continuare? ").lower()
        if scelta!="si":
            break

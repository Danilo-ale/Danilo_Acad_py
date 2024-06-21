lista=[]
while True:
    num=input("Inserisci numero: ")   #
    if num.isnumeric():         #controllo numero
        lista.append(num)       #append nella lista
    else:
        print("Scrivi un numero ")
    if(num=="0"):
        break
sum=0
for i in lista:     #sommo, facendo il cast all'elemento della lista
    sum+=int(i)

print("somma: ",sum)
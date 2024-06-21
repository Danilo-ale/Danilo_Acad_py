lista=[]
while True:
    num=input("Inserisci numero: ")
    if num.isnumeric():
        lista.append(num)
    else:
        print("Scrivi un numero ")
    if(num=="0"):
        break
sum=0
for i in lista:
    sum+=int(i)

print("somma: ",sum)
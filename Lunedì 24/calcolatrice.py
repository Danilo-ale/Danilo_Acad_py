num1=int(input("Inserisci primo numero: "))
num2=int(input("Inserisci secondo numero: "))
oper=input("Inserisci operazione: ")
if oper=="+":
    print(num1+num2)
elif oper=="-":
    print(num1-num2)
elif oper=="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("Non si può dividere per 0")
elif oper=="*":
    print(num1*num2)
else:
    print("Operatore non valido")

S=str(input("Dati elemente in sirul dat:"))
#a
x=S.count('A')
print(" Numarul de aparitii ale caracerului este ",x)
#b
for i in S:
    sir2=S.replace('A','*')
print("(A-*)Sirul obtinut este",sir2)
#c
for i in S:
    sir3=S.replace('B',' ')
print("(B) Sirul obtinut este",sir3)
#d
if 'MA' in S:
    y=S.count('MA')
    print(" Numarul de aparitii a silabei 'MA' in sir:",y)
else:
    print("Nu exista silaba 'MA' in sir" )
#e
if 'MA' in S:
    sir4=S.replace('MA','TA')
print("(TA) Sirul obinut este ",sir4)
#f

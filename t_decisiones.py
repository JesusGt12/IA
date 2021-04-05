print ("Toma de deciciones")
print("Ingrese los datos de la primera alternativa \n")
x1 = float(input("Ingresa cantidad a ganar:\t"))
p1 = float(input("Ingresa probabilidad de ganar:\t"))
x2 = float(input("Ingresa cantidad a perder:\t"))
p2 = float(input("Ingresa probabilidad de perder:\t"))
print("\n\nIngrese los datos de la segunda alternativa\n")
x11 = float(input("Ingresa cantidad a ganar:\t"))
p11 = float(input("Ingresa probabilidad de ganar:\t"))
x21 = float(input("Ingresa cantidad a perder:\t"))
p21 = float(input("Ingresa probabilidad de perder:\t"))

print("\nOpcion 1 : \nGanar ", x1," con ", p1, " de probabilidad o perder ", x2, " con ", p2, " de probabilidad ")
print("\nOpcion 2 : \nGanar ", x11," con ", p11, " de probabilidad o perder ", x21, " con ", p21, " de probabilidad ")

s1 = ((x1*(p1/100)) - (x2*(p2/100)))
s2 = ((x11*(p11/100)) - (x21*(p21/100))) 

if(s1>s2):
    print("\n La mejor Toma de Decision es la numero 1")
else:
    print("\n La mejor Toma de Decision es la numero 2")

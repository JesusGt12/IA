
import pandas as pd
print("FICHEROS EN CSV")
veces=int(input ("Cuantas veces desea realizar el proceso?\n"))

df=pd.DataFrame()
for i in range (veces):
    i=i+1
    print("**Ingresar datos del alumno**")
    nom = (input("Nombre:\t"))
    ap = (input("Apellidos:\t"))
    ed = int(input("Edad:\t"))
    gra = int(input("Grado:\t"))
    grup = int(input("Grupo:\t"))
    mail = (input("Email:\t"))

    data = {'Nombre': [nom],
        'Apellidos': [ap],
        'Edad': [ed],
        'Grado': [gra],
        'Grupo': [grup],
        'Email': [mail]}
    
    save=int(input("<<Guardar y Salir>> \n 1.- Si \n 2.- No "))
    df=df.append(data,ignore_index=True)
    
    if (save == 1):
        df.to_csv('example1.csv')
    else:
        print("Adios")

import xlrd
import pandas as pd

def entrenar(theta,fac_ap,w1,w2,epochs,x1,x2,d,n_muestras):
    errores = True
    while errores:
        errores = False
        for i in range(n_muestras): 
            z = ((x1[i] * w1)+(x2[i] * w2)) - theta # calculamos z
            
            if z >= 0:
                z = 1
            else:
                z = 0
            
            if z != d[i]:
                errores = True
                # calcular errores
                error = (d[i] - z)
                # ajustar theta
                theta = theta + (-(fac_ap * error))
                # ajustar pesos
                w1 = w1 + (x1[i] * error * fac_ap)
                w2 = w2 + (x2[i] * error * fac_ap)
                epochs +=1
                
    return w1, w2, epochs, theta
                

# ciclo principal
if __name__ == "__main__":
    # Leeemos el archivo excel or
    archivo_excel = pd.read_excel("/home/atlant/Documentos/IA/perceptron_data.xlsx")
    theta = 0.2# asignamos valor a tetha
    fac_ap = 0.2# factor de aprendisaje
    w1 = 0.4# peso 1
    w2 = 0.6# pesos 2
    epochs = 0# iteracciones para ajustar los pesos
    x1 = archivo_excel["x1"]
    x2 = archivo_excel["x2"]
    d = archivo_excel["d"]#valor deseado que toma los valores de la columna de del excel
    n_muestras = len(d)#numero de iteracciones
    w1, w2, epochs, theta = entrenar(theta,fac_ap,w1,w2,epochs,x1,x2,d,n_muestras)#nos devuelve los valores
    print ("w1 = ", w1)
    print ("w2 = ", w2)
    print ("Theta =", theta)
    print ("\n""epochs =", epochs)
    

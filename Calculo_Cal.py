import statistics
import time
import contextlib

def cal():
    #Declaracion de las variables
    su_name = input("Digite el Nombre del Estudiante: ")
    nota_1 = int(input("Digite el valor de la nota 1: "))
    nota_2 = int(input("Digite el valor de la nota 2: "))
    nota_3 = int(input("Digite el valor de la nota 3: "))
    nota_4 = int(input("Digite el valor de la nota 4: "))
    print("\n")
   
    #Lista de Notas 
    lista_notas = nota_1,nota_2,nota_3,nota_4
    #Calculo del Promedio
    promedio = int(statistics.mean(lista_notas))
    print("[~] Procesando el promedio.... ")
    time.sleep(1)

    #Condiciones
    if promedio >= 90:
        print("[+] El Promedio es " + str(promedio) + ", la nota es A")
    elif promedio > 79 and promedio <= 89:
        print("[+] El Promedio es " + str(promedio) + ", la nota es B")
    elif promedio > 69 and promedio <= 79:
        print("[+] El Promedio es " + str(promedio) + ", la nota es C")
    else:
        print("[+] La Nota es F")
        print(promedio)

    file_path = su_name + '.txt'
    with open(file_path, "w") as o:
        with contextlib.redirect_stdout(o):
            print("Califiacion de: " + su_name)
            if promedio >= 90:
                print("[+] El Promedio es " + str(promedio) + ", la nota es A")
            elif promedio > 79 and promedio <= 89:
                print("[+] El Promedio es " + str(promedio) + ", la nota es B")
            elif promedio > 69 and promedio <= 79:
                print("[+] El Promedio es " + str(promedio) + ", la nota es C")
            else:
                 print("[+] La Nota es F")

if __name__ == '__main__':
    cal()

#By Maicker Miguel Ravelo Flores (dstark)
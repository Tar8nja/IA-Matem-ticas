import numpy
import math
import matplotlib.pyplot as plt


def __main__():

    base_plaza=2.4
    altura_plaza=4.5
    amplitud_carril=3.5

    def Calculos(base1, altura1):
        def PlazasHilera():
            base_disponible=base1-(2*altura_plaza+2*amplitud_carril)
            plazas_hilera=base_disponible//base_plaza
            return plazas_hilera


        def PlazasVerticales():
            altura_disponible=altura1-(2*altura_plaza)
            plazas_verticales=altura_disponible//base_plaza
            return plazas_verticales


        def numCarriles():
            num_carriles=altura1//(2*altura_plaza+amplitud_carril)
            return num_carriles


        def numPlazas():
            plazas_horizontales=2*PlazasHilera()*numCarriles()
            plazas_verticales=2*PlazasVerticales()
            plazas_totales=plazas_verticales+plazas_horizontales
            return plazas_totales

        # print("Num total de plazas: ", numPlazas())

        area=base1*altura1
        if area==0: 
            return 0
        proportion=numPlazas()/area*100
        return proportion



    # - Input de Parámetros -
    parametro_min=float(input("Altura y base mínmas a analizar[m]: "))
    parametro_max=float(input("Altura y base máximas a analizar[m]: "))
    incremento=float(input("Distancia incrementada por paso[m]: "))
    matr_tamano=int((parametro_max-parametro_min)/incremento)
    matriz=numpy.zeros((matr_tamano,matr_tamano))
    print("Medidas de la matriz: ",matriz.shape)

    

    # - Cálculo de la matriz -
    tamano=int(math.sqrt(matriz.size))
    for i in range(tamano):
        for j in range(tamano):
            matriz[i][j]=Calculos(i*incremento+parametro_min,j*incremento+parametro_min)
        matriz[i][j]=Calculos(i*incremento+parametro_min,j*incremento+parametro_min)
    print(matriz)



    # - Creación del título del gráfico - 
    str_parametro_min=str(parametro_min)
    str_parametro_max=str(parametro_max)
    str_incremento=str(incremento)
    grf_tamano=(parametro_max-parametro_min)/incremento-0.5
    titulo="Optimización de "+str_parametro_min+"[m] hasta "+str_parametro_max+"[m] haciendo pasos de "+str_incremento+"[m]"
    plt.title(titulo)
    



    # - Pintar el gráfico -
    imagen=plt.imshow(matriz)
    imagen.set_cmap('coolwarm')
    plt.colorbar(imagen)
    plt.axis([-0.5, grf_tamano, -0.5, grf_tamano])
    plt.show()

__main__()
input()